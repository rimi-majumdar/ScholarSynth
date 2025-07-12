# Smart Assistant with Memory

✅ Upload document → Get summary  
✅ Ask questions → Save & retrieve from DB  
✅ Challenge Me → Answer + Evaluation stored  
✅ View history by document and user  
✅ Built with Streamlit + SQLite + Together AI

## To Run:

pip install -r requirements.txt  
streamlit run main.py# 🗂️ ScholarSynth (Research Memory Assistant)

🔗 Live App: [https://scholarsynth.onrender.com](https://scholarsynth.onrender.com)

ScholarSynth is an intelligent, document-aware AI assistant designed to help users explore, understand, and interact with research papers, technical documents, or books. Users can upload a PDF or TXT file, receive concise summaries, ask contextual questions, or generate challenge questions and get feedback on their answers — all while maintaining memory of past sessions.

---

## 🚀 Features

- 📄 Upload PDF or TXT documents up to 200MB
- 📌 Automatically generate a summary of the uploaded document
- 🧠 Ask contextual questions directly from the content
- 📝 Challenge mode: generate comprehension questions and evaluate your answers
- 📂 Memory-enabled: View and manage past sessions in the sidebar
- 🗑️ Delete old sessions or revisit any uploaded document
- 🎨 Clean and modern UI with black theme and intuitive sidebar

---

## 📸 UI Preview

<img width="1917" height="872" alt="image" src="https://github.com/user-attachments/assets/78c2dd3d-b1c0-43a2-a810-8ccec1e00b78" />


<img width="1903" height="862" alt="image" src="https://github.com/user-attachments/assets/44ea2fa8-9452-4080-9069-d44370904c99" />

<img width="1589" height="574" alt="image" src="https://github.com/user-attachments/assets/7699392c-d1da-4f80-b302-d76aa3962271" />

<img width="1903" height="833" alt="image" src="https://github.com/user-attachments/assets/a4285793-c929-48e5-9da8-436b43a783ea" />

<img width="1912" height="803" alt="image" src="https://github.com/user-attachments/assets/5eec0729-e14e-4939-b8ed-4d624df29d4d" />

<img width="1908" height="830" alt="image" src="https://github.com/user-attachments/assets/0f2ed3e7-bfbd-4d51-b330-ee9e7fa07623" />

<img width="298" height="851" alt="image" src="https://github.com/user-attachments/assets/4797b808-6839-481e-a5be-5afc08b195c5" />






---

## 🛠️ Technologies Used

- Python
- Streamlit
- SQLAlchemy + SQLite (for session memory)
- PyMuPDF (for PDF parsing)
- Together AI API (LLaMA-3 for summarization, Q&A, evaluation)
- Hosted on Render

---

## 🧪 How to Run Locally

1. Clone this repository:

```bash
git clone https://github.com/your-username/scholarsynth.git
cd scholarsynth
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set your Together API key (optional override):

Edit `main.py` or `backend/utils.py` if you want to change the API key.

5. Run the app:

```bash
streamlit run main.py
```

---

## ⚙️ Deployment

The app is deployed on Render and accessible publicly via:

🔗 https://scholarsynth.onrender.com

To deploy your own version:

- Push the repo to GitHub
- Connect GitHub to Render
- Set the start command:
  ```bash
  streamlit run main.py --server.port=$PORT --server.address=0.0.0.0
  ```

Ensure your `.streamlit/config.toml` contains:

```toml
[server]
headless = true
port = "$PORT"
enableCORS = false
address = "0.0.0.0"
```

---

## 🧠 Credits

Built by [your-name] as part of a GenAI internship assignment to demonstrate:
- Document-aware summarization
- Contextual Q&A from source files
- Evaluation of user input using LLMs
- Persistent memory with per-user document history

---

## 📬 Feedback / Contributions

Feel free to fork this repo or suggest features via Issues or Pull Requests.  

