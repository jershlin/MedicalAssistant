def display_patient_profile(patient):
    print("\n===== PATIENT PROFILE =====")

    for key, value in patient.items():
        print(f"{key.replace('_', ' ').title()}: {value}")