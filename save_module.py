
from pathlib import Path
from datetime import datetime


OUTPUT_DIR = Path("outputs")
OUTPUT_FILE = OUTPUT_DIR / "medical_analysis.txt"


def save_medical_analysis(patient, symptoms, missing,
                          analysis, questions, guidance):

    OUTPUT_DIR.mkdir(exist_ok=True)

    with open(OUTPUT_FILE, "a", encoding="utf-8") as file:

        file.write("\n" + "=" * 60 + "\n")
        file.write("AI MEDICAL SYMPTOM ASSISTANT REPORT\n")
        file.write("=" * 60 + "\n")

        file.write(
            f"Date: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n\n"
        )

        file.write("PATIENT INFORMATION\n")
        for key, value in patient.items():
            file.write(f"{key.replace('_', ' ').title()}: {value}\n")

        file.write("\nREPORTED SYMPTOMS\n")
        for symptom in symptoms:
            file.write(f"- {symptom}\n")

        file.write("\nMISSING INFORMATION\n")
        for item in missing:
            file.write(f"- {item}\n")

        file.write("\nSYMPTOM ANALYSIS\n")
        file.write(analysis + "\n")

        file.write("\nFOLLOW-UP QUESTIONS\n")
        file.write(questions + "\n")

        file.write("\nMEDICAL ATTENTION GUIDANCE\n")
        file.write(guidance + "\n")

        file.write("\nDISCLAIMER\n")
        file.write(
            "This AI-generated response is intended for educational "
            "and informational purposes only. It is not a medical "
            "diagnosis and does not replace advice from a qualified "
            "healthcare professional. For serious, worsening or urgent "
            "symptoms, seek appropriate medical care.\n"
        )

    print(f"\nReport saved successfully to: {OUTPUT_FILE}")
