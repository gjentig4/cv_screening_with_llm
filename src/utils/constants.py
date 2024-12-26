"""Constants used throughout the CV screening system."""

# Candidate levels
ENTRY_LEVEL = "entry_level"
MID_LEVEL = "mid_level"

# Experience ranges (in years)
EXPERIENCE_RANGES = {
    ENTRY_LEVEL: (0, 2),
    MID_LEVEL: (2, 5),
}

# Technical skills pool
PROGRAMMING_LANGUAGES = [
    "Python", "R", "SQL", "Java", "C++", "JavaScript",
    "Julia", "MATLAB", "Scala"
]

ML_FRAMEWORKS = [
    "TensorFlow", "PyTorch", "Scikit-learn", "Keras", "XGBoost",
    "LightGBM", "Pandas", "NumPy", "SciPy", "Hugging Face"
]

DATA_TOOLS = [
    "Docker", "Git", "AWS", "GCP", "Azure", "Kubernetes",
    "Airflow", "MLflow", "DVC", "Weights & Biases"
]

# Education levels
EDUCATION_LEVELS = [
    "Bachelor's in Computer Science",
    "Bachelor's in Data Science",
    "Bachelor's in Statistics",
    "Bachelor's in Mathematics",
    "Master's in Computer Science",
    "Master's in Data Science",
    "Master's in Statistics",
    "Master's in Mathematics"
]

# Common project types
PROJECT_TYPES = [
    "Machine Learning Classification",
    "Natural Language Processing",
    "Computer Vision",
    "Time Series Analysis",
    "Recommendation Systems",
    "Data Pipeline Development",
    "A/B Testing",
    "Data Visualization",
    "Statistical Analysis",
    "ETL Pipeline",
    "Web Scraping and Data Collection",
    "API Development",
    "Database Design and Optimization",
    "Real-time Data Processing",
    "Data Quality Assessment",
    "Automated Reporting System",
    "Text Mining and Analytics",
    "Anomaly Detection System",
    "Data Warehousing",
    "Business Intelligence Dashboard",
    "Chatbot Development",
    "Image Processing Pipeline",
    "Sentiment Analysis",
    "Market Basket Analysis",
    "Customer Segmentation",
    "Fraud Detection System",
    "Social Media Analytics",
    "Search Engine Development",
    "Data Migration Project",
    "Performance Optimization"
]

# Generic role titles
ROLES = [
    "Data Scientist",
    "Machine Learning Engineer",
    "Data Analyst",
    "AI Engineer",
    "Research Assistant",
    "Data Science Intern",
    "Junior Data Scientist",
    "Junior ML Engineer",
    "Data Engineering Intern",
    "ML Research Intern"
]
