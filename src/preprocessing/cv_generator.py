"""Module for generating synthetic CV data."""

import random
from datetime import datetime, timedelta
from typing import List, Dict, Tuple, Optional
import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
from ..utils.constants import (
    ENTRY_LEVEL,
    MID_LEVEL,
    EXPERIENCE_RANGES,
    PROGRAMMING_LANGUAGES,
    ML_FRAMEWORKS,
    DATA_TOOLS,
    EDUCATION_LEVELS,
    PROJECT_TYPES,
    ROLES,
)

class CVGenerator:
    """Generate synthetic CVs for testing and development."""

    def __init__(self, output_dir: str):
        """Initialize the CV generator.
        
        Args:
            output_dir: Directory to save generated CVs
        """
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        
        # Initialize styles
        self.styles = getSampleStyleSheet()
        self.styles.add(ParagraphStyle(
            name='Custom',
            parent=self.styles['Normal'],
            spaceBefore=6,
            spaceAfter=6,
            alignment=TA_LEFT,
        ))

    def _generate_contact_info(self) -> Dict[str, str]:
        """Generate random contact information."""
        first_names = ["Alex", "Sam", "Jordan", "Taylor", "Morgan", "Casey"]
        last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia"]
        
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        email = f"{name.lower().replace(' ', '.')}@email.com"
        phone = f"+1-{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
        location = random.choice(["New York, NY", "San Francisco, CA", "Boston, MA", "Seattle, WA"])
        
        return {
            "name": name,
            "email": email,
            "phone": phone,
            "location": location
        }

    def _generate_education(self, level: str) -> List[Dict[str, str]]:
        """Generate education history based on candidate level."""
        education = []
        degree = random.choice(EDUCATION_LEVELS)
        
        end_year = datetime.now().year - random.randint(0, 2)
        start_year = end_year - random.randint(3, 4)
        
        education.append({
            "degree": degree,
            "period": f"{start_year} - {end_year}",
            "gpa": f"{random.uniform(3.0, 4.0):.2f}"
        })
        
        return education

    def _generate_experience(self, level: str) -> List[Dict[str, str]]:
        """Generate work experience based on candidate level."""
        experience = []
        min_years, max_years = EXPERIENCE_RANGES[level]
        
        num_positions = 1 if level == ENTRY_LEVEL else random.randint(1, 3)
        
        end_date = datetime.now()
        for _ in range(num_positions):
            duration = random.randint(min_years * 12, max_years * 12)  # in months
            start_date = end_date - timedelta(days=duration * 30)
            
            position = random.choice(ROLES)
            
            achievements = [
                f"Developed {random.choice(PROJECT_TYPES).lower()} using {random.choice(ML_FRAMEWORKS)}",
                f"Improved model performance by {random.randint(10, 50)}% using {random.choice(ML_FRAMEWORKS)}",
                f"Built data pipelines using {random.choice(DATA_TOOLS)} and {random.choice(PROGRAMMING_LANGUAGES)}",
                f"Collaborated with {random.randint(2, 5)} team members on {random.choice(PROJECT_TYPES).lower()}"
            ]
            
            experience.append({
                "position": position,
                "period": f"{start_date.strftime('%b %Y')} - {end_date.strftime('%b %Y')}",
                "achievements": random.sample(achievements, k=random.randint(2, 4))
            })
            
            end_date = start_date - timedelta(days=30)  # 1 month gap between positions
        
        return experience

    def _generate_skills(self, level: str) -> Dict[str, List[str]]:
        """Generate technical skills based on candidate level."""
        num_skills = {
            "programming": random.randint(1, 6),
            "frameworks": random.randint(1, 6),
            "tools": random.randint(1, 6)
        }
        
        return {
            "programming": random.sample(PROGRAMMING_LANGUAGES, k=num_skills["programming"]),
            "frameworks": random.sample(ML_FRAMEWORKS, k=num_skills["frameworks"]),
            "tools": random.sample(DATA_TOOLS, k=num_skills["tools"])
        }

    def _generate_projects(self, level: str) -> List[Dict[str, str]]:
        """Generate project experience based on candidate level."""
        num_projects = random.randint(2, 3) if level == ENTRY_LEVEL else random.randint(3, 5)
        projects = []
        
        for _ in range(num_projects):
            project_type = random.choice(PROJECT_TYPES)
            technologies = []
            if random.random() > 0.5:
                technologies.append(random.choice(ML_FRAMEWORKS))
            if random.random() > 0.5:
                technologies.append(random.choice(PROGRAMMING_LANGUAGES))
            if random.random() > 0.5:
                technologies.append(random.choice(DATA_TOOLS))
            
            description = f"Implemented {project_type.lower()}"
            if technologies:
                description += f" using {', '.join(technologies)}"
            
            result = random.choice([
                f"Achieved {random.randint(80, 99)}% accuracy",
                f"Reduced error rate by {random.randint(20, 50)}%",
                f"Improved efficiency by {random.randint(20, 70)}%",
                f"Automated {random.randint(10, 40)} hours of manual work per week",
                f"Processed {random.randint(100, 1000)}K data points daily",
                f"Reduced processing time by {random.randint(30, 80)}%"
            ])
            
            projects.append({
                "name": f"{project_type} Project",
                "description": description,
                "result": result,
                "technologies": technologies
            })
        
        return projects

    def _create_pdf(self, cv_data: Dict, filename: str):
        """Create a PDF version of the CV."""
        doc = SimpleDocTemplate(
            filename,
            pagesize=letter,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=72
        )
        
        story = []
        
        # Contact Information
        story.append(Paragraph(cv_data["contact"]["name"], self.styles["Heading1"]))
        contact_text = (
            f'{cv_data["contact"]["email"]} | {cv_data["contact"]["phone"]} | '
            f'{cv_data["contact"]["location"]}'
        )
        story.append(Paragraph(contact_text, self.styles["Custom"]))
        story.append(Spacer(1, 12))
        
        # Education
        story.append(Paragraph("Education", self.styles["Heading2"]))
        for edu in cv_data["education"]:
            edu_text = (
                f'<b>{edu["degree"]}</b><br/>'
                f'GPA: {edu["gpa"]} | {edu["period"]}'
            )
            story.append(Paragraph(edu_text, self.styles["Custom"]))
        story.append(Spacer(1, 12))
        
        # Experience
        story.append(Paragraph("Experience", self.styles["Heading2"]))
        for exp in cv_data["experience"]:
            exp_text = (
                f'<b>{exp["position"]}</b><br/>'
                f'{exp["period"]}'
            )
            story.append(Paragraph(exp_text, self.styles["Custom"]))
            for achievement in exp["achievements"]:
                story.append(Paragraph(f'• {achievement}', self.styles["Custom"]))
        story.append(Spacer(1, 12))
        
        # Skills
        story.append(Paragraph("Technical Skills", self.styles["Heading2"]))
        skills = cv_data["skills"]
        for category, skill_list in skills.items():
            story.append(Paragraph(f'<b>{category.title()}:</b> {", ".join(skill_list)}', 
                                self.styles["Custom"]))
        story.append(Spacer(1, 12))
        
        # Projects
        story.append(Paragraph("Projects", self.styles["Heading2"]))
        for project in cv_data["projects"]:
            project_text = (
                f'<b>{project["name"]}</b><br/>'
                f'{project["description"]}<br/>'
                f'Result: {project["result"]}<br/>'
                f'Technologies: {", ".join(project["technologies"])}'
            )
            story.append(Paragraph(project_text, self.styles["Custom"]))
            story.append(Spacer(1, 6))
        
        doc.build(story)

    def generate_cv(self, level: str = ENTRY_LEVEL) -> str:
        """Generate a complete CV and save it as PDF.
        
        Args:
            level: Candidate level (entry_level or mid_level)
            
        Returns:
            str: Path to the generated PDF file
        """
        if level not in [ENTRY_LEVEL, MID_LEVEL]:
            raise ValueError(f"Invalid level: {level}. Must be either {ENTRY_LEVEL} or {MID_LEVEL}")
        
        cv_data = {
            "contact": self._generate_contact_info(),
            "education": self._generate_education(level),
            "experience": self._generate_experience(level),
            "skills": self._generate_skills(level),
            "projects": self._generate_projects(level)
        }
        
        # Create filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(
            self.output_dir,
            f"cv_{level}_{cv_data['contact']['name'].lower().replace(' ', '_')}_{timestamp}.pdf"
        )
        
        # Generate PDF
        self._create_pdf(cv_data, filename)
        
        return filename
