import fitz  # PyMuPDF

def extract_text_from_file(file):
    try:
        if file.name.endswith(".pdf"):
            doc = fitz.open(stream=file.read(), filetype="pdf")
            text = "".join(page.get_text() for page in doc)
            doc.close()
            return text

        elif file.name.endswith(".txt"):
            return file.read().decode("utf-8", errors="ignore")

        else:
            return "❌ Unsupported file format."

    except Exception as e:
        return f"❌ Error reading file: {str(e)}"
