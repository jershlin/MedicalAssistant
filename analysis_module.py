
from utils import ask_ollama


def analyze_symptoms(prompt):
    print("\nAnalyzing symptoms using Ollama Llama 3.2...")
    print("Please wait...\n")

    analysis = ask_ollama(prompt)

    return analysis


def display_analysis(analysis):
    print("\n========== SYMPTOM ANALYSIS ==========")
    print(analysis)
    print("======================================")
