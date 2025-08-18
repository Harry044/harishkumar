from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from typing import List, Optional
import uuid
from datetime import datetime

load_dotenv()

app = FastAPI(title="Harish Kumar Portfolio API")

# CORS middleware for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data models
class ContactMessage(BaseModel):
    name: str
    email: str
    subject: str
    message: str
    timestamp: Optional[datetime] = None

class SkillCategory(BaseModel):
    category: str
    skills: List[str]

class Project(BaseModel):
    id: str
    title: str
    description: str
    tech_used: List[str]
    challenge: str
    outcome: str
    duration: str
    image_url: Optional[str] = None

class Education(BaseModel):
    degree: str
    institution: str
    percentage: Optional[str] = None
    year: str
    achievement: Optional[str] = None

class Certification(BaseModel):
    name: str
    issuer: str
    description: Optional[str] = None

# Updated portfolio data for Harish Kumar
portfolio_data = {
    "personal_info": {
        "name": "Harish Kumar",
        "title": "Aspiring Data Science & AI Enthusiast | Learning Python, SQL, Machine Learning & Power BI",
        "tagline": "Driven by Data. Powered by Purpose.",
        "about": "Aspiring Data Science & AI Enthusiast with a strong academic foundation in Economics. Currently learning Python, SQL, Machine Learning & Power BI to transition into data-driven roles. Passionate about leveraging analytical skills and cutting-edge technologies to solve real-world problems through data insights and artificial intelligence.",
        "email": "mr.harishgrewal514@gmail.com",
        "phone": "9805877514",
        "linkedin": "https://www.linkedin.com/in/harish044",
        "github": "https://github.com/Harry044",
        "naukri": "https://www.naukri.com/mnjuser/profile?id=&altresid",
        "soft_skills": ["Analytical Thinking", "Problem Solving", "Data Analysis", "Research Skills", "Communication"]
    },
    "skills": [
        {
            "category": "Data & Analytics Tools",
            "skills": ["Power BI Desktop", "MySQL", "Advanced Excel", "Data Visualization", "Statistical Analysis"]
        },
        {
            "category": "Programming Languages", 
            "skills": ["Python", "C++ Object Oriented Programming", "SQL", "Arduino IDE"]
        },
        {
            "category": "Core Competencies",
            "skills": ["Machine Learning", "Data Science", "Economic Analysis", "Research Methods", "Project Management"]
        }
    ],
    "projects": [
        {
            "id": str(uuid.uuid4()),
            "title": "Power Monitoring System",
            "description": "Developed a comprehensive Power Monitoring System using Arduino IDE, ESP8266 and C++ to monitor electrical power consumption. Integrated sensors and real-time data visualization for accurate analysis.",
            "tech_used": ["Arduino IDE", "ESP8266", "C++", "Sensors", "Real-time Data Visualization"],
            "challenge": "Creating an accurate and real-time power monitoring solution with proper data visualization",
            "outcome": "Successfully developed a working power monitoring system with real-time analysis capabilities",
            "duration": "Jun 2024 - Aug 2024"
        },
        {
            "id": str(uuid.uuid4()),
            "title": "Economic Data Analysis Project",
            "description": "Comprehensive analysis of economic trends using advanced Excel and statistical methods",
            "tech_used": ["Advanced Excel", "Statistical Analysis", "Data Visualization"],
            "challenge": "Analyzing complex economic data to derive meaningful insights",
            "outcome": "Generated actionable insights for economic trend analysis",
            "duration": "Academic Project"
        }
    ],
    "education": [
        {
            "degree": "M.A Economics",
            "institution": "Sardar Patel University (SPU)",
            "percentage": "Full Time",
            "year": "2022-2024",
            "achievement": None
        },
        {
            "degree": "B.A Economics",
            "institution": "Govt. College Bassa (Gohar)",
            "percentage": "Full Time", 
            "year": "2019-2022",
            "achievement": None
        },
        {
            "degree": "Class XII",
            "institution": "Himachal Pradesh Board",
            "percentage": "88%",
            "year": "2019",
            "achievement": "State Merit Award - Academic Excellence with brand-new laptop"
        },
        {
            "degree": "Class X",
            "institution": "Himachal Pradesh Board",
            "percentage": None,
            "year": "2017",
            "achievement": None
        }
    ],
    "certifications": [
        {
            "name": "NIELIT Certification Program",
            "issuer": "National Institute of Electronics & Information Technology (NIELIT)",
            "description": "Mandi Himachal Pradesh (Offsite) - Advanced IT and Electronics certification"
        },
        {
            "name": "State Merit Award - Academic Excellence",
            "issuer": "Government of Himachal Pradesh", 
            "description": "Recognized for securing 88% in Class 12 Board Exams (2019). Award included a brand-new laptop."
        },
        {
            "name": "Power BI Fundamentals",
            "issuer": "Self-Learning",
            "description": "Currently learning Power BI Desktop for data visualization and analytics"
        },
        {
            "name": "Python Programming",
            "issuer": "Self-Learning",
            "description": "Learning Python programming for data science and machine learning applications"
        },
        {
            "name": "MySQL Database Management",
            "issuer": "Self-Learning",
            "description": "Database design, management, and query optimization"
        },
        {
            "name": "Machine Learning Fundamentals",
            "issuer": "Self-Learning",
            "description": "Understanding core concepts of machine learning and AI"
        }
    ]
}

# API endpoints
@app.get("/api/")
def read_root():
    return {"message": "Harish Kumar Portfolio API"}

@app.get("/api/profile")
def get_profile():
    return portfolio_data["personal_info"]

@app.get("/api/skills")
def get_skills():
    return portfolio_data["skills"]

@app.get("/api/projects")
def get_projects():
    return portfolio_data["projects"]

@app.get("/api/education")
def get_education():
    return portfolio_data["education"]

@app.get("/api/certifications")
def get_certifications():
    return portfolio_data["certifications"]

@app.post("/api/contact")
def submit_contact(message: ContactMessage):
    # In a real application, you would save this to a database
    message.timestamp = datetime.now()
    return {"message": "Thank you for your message! I'll get back to you soon.", "status": "success"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8002))
    uvicorn.run("server:app", host="0.0.0.0", port=port, reload=True)