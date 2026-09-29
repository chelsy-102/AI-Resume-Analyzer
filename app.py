import streamlit as st

st.title("AI Resume Analyzer")
st.write("Analyze your resume against a job description")

resume = st.text_area("Paste your Resume")
job_description = st.text_area("Paste Job Description")

skills = [
    "python",
    "java",
    "sql",
    "html",
    "css",
    "javascript",
    "react",
    "machine learning",
    "deep learning",
    "pandas",
    "numpy",
    "excel",
    "communication",
    "customer service",
    "problem solving",
    "teamwork"
]

if st.button("Analyze Resume"):

    if resume and job_description:

        resume_text = resume.lower()
        job_text = job_description.lower()

        required_skills = []
        matching_skills = []
        missing_skills = []

        for skill in skills:
            if skill in job_text:
                required_skills.append(skill)

                if skill in resume_text:
                    matching_skills.append(skill)
                else:
                    missing_skills.append(skill)

        if required_skills:
            match_percentage = (
                len(matching_skills) / len(required_skills)
            ) * 100
        else:
            match_percentage = 0

        st.subheader("Resume Analysis")

        st.write(
            f"Match Percentage: {match_percentage:.2f}%"
        )

        st.write("### Matching Skills")
        st.write(matching_skills)

        st.write("### Missing Skills")
        st.write(missing_skills)

    else:
        st.warning("Please enter both resume and job description.")