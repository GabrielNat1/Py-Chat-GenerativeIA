from flask import render_template, request, jsonify
import google.generativeai as genai
import os

# Configure a chave de API
genai.configure(api_key=os.environ['GOOGLE_AI_API_KEY'])
model = genai.GenerativeModel('gemini-pro')

from app import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    cmd = "seja normal, não faça textos sem sentido, não faça textos muito longos, caso não souber resonder, responda com 'não sei'."
    model.generate_content(cmd)
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"response": "Por favor, envie uma mensagem válida."})
    
    try:
        # Gera resposta do chatbot
        response = model.generate_content(user_input)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"response": "Erro ao processar a mensagem. Tente novamente mais tarde."})