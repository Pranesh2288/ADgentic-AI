import fitz # PyMuPDF


class BriefLoader:
    def load(self, path: str) -> str:
        doc = fitz.open(path)
        text = "".join(page.get_text() for page in doc)
        return text