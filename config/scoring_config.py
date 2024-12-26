"""Configuration file for scoring parameters and weights."""

SCORING_WEIGHTS = {
    "technical_skills": {
        "weight": 0.3,
        "components": {
            "python_proficiency": 0.4,
            "ml_frameworks": 0.4,
            "other_skills": 0.2
        }
    },
    "project_experience": {
        "weight": 0.3,
        "components": {
            "complexity": 0.4,
            "relevance": 0.3,
            "impact": 0.3
        }
    },
    "problem_solving": {
        "weight": 0.25,
        "components": {
            "approach": 0.5,
            "implementation": 0.5
        }
    },
    "growth_potential": {
        "weight": 0.15,
        "components": {
            "learning_trajectory": 0.6,
            "adaptability": 0.4
        }
    }
}

# Minimum score thresholds
MINIMUM_SCORES = {
    "technical_skills": 60,
    "project_experience": 50,
    "problem_solving": 60,
    "growth_potential": 50,
    "overall": 65
}

# GPT-4 configuration
LLM_CONFIG = {
    "model": "gpt-4",
    "temperature": 0.7,
    "max_tokens": 1000
}
