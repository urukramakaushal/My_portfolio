# Edit this file to update the website. No need to touch app.py or template.html.
NAME = "Urukrama Kaushal"
TITLE = "Data Science Student"
LOCATION = "Indore, Madhya Pradesh"
EMAIL = "urukramakaushal@gmail.com"
PHONE = "+91 9630463334"  # set to "" to hide it on the site
GITHUB = "https://github.com/urukramakaushal"
LINKEDIN = "https://www.linkedin.com/in/urukrama-kaushal-35673b1b2/"

# Resume files (put them next to app.py). The PDF is shown on the site; both can be downloaded.
# To update your resume, just replace these files. Set RESUME_DOCX = "" to offer only the PDF.
RESUME_PDF = "resume.pdf"
RESUME_DOCX = "resume.docx"

ROLES = ["Data Science Student", "ML & NLP Builder", "Full Stack Developer", "Chatbot Engineer"]

SUMMARY = (
    "Passionate Data Science student skilled in developing and applying machine learning "
    "and deep learning solutions. Experienced with Python, TensorFlow, PyTorch, and LangChain "
    "for chatbot development and NLP tasks. Strong foundation in data analysis, model building, "
    "and deployment. Eager to use data-driven problem solving to contribute to impactful projects."
)

# (label, value, text shown when the card flips)
STATS = [
    ("CGPA", "9.6 / 10", "B.Tech in Data Science at IPS Academy, Indore"),
    ("Students served", "~10,000", "by the Institute's Autonomous System I'm leading"),
    ("Faculty supported", "500+", "using the same campus platform every day"),
    ("Paperwork reduced", "90%", "by expanding the campus event-tracking system"),
]

SKILLS = {
    "Languages & Data": ["Python", "SQL", "Pandas", "NumPy", "Data Analysis"],
    "ML / AI": ["TensorFlow", "PyTorch", "LangChain", "NLP", "Deep Learning", "Scikit-learn"],
    "Tools & Web": ["Git", "GitHub", "Flask"],
}

EXPERIENCE = [
    {
        "role": "Full Stack Developer Trainee",
        "org": "IPS Academy, Indore",
        "when": "May 2024 – Present",
        "points": [
            "Expanded a campus management system that tracks academic events, reducing paperwork by 90%.",
            "Leading development of the Institute's Autonomous System, serving ~10,000 students and 500+ faculty.",
        ],
    },
    {
        "role": "Data Science Intern",
        "org": "Nanosystems Consulting Services Pvt. Ltd (on-site)",
        "when": "Sep 2022 – Nov 2022",
        "points": [
            "Built and optimized chatbot solutions.",
            "Hands-on with TensorFlow, LangChain, and PyTorch for deep learning and NLP applications.",
        ],
    },
]

PROJECTS = [
    {
        "name": "Custom Chatbot with Modified Answers",
        "desc": "Chatbot for domain-specific queries with customized answers. Uses TensorFlow, PyTorch and "
                "LangChain for NLP, intent recognition and context-aware, dynamic responses.",
        "tags": ["TensorFlow", "PyTorch", "LangChain", "NLP"],
        "icon": "🤖",
        "link": "",  # paste repo link, e.g. "https://github.com/urukramakaushal/chatbot"
    },
    {
        "name": "Movie Recommendation System",
        "desc": "Recommendation engine built with Python, Pandas and Scikit-learn, implementing both "
                "content-based and collaborative filtering.",
        "tags": ["Python", "Pandas", "Scikit-learn"],
        "icon": "🎬",
        "link": "",  # paste repo link
    },
]

EDUCATION = {
    "degree": "B.Tech (Data Science)",
    "school": "Institute of Engineering & Science, IPS Academy, Indore",
    "when": "Sep 2022 – Present",
    "note": "Current CGPA: 9.6/10",
    # the six faces of the spinning 3D cube
    "cube": ["B.Tech", "Data Science", "9.6 CGPA", "IPS Academy", "Since 2022", "Indore"],
}