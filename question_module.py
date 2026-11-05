
from utils import ask_ollama


def generate_follow_up_questions(patient, symptoms, missing):
    prompt = f"""
You are a medical information assistant.

Patient age: {patient.get('age', 'Not provided')}
Sex: {patient.get('sex', 'Not provided')}
Duration: {patient.get('duration', 'Not provided')}
Severity: {patient.get('severity', 'Not provided')}

Reported symptoms:
{', '.join(symptoms)}

Missing information:
{', '.join(missing)}

Generate 5 relevant follow-up questions to understand
the reported symptoms better.

Ask clear, simple and relevant questions.

Do not diagnose the patient.
Do not prescribe medication.
Do not invent patient information.

If potentially serious symptoms are reported,
advise the user to seek appropriate professional
medical attention rather than relying on questions.

Return only a numbered list of questions.
"""

    return ask_ollama(prompt)


def display_follow_up_questions(questions):
    print("\n========== FOLLOW-UP QUESTIONS ==========")
    print(questions)
    print("=========================================")
