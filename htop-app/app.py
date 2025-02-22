from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the HTOP Monitor</h1><p>Visit <a href='/htop'>/htop</a> to view system info.</p>"

@app.route('/htop')
def htop_info():
    name = "Shivanshu Chauhan"  # Your actual name
    username = "razputshivanshu"  # Your actual username
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " IST"

    try:
        top_output = subprocess.check_output("top -bn1", shell=True, text=True)
    except Exception as e:
        top_output = str(e)

    response = f"""
    <h2>Name: {name}</h2>
    <h3>Username: {username}</h3>
    <h3>Server Time (IST): {server_time}</h3>
    <pre>{top_output}</pre>
    """
    
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
