
from input_module import collect_patient_information
from profile_module import display_patient_profile
from symptom_module import extract_symptoms
from context_module import (
    identify_missing_information,
    display_missing_information
)
from prompt_module import generate_medical_prompt
from analysis_module import analyze_symptoms, display_analysis
from question_module import (
    generate_follow_up_questions,
    display_follow_up_questions
)
from safety_module import (
    generate_medical_guidance,
    display_disclaimer
)
from save_module import save_medical_analysis


def main():
    patient = None
    symptoms = []
    missing = []
    analysis = ""
    questions = ""
    guidance = ""

    while True:
        print("\n" + "=" * 50)
        print("       AI MEDICAL SYMPTOM ASSISTANT")
        print("=" * 50)
        print("1. Enter Patient Information")
        print("2. Enter Symptoms")
        print("3. Analyze Symptoms")
        print("4. Generate Follow-up Questions")
        print("5. Display Possible Conditions")
        print("6. Display Medical Attention Guidance")
        print("7. Display Disclaimer")
        print("8. Save Report")
        print("9. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            patient = collect_patient_information()
            symptoms = []
            missing = []
            analysis = ""
            questions = ""
            guidance = ""
            print("\nPatient information saved successfully!")

        elif choice == "2":
            if patient:
                patient["symptoms"] = input(
                    "\nDescribe your symptoms: "
                )
                symptoms = []
                analysis = ""
                questions = ""
                print("\nSymptoms entered successfully!")
            else:
                print("\nPlease enter patient information first.")

        elif choice == "3":
            if patient:
                print("\nExtracting symptoms...")
                symptoms = extract_symptoms(patient)

                print("\n===== REPORTED SYMPTOMS =====")
                if symptoms:
                    for symptom in symptoms:
                        print("-", symptom)
                else:
                    print("No matching symptoms extracted.")

                missing = identify_missing_information(patient)
                display_missing_information(missing)

                prompt = generate_medical_prompt(
                    patient, symptoms, missing
                )

                analysis = analyze_symptoms(prompt)
                display_analysis(analysis)

                questions = ""
                guidance = ""

            else:
                print("\nPlease enter patient information first.")

        elif choice == "4":
            if patient:
                if not symptoms:
                    symptoms = extract_symptoms(patient)

                if not missing:
                    missing = identify_missing_information(patient)

                questions = generate_follow_up_questions(
                    patient, symptoms, missing
                )
                display_follow_up_questions(questions)

            else:
                print("\nPlease enter patient information first.")

        elif choice == "5":
            if analysis:
                print("\n===== POSSIBLE CONDITIONS =====")

                start = analysis.find("3. Possible Conditions")
                end = analysis.find("4. Explanation")

                if start != -1:
                    if end != -1 and end > start:
                        print(analysis[start:end])
                    else:
                        print(analysis[start:])
                else:
                    print(
                        "Possible conditions section not found. "
                        "Please analyze symptoms again."
                    )
            else:
                print("\nPlease analyze symptoms first.")

        elif choice == "6":
            if patient:
                guidance = generate_medical_guidance(patient)
            else:
                print("\nPlease enter patient information first.")

        elif choice == "7":
            display_disclaimer()

        elif choice == "8":
            if patient and analysis:
                if not symptoms:
                    symptoms = extract_symptoms(patient)

                if not missing:
                    missing = identify_missing_information(patient)

                if not questions:
                    questions = "Not generated."

                if not guidance:
                    guidance = (
                        "If symptoms are severe, rapidly worsening "
                        "or concerning, seek appropriate professional "
                        "medical care."
                    )

                save_medical_analysis(
                    patient,
                    symptoms,
                    missing,
                    analysis,
                    questions,
                    guidance
                )
            else:
                print(
                    "\nPlease enter patient information and "
                    "analyze symptoms before saving."
                )

        elif choice == "9":
            print("\nThank you for using AI Medical Symptom Assistant.")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice. Enter a number from 1 to 9.")


if __name__ == "__main__":
    main()
