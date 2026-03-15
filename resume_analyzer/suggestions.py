def generate_suggestions(resume_skills, job_skills):
    missing_skills = set(job_skills) - set(resume_skills)

    suggestions = []
    if missing_skills:
        suggestions.append("Add these missing skills: " + ", ".join(missing_skills))
    else:
        suggestions.append("Your skills match well with the job description.")

    return suggestions
