from flask import Flask, render_template, request
import os
import pandas as pd
import threading
from utils.send_messages import send_common_message, send_personalized_messages

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/common', methods=['GET', 'POST'])
def common():
    if request.method == 'POST':
        file = request.files['excel']
        message = request.form['message']
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            # Start message sending in a background thread
            threading.Thread(target=send_common_message, args=(filepath, message)).start()

            return '''
                <h2>Messages are being sent in the background!</h2>
                <br>
                <a href="/" style="
                    display:inline-block;
                    padding: 10px 20px;
                    background-color: #25D366;
                    color: white;
                    text-decoration: none;
                    border-radius: 8px;
                    font-size: 16px;
                ">Back to Home</a>
            '''
    return render_template('common.html')

@app.route('/personalized', methods=['GET', 'POST'])
def personalized():
    if request.method == 'POST':
        file = request.files['excel']
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            # Start personalized messages in a background thread
            threading.Thread(target=send_personalized_messages, args=(filepath,)).start()

            return '''
                <h2>Messages are being sent in the background!</h2>
                <br>
                <a href="/" style="
                    display:inline-block;
                    padding: 10px 20px;
                    background-color: #25D366;
                    color: white;
                    text-decoration: none;
                    border-radius: 8px;
                    font-size: 16px;
                ">Back to Home</a>
            '''
    return render_template('personalized.html')

if __name__ == '__main__':
    app.run(debug=True)
