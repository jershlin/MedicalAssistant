
DISCLAIMER = """
This AI-generated response is intended for educational
and informational purposes only.

It is not a medical diagnosis and does not replace advice
from a qualified healthcare professional.

For serious, worsening or urgent symptoms, seek
appropriate medical care.
"""


def generate_medical_guidance(patient):
    severity = patient.get("severity", "").strip().lower()

    print("\n========== MEDICAL ATTENTION GUIDANCE ==========")

    if severity == "severe":
        guidance = (
            "You have reported severe symptoms. Please seek "
            "prompt professional medical attention. If symptoms "
            "are potentially life-threatening, contact local "
            "emergency services immediately."
        )
    else:
        guidance = (
            "If symptoms are severe, rapidly worsening, persistent "
            "or concerning, seek appropriate professional medical "
            "care. This application cannot determine your clinical "
            "urgency."
        )

    print(guidance)
    return guidance


def display_disclaimer():
    print("\n========== DISCLAIMER ==========")
    print(DISCLAIMER)
    print("================================")
