from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from google import genai
from dotenv import load_dotenv
import json
import os
load_dotenv()
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route("/suggestions")
def suggestions():
    return render_template("suggestions.html")

@app.route("/Gemini_Request", methods=["POST"])
def Gemini_Request():

    print('getting key')
    #creates Gemini client with key (hard-coded)
    gemini_key = os.getenv("GEMINIKEY")
    print('key found')
    print(gemini_key)
    client = genai.Client(api_key=gemini_key)

    #get incoming JSON from frontend for now just test variables
    data = request.get_json()
    income = data["income"]
    fixed = data["fixed"]
    variable = data["variable"]
    intermittent = data["intermittent"]
    discretionary = data["discretionary"]
    current_saving = data["current_saving"]
    saving = data["saving"]
    
    prompt = (f"""
    You are a budgeting assistant for UC Irvine college students.

    Here is the user's budget data:
    Income (Monthly): {income}
    Fixed (expenses that remain the same every month): {fixed}
    Variable (Expenses that vary from month to month: {variable}
    Intermittent (Expenses that occur at various times only): {intermittent}
    Discretionary (Expenses to reward ourselves with): {discretionary}
    Current Savings (Today): {current_saving}
    Savings Goal (in one years time from today): {saving}

    Analyze this and provide responses in clear friendly English in a Dictionary format only with no surrounding characters. Do not add any additional text:
    Summary: A short summary (2-3 sentences) of their financial health.
    Suggestion1: personalized suggestion (2-3 sentences) to reach savings goal
    Suggestion2: personalized suggestion (2-3 sentences) to reach savings goal
    Suggestion3: personalized suggestion (2-3 sentences) to reach savings goal
    Encouragement:  An encouraging message (2-3 sentences) to help them  stay on track.
    recommendedSavings: Recommended amount to save each month (decimal value only)

    """)

    #sends the user's message to Gemini
    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
    )

    #turns the response back from Gemini into text
    text = response.text

    #uses imported json library to turn the text into a json file
    jsonData = json.loads(text)

    print(jsonData)


    #since we prompted gemini to return as dictionary we can call the key to get the value
    #print(jsonData['Suggestion 2'])

    return jsonify(jsonData)
if __name__ == "__main__":
    app.run(debug=True)

    