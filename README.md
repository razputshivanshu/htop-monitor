# HTOP Monitor - Flask App

A simple Flask app that displays system info, including the current server time and top command output. Runs on GitHub Codespaces.

## Features

- Displays your name and username.

- Shows current server time (IST).

- Fetches system process info using top.

## Setup

1. Clone the Repo
```
git clone <your-repo-url>
cd <your-repo-name>
```
2. Install Flask
```
pip install flask
```
3. Run the App
```
python app.py
```
4. Make Port Public (Codespaces)

Open Ports panel → Find Port 5000 → Set to Public.

## Access

- Home: https://<your-codespace-name>-5000.app.github.dev/

- System Info: https://<your-codespace-name>-5000.app.github.dev/htop

## Example Output

```
Name: Shivanshu Chauhan
Username: razputshivanshu
Server Time (IST): 2025-02-22 07:18:59 IST

(top command output...)
```

