
def identify_missing_information(patient):
    missing = []

    symptoms = patient.get("symptoms", "").lower()
    history = patient.get("medical_history", "").strip().lower()
    severity = patient.get("severity", "").strip().lower()
    duration = patient.get("duration", "").strip().lower()

    if "fever" in symptoms and "temperature" not in symptoms:
        missing.append("Exact measured body temperature")

    if any(word in symptoms for word in ["cough", "fever", "breathing"]):
        missing.append("Whether breathing difficulty is present")

    if not duration:
        missing.append("Exact duration of symptoms")

    if not severity:
        missing.append("Severity of symptoms")

    if not history or history in ["none", "no", "not applicable"]:
        missing.append("Confirmation of relevant medical history")

    missing.append("Whether symptoms are improving or worsening")
    missing.append("Presence of any additional symptoms")

    return missing


def display_missing_information(missing):
    print("\n===== MISSING INFORMATION =====")

    if missing:
        for item in missing:
            print("-", item)
    else:
        print("No missing information identified.")
