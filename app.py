# app.py (Final, Fully AI-Powered Version)

import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
print("Backend server starting...")

# --- 1. Configure the Gemini API ---
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Gemini API key not found. Please set it in the .env file.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')
print("✅ Gemini API configured successfully.")

app = Flask(__name__)
CORS(app)

# --- 2. Define Candidate Labels ---
# We still provide the labels to guide the model's classification
candidate_labels = [
    'govt_job', 'marriage', 'nostalgia', 'comparison', 'money_advice', 
    'health', 'philosophy', 'study_abroad', 'job_shaming', 'random_fact', 
    'gulf_stories', 'politics', 'food_control'
]

# --- 3. THE NEW, ADVANCED PROMPT ---
# This prompt asks the model to generate the response text itself.
def create_prompt(advice_text):
    return f"""
    You are the "Sarcastic Ammavan Decoder". Your job, apparently, is to listen to yet another piece of cliché advice given in Malayalam and put it into a neat little box. You've heard it all before, but here we go again.

    Here's what you need to do, try to contain your excitement:
    1. Figure out which predictable category this advice falls into from this list: {', '.join(candidate_labels)}.
    2. Create a "classification_text" in Malayalam that dryly points out what type of cliché this is.
    3. Create a "recommended_action" in Malayalam. This should NOT be genuinely helpful. It should be a sarcastic or passive-aggressive way to endure the conversation and escape.

    Spit out ONLY a single, valid JSON object. Don't get creative with the format. It must have these four keys:
    - "label": The single best category name.
    - "confidence": Your confidence in how predictable this was, from 0.0 to 1.0.
    - "classification_text": The dry, sarcastic description in Malayalam.
    - "recommended_action": The unhelpful, sarcastic escape plan in Malayalam.
    
    For example, if the advice is "എത്രയും പെട്ടെന്ന് ഒരു സർക്കാർ ജോലിയിൽ കയറിപ്പറ്റാൻ നോക്ക്", your sarcastic response should be:
    {{
        "label": "govt_job",
        "confidence": 0.98,
        "classification_text": "അതെ, സ്ഥിരം സർക്കാർ ജോലി പുരാണം",
        "recommended_action": "ഒരു പുഞ്ചിരി പാസാക്കി മെല്ലെ സംഭാഷണത്തിൽ നിന്ന് ഊരിപ്പോരുക."
    }}
    
    Alright, brace yourself. Here's the piece of "wisdom" you have to deal with now.
    Advice to analyze: "{advice_text}"
    
    JSON Response:
    """

# --- 4. The API endpoint ---
@app.route('/analyze', methods=['POST'])
def analyze_advice():
    data = request.get_json()
    advice_text = data['advice_text']
    
    prompt = create_prompt(advice_text)
    response = model.generate_content(prompt)
    
    try:
        cleaned_response_text = response.text.strip().replace("```json", "").replace("```", "")
        model_output = json.loads(cleaned_response_text)
        
        # We now get everything directly from the model's JSON response
        final_response = {
            "classification": model_output.get("classification_text", "അജ്ഞാതമായ ജ്ഞാനം"),
            "confidence": f"{float(model_output.get('confidence', 0)) * 100:.2f}%",
            "recommended_action": model_output.get("recommended_action", "സൂക്ഷിച്ച് കൈകാര്യം ചെയ്യുക.")
        }
        return jsonify(final_response)
        
    except (json.JSONDecodeError, AttributeError, KeyError) as e:
        print(f"Error parsing Gemini response: {e}")
        print(f"Raw response text: {response.text}")
        return jsonify({"error": "Failed to parse the model's response"}), 500

# --- 5. Run the App ---
if __name__ == '__main__':
    app.run(debug=True, port=8080)