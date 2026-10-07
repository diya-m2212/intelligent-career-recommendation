# projects.py
# Recommends practical projects based on
# the student's recommended career and skill gaps.


PROJECT_RECOMMENDATIONS = {

    "AI_ML": [

        {
            "level": "Beginner",
            "title": "Student Performance Prediction",
            "description":
                "Build a machine learning model that predicts "
                "student academic performance using factors such "
                "as study time, attendance and previous scores.",
            "skills": [
                "Python",
                "Pandas",
                "NumPy",
                "Scikit-learn",
                "Data Analysis"
            ]
        },

        {
            "level": "Intermediate",
            "title": "Career Recommendation System",
            "description":
                "Build an ML system that recommends suitable "
                "career domains based on student skills, interests "
                "and academic performance.",
            "skills": [
                "Python",
                "Pandas",
                "Scikit-learn",
                "Machine Learning",
                "Data Preprocessing"
            ]
        },

        {
            "level": "Advanced",
            "title": "Intelligent Student Career Assistant",
            "description":
                "Build an intelligent application that combines "
                "career prediction, skill-gap analysis, project "
                "recommendations and personalized learning paths.",
            "skills": [
                "Machine Learning",
                "Python",
                "FastAPI",
                "PostgreSQL",
                "React",
                "Recommendation Systems"
            ]
        }
    ],


    "Data_Science": [

        {
            "level": "Beginner",
            "title": "Student Data Analysis Dashboard",
            "description":
                "Analyze student performance data and create "
                "visualizations showing marks, attendance and "
                "subject-wise performance.",
            "skills": [
                "Python",
                "Pandas",
                "NumPy",
                "Matplotlib",
                "Data Analysis"
            ]
        },

        {
            "level": "Intermediate",
            "title": "Sales Data Analytics System",
            "description":
                "Analyze sales data to identify trends, "
                "top-performing products and customer patterns.",
            "skills": [
                "Python",
                "Pandas",
                "SQL",
                "Data Visualization",
                "Statistics"
            ]
        },

        {
            "level": "Advanced",
            "title": "Business Intelligence Analytics Platform",
            "description":
                "Build a complete analytics platform that "
                "processes business data and provides insights "
                "through dashboards and reports.",
            "skills": [
                "Python",
                "SQL",
                "Statistics",
                "Data Visualization",
                "PostgreSQL"
            ]
        }
    ],


    "Software_Development": [

        {
            "level": "Beginner",
            "title": "Student Management System",
            "description":
                "Build an application for managing student "
                "records, courses, marks and attendance.",
            "skills": [
                "Java",
                "OOP",
                "SQL",
                "PostgreSQL"
            ]
        },

        {
            "level": "Intermediate",
            "title": "Resource Booking API",
            "description":
                "Build a backend API that allows users to view "
                "resources, create reservations and manage bookings.",
            "skills": [
                "Java",
                "Spring Boot",
                "REST API",
                "JWT",
                "PostgreSQL"
            ]
        },

        {
            "level": "Advanced",
            "title": "Full-Stack Job Recommendation Platform",
            "description":
                "Build a full-stack platform that recommends "
                "jobs based on student skills, education and "
                "career preferences.",
            "skills": [
                "Java",
                "Spring Boot",
                "React",
                "PostgreSQL",
                "REST API",
                "Machine Learning"
            ]
        }
    ],


    "Cloud_Computing": [

        {
            "level": "Beginner",
            "title": "Cloud Hosted Portfolio",
            "description":
                "Create a personal portfolio website and deploy "
                "it using a cloud platform.",
            "skills": [
                "HTML",
                "CSS",
                "Cloud Hosting",
                "Linux"
            ]
        },

        {
            "level": "Intermediate",
            "title": "Cloud-Based File Storage System",
            "description":
                "Build an application that allows users to upload "
                "and download files using cloud storage.",
            "skills": [
                "AWS S3",
                "Python",
                "REST API",
                "Cloud Storage",
                "IAM"
            ]
        },

        {
            "level": "Advanced",
            "title": "Cloud-Native Application Deployment",
            "description":
                "Build and deploy a backend application using "
                "cloud compute, managed database, networking "
                "and monitoring services.",
            "skills": [
                "AWS",
                "EC2",
                "S3",
                "RDS",
                "IAM",
                "Cloud Networking"
            ]
        }
    ],


    "Cybersecurity": [

        {
            "level": "Beginner",
            "title": "Password Security Analyzer",
            "description":
                "Build a tool that evaluates password strength "
                "and explains common password security risks.",
            "skills": [
                "Python",
                "Cybersecurity Basics",
                "Authentication"
            ]
        },

        {
            "level": "Intermediate",
            "title": "Network Monitoring Tool",
            "description":
                "Build a safe network monitoring application "
                "that records network activity and identifies "
                "unusual patterns.",
            "skills": [
                "Python",
                "Networking",
                "Linux",
                "Cybersecurity"
            ]
        },

        {
            "level": "Advanced",
            "title": "Security Monitoring Dashboard",
            "description":
                "Build a defensive security monitoring system "
                "that collects logs and highlights suspicious "
                "events.",
            "skills": [
                "Python",
                "Linux",
                "Networking",
                "Log Analysis",
                "Cybersecurity"
            ]
        }
    ]
}


def recommend_projects(career, student_data):

    if career not in PROJECT_RECOMMENDATIONS:

        return (
            "\nNo project recommendations available "
            "for this career."
        )

    projects = PROJECT_RECOMMENDATIONS[career]

    result = []

    result.append("\n")
    result.append("=" * 60)
    result.append("              PROJECT RECOMMENDATIONS")
    result.append("=" * 60)

    result.append(
        f"\nCareer: {career.replace('_', ' ')}"
    )

    result.append(
        "\nThese projects are designed to help you "
        "develop practical career skills."
    )

    for project in projects:

        result.append("\n" + "-" * 60)

        result.append(
            f"\n🚀 {project['level'].upper()} LEVEL"
        )

        result.append(
            f"   Project: {project['title']}"
        )

        result.append(
            f"\n   Description:"
        )

        result.append(
            f"   {project['description']}"
        )

        result.append(
            "\n   Skills you will practice:"
        )

        for skill in project["skills"]:

            result.append(
                f"   → {skill}"
            )

    result.append("\n" + "-" * 60)

    return "\n".join(result)