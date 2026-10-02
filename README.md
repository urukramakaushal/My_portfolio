# Urukrama Kaushal: Portfolio 📊

A 3D animated portfolio: a Streamlit app embedding a Three.js site where **every section has its own 3D world**, plus an in-page resume viewer with downloads.

| Section | 3D background | Page effects |
|---|---|---|
| Home | Wireframe AI core + neural-network particle field | Loader, 3D letter drop-in, typing roles, magnetic buttons |
| About | Morphing data-sphere (2,600 particles) | Word-by-word blur reveal, 3D flip stat cards, counters |
| Skills | Spiral galaxy | Draggable 3D skill sphere, tilt cards, 3D marquees |
| Experience | Rotating DNA double helix | Scroll-drawn timeline, cards swing in from the sides |
| Projects | Synthwave wave terrain + sun | Deep 3D tilt with glare, layered depth, animated borders |
| Education | Tumbling wireframe solids | Draggable 3D cube, animated CGPA bar |
| Resume | Hyperspace warp tunnel | Floating 3D paper with holo sheen, full-screen viewer, PDF/DOCX download |
| Contact | Dotted globe with live connection arcs | Big 3D headline, click-to-copy email |

Plus: custom cursor, scroll progress bar, side dot navigation, scrambled section titles, grain overlay. Animations switch off automatically for visitors who prefer reduced motion.

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Customize
- **Content:** everything lives in `data.py`. Paste your project repo links into `PROJECTS`.
- **Resume:** replace `resume.pdf` and `resume.docx` (keep the same names, or change `RESUME_PDF` / `RESUME_DOCX` in `data.py`). The page preview is generated from the PDF automatically.
- **Look:** `template.html`.

## Deploy free (Streamlit Community Cloud)
1. Push this folder to GitHub (include `resume.pdf` and `resume.docx`).
2. Go to https://share.streamlit.io and sign in with GitHub.
3. Click **Create app**, pick this repo, branch `main`, main file `app.py`, then **Deploy**.