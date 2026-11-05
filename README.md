# AI-Powered Medical Symptom Assistant

An AI-powered medical information assistant developed using **Python and Ollama Llama 3.2**. The application collects user-provided health information, extracts reported symptoms, identifies missing context, generates preliminary informational analysis, and provides follow-up questions and cautious medical guidance.

> **Important:** This project uses a locally hosted Ollama model as an alternative to the GPT-4 API. It does not use the actual GPT-4 API.

## Features

- Patient information collection (age, sex, symptoms, duration, severity, medical history, medications and allergies).
- Symptom extraction using keyword matching.
- Identification of potentially relevant missing information.
- Structured prompt generation.
- AI-powered preliminary symptom analysis using Ollama Llama 3.2.
- Follow-up question generation.
- Medical attention guidance.
- Medical disclaimer.
- Save generated analysis to a text report.
- Continuous menu-driven application.

## Technologies Used

- Python 3
- Ollama
- Llama 3.2
- Requests
- VS Code

## Project Structure

```text
MedicalAssistant/
│
├── main.py
├── input_module.py
├── profile_module.py
├── symptom_module.py
├── context_module.py
├── prompt_module.py
├── analysis_module.py
├── question_module.py
├── safety_module.py
├── save_module.py
├── utils.py
│
├── data/
│
├── outputs/
│   └── medical_analysis.txt
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/jershlin/MedicalAssistant.git
```

### 2. Open the project directory

```bash
cd MedicalAssistant
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Install and start Ollama

Download Ollama from:

https://ollama.com/

Pull the Llama 3.2 model:

```bash
ollama pull llama3.2
```

### 7. Run the application

```bash
python main.py
```

## Application Menu

The application provides the following options:

1. Enter Patient Information
2. Enter Symptoms
3. Analyze Symptoms
4. Generate Follow-up Questions
5. Display Possible Conditions
6. Display Medical Attention Guidance
7. Display Disclaimer
8. Save Report
9. Exit

## Output

The generated analysis is saved locally at:

```text
outputs/medical_analysis.txt
```

The report includes patient information, extracted symptoms, missing information, preliminary analysis, follow-up questions, medical attention guidance and a disclaimer.

The generated report is excluded from Git uploads to protect user-provided health information.

## Safety and Disclaimer

This application is intended for educational and informational purposes only.

- It does not provide a medical diagnosis.
- Possible conditions are informational possibilities, not confirmed conditions.
- It does not replace professional medical advice.
- It does not make reliable clinical triage decisions.
- Users should seek qualified medical attention for serious, worsening or urgent symptoms.

**Disclaimer:** This AI-generated response is intended for educational and informational purposes only. It is not a medical diagnosis and does not replace advice from a qualified healthcare professional. For serious, worsening or urgent symptoms, seek appropriate medical care.

## Author

**Jershlin Paul J**

## Course

**24CS2506 – Building Applications using GPT-4**

**Experiment 6 – AI-Powered Medical Symptom Assistant**

## Repository

https://github.com/jershlin/MedicalAssistant