import base64
import io
import json
import pathlib

import streamlit as st
import streamlit.components.v1 as components

import data as d

HERE = pathlib.Path(__file__).parent

st.set_page_config(page_title=f"{d.NAME} | Portfolio", page_icon="📊", layout="wide",
                   initial_sidebar_state="collapsed")

# Hide Streamlit chrome and let the portfolio fill the whole page
st.markdown(
    """<style>
    #MainMenu, header, footer {visibility: hidden;}
    .stApp {background: #05060d;}
    .block-container {padding: 0 !important; max-width: 100% !important;}
    iframe {height: 100vh !important; border: 0; width: 100% !important;}
    </style>""",
    unsafe_allow_html=True,
)


def _b64(raw: bytes) -> str:
    return base64.b64encode(raw).decode("ascii")


def _stamp(path: pathlib.Path):
    return path.stat().st_mtime if path.exists() else None


@st.cache_data(show_spinner=False)
def load_resume(pdf_name: str, docx_name: str, stamp):
    """Read the resume files and render the PDF pages to images for the on-page viewer."""
    pdf_path = HERE / pdf_name if pdf_name else None
    docx_path = HERE / docx_name if docx_name else None
    has_pdf = bool(pdf_path and pdf_path.exists())
    has_docx = bool(docx_path and docx_path.exists())
    if not (has_pdf or has_docx):
        return None

    pages = []
    if has_pdf:
        try:
            import pypdfium2 as pdfium
            doc = pdfium.PdfDocument(str(pdf_path))
            for i in range(len(doc)):
                img = doc[i].render(scale=2.2).to_pil().convert("RGB")
                if img.convert("L").getextrema()[0] > 245:  # skip blank pages
                    continue
                buf = io.BytesIO()
                img.save(buf, "PNG", optimize=True)
                pages.append(_b64(buf.getvalue()))
        except Exception:
            pages = []  # viewer falls back to a placeholder; downloads still work

    return {
        "pages": pages,
        "pdf": _b64(pdf_path.read_bytes()) if has_pdf else None,
        "docx": _b64(docx_path.read_bytes()) if has_docx else None,
        "file": d.NAME.replace(" ", "_") + "_Resume",
    }


resume_pdf = getattr(d, "RESUME_PDF", "")
resume_docx = getattr(d, "RESUME_DOCX", "")
stamp = (_stamp(HERE / resume_pdf) if resume_pdf else None,
         _stamp(HERE / resume_docx) if resume_docx else None)

keys = ["NAME", "TITLE", "LOCATION", "EMAIL", "PHONE", "GITHUB", "LINKEDIN", "SUMMARY",
        "STATS", "SKILLS", "EXPERIENCE", "PROJECTS", "EDUCATION", "ROLES"]
payload = {k: getattr(d, k, "") for k in keys}
payload["RESUME"] = load_resume(resume_pdf, resume_docx, stamp)
payload = json.dumps(payload).replace("</", "<\\/")

html = (HERE / "template.html").read_text(encoding="utf-8")
components.html(html.replace("__DATA__", payload), height=900, scrolling=True)