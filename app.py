# chatbot_medical_v1.py
import openai
from openai import OpenAI

# Setup your client (use your actual API key here)
client = OpenAI(api_key="OPENAI_API_KEY")
def analyze_results(patient_data):
    prompt = f"""
    A doctor has received the following patient test results:

    {patient_data}

    Based on this data:
    1. Summarize the key findings.
    2. Rate the severity (Low, Moderate, High).
    3. Suggest possible medications or further tests (if needed).

    Please be concise and medically appropriate.
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    return response.choices[0].message.content

# Example usage
if __name__ == "__main__":
    sample_input = """
    - Blood Pressure: 165/100 mmHg
    - Heart Rate: 95 bpm
    - Fasting Glucose: 145 mg/dL
    - LDL Cholesterol: 190 mg/dL
    - Complaints: Headache, dizziness
    """

    result = analyze_results(sample_input)
    print("\n--- Chatbot Response ---\n")
    print(result)
