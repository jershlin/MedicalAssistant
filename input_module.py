def collect_patient_information():
    print("\n===== PATIENT INFORMATION =====")

    patient = {
        "age": input("Enter age: "),
        "sex": input("Enter sex (optional): "),
        "symptoms": input("Describe your symptoms: "),
        "duration": input("How long have you had these symptoms? "),
        "severity": input("Severity (Mild/Moderate/Severe): "),
        "medical_history": input("Relevant medical history: "),
        "medications": input("Current medications (optional): "),
        "allergies": input("Known allergies (optional): ")
    }

    return patient