def extract_symptoms(patient):
    text = patient["symptoms"].lower()

    symptom_keywords = [
        "fever",
        "cough",
        "sore throat",
        "headache",
        "body pain",
        "fatigue",
        "vomiting",
        "nausea",
        "diarrhea",
        "runny nose",
        "chest pain",
        "breathing difficulty",
        "shortness of breath",
        "dizziness",
        "rash"
    ]

    extracted = []

    for symptom in symptom_keywords:
        if symptom in text:
            extracted.append(symptom.title())

    return extracted