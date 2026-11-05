
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3.2"


def ask_ollama(prompt):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=300
        )

        response.raise_for_status()
        result = response.json()

        return result.get("response", "No response received.")

    except requests.exceptions.ConnectionError:
        return (
            "Error: Ollama is not running. "
            "Please start Ollama and try again."
        )

    except requests.exceptions.Timeout:
        return "Error: Ollama request timed out."

    except requests.exceptions.RequestException as error:
        return f"Ollama API Error: {error}"
