def extract_skills(text):
    with open("skills.txt", "r") as f:
        skills = [skill.strip().lower() for skill in f.readlines()]

    text_words = set(text.split())
    matched_skills = [skill for skill in skills if skill in text_words]

    return matched_skills
