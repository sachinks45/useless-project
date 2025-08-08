Ammavan Advice Authenticator 🧠👴
Basic Details
Team Name: [Team Pazham Pori] Team Members

Team Lead: SACHIN K S - COCHIN UNIVERSITY OF SCIENCE AND TECHNOLOGY
Member 2: ROHITH R - COCHIN UNIVERSITY OF SCIENCE AND TECHNOLOGY

Project Description
The Ammavan Advice Authenticator is a satirical web application that uses Google's state-of-the-art Gemini AI to analyze unsolicited advice, typically received from Keralite uncles ("Ammavans"). Users can either type or speak the advice directly into the app, which then provides a sarcastic classification and a recommended passive-aggressive response.

The Problem (that doesn't exist)
Every year, countless hours of productive chai-sipping and pazham pori-eating are momentarily disrupted by the critical social dilemma of receiving unsolicited advice at family functions. This barrage of well-meaning but often cliché wisdom has, until now, gone unaddressed by modern technology, leaving the youth of Kerala to fend for themselves with only polite nods and awkward smiles.

The Solution (that nobody asked for)
We have developed an over-engineered, cloud-based, AI-powered platform to tackle this non-issue head-on. It features a voice-activated interface, allowing users to verbally input "Ammavan" wisdom for real-time analysis. Our solution leverages the power of Large Language Models to decode this unsolicited wisdom, empowering users with a detailed analysis and a sarcastic, passive-aggressive escape plan to navigate these conversations.

Technical Details
Technologies/Components Used
For Software:

Languages Used: Python, HTML5, CSS3, JavaScript

Frameworks & APIs: Flask, Google Gemini API, Web Speech API (for browser-based Speech-to-Text)

Libraries Used: google-generativeai, python-dotenv

Tools Used: Visual Studio Code, Git, Google AI Studio

For Hardware:

Not Applicable for this project.

Implementation
For Software:
Installation

Clone the repository:

Bash

git clone [your-repo-link]
cd [your-repo-folder]
Create and activate a virtual environment (using Python 3.9+):

Bash

python -m venv venv
venv\Scripts\activate
Install the required packages:

Bash

pip install -r requirements.txt
(Or pip install google-generativeai python-dotenv Flask Flask-Cors)

Create a .env file in the root directory and add your Gemini API key:

GEMINI_API_KEY=YOUR_API_KEY_HERE
Run

Start the Flask backend server:

Bash

python app.py
Open the frontend by double-clicking the index.html file in your web browser. When prompted, allow the browser to access your microphone to use the voice feature.

Project Documentation
For Software:
Screenshots (Add at least 3)

The main interface, featuring options for both text and voice input.

The AI is deep in thought, processing the cliché with its advanced neural networks.

The final, sarcastically generated analysis and recommended course of action, delivered with confidence.

Diagrams

Application workflow: The user can either type or speak the advice. If spoken, the browser's Web Speech API transcribes it to text. The text is then sent from the frontend to the Flask backend. The backend constructs a prompt, gets a JSON response from the Gemini API, and returns the formatted result to be displayed on the webpage.

Project Demo
Video

[Add your demo video link here]
A walkthrough of the application, demonstrating a user entering advice via both text and voice and receiving a sarcastic, AI-generated analysis in real-time.

Team Contributions
Sachin:[UI/UX Design,Front-End]
Rohith: [AI Prompt Engineering,Voice Interface Integration]
