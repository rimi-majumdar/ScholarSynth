import streamlit as st
import os
from datetime import datetime
from backend.processor import extract_text_from_file
from backend.summarizer import generate_summary
from backend.qna_engine import answer_question
from backend.challenge_generator import generate_challenges, evaluate_answers
from backend.models import SessionLocal, SessionRecord, QARecord

API_KEY = "tgp_v1_dM6JW4D9hN47uzNNphHj9q42OjinWLtCCvOAmRKY0SU"
st.set_page_config(page_title="Smart Assistant with Memory", layout="wide")

db = SessionLocal()

st.sidebar.title("🧠 Memory")
user = st.sidebar.text_input("Your name", value="guest")

# Show past sessions
st.sidebar.markdown("### 📄 Your Documents")
past_sessions = db.query(SessionRecord).filter_by(user=user).order_by(SessionRecord.timestamp.desc()).all()
for sess in past_sessions:
    with st.sidebar.expander(f"{sess.document_name} - {sess.timestamp.strftime('%b %d')}"):
        for qa in sess.questions:
            st.write(f"Q: {qa.question}")
            st.caption(f"A: {qa.answer[:100]}...")

uploaded_file = st.file_uploader("Upload PDF or TXT", type=["pdf", "txt"])
if uploaded_file:
    with st.spinner("Reading document..."):
        content = extract_text_from_file(uploaded_file)
        st.session_state.content = content

    doc_name = uploaded_file.name
    session_db = SessionRecord(user=user, document_name=doc_name)
    db.add(session_db)
    db.commit()
    st.session_state.session_id = session_db.id

    st.subheader("📄 Auto Summary")
    summary = generate_summary(content, API_KEY)
    st.success(summary)

    mode = st.radio("Choose Mode", ["Ask Anything", "Challenge Me"])
    if mode == "Ask Anything":
        q = st.text_input("Ask a question from this document")
        if q:
            answer = answer_question(content, q, API_KEY)
            st.write(answer)
            # Save to DB
            qa = QARecord(session_id=session_db.id, question=q, answer=answer)
            db.add(qa)
            db.commit()
    else:
        if st.button("Generate Challenge Questions"):
            questions = generate_challenges(content, API_KEY)
            st.session_state.questions = questions
            st.session_state.responses = [""] * len(questions)

        if "questions" in st.session_state:
            for i, q in enumerate(st.session_state.questions):
                st.markdown(f"**Q{i+1}: {q}**")
                st.session_state.responses[i] = st.text_area(f"Answer to Q{i+1}", key=f"ans_{i}")
            if st.button("Evaluate Answers"):
                results = evaluate_answers(content, st.session_state.questions, st.session_state.responses, API_KEY)
                for i, res in enumerate(results):
                    st.markdown(f"🧠 Feedback Q{i+1}: {res}")
                    qa = QARecord(session_id=session_db.id, question=st.session_state.questions[i], answer=res)
                    db.add(qa)
                db.commit()