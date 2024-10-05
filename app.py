from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

MACRO_TYPES = {
    "open_file": "Open File",
    "run_command": "Run Command",
    "key_press": "Key Press",
}

@app.route('/')
def index():
    return render_template('index.html', macro_types=MACRO_TYPES)

@app.route('/generate_script', methods=['POST'])
def generate_script():
    file_path = request.json['filePath']
    macro_action = request.json['macroAction']
    macro_type = request.json['macroType']
    
    script = generate_macro_script(macro_type, file_path, macro_action)
    
    return jsonify({'script': script})

def generate_macro_script(macro_type, file_path, macro_action):
    if macro_type == "open_file":
        return f"""
# El Gato Stream Deck Macro Script
# Macro Type: Open File
# File Path: {file_path}

import os

def open_file():
    try:
        os.startfile(r'{file_path}')
        print(f"Opened file: {file_path}")
    except Exception as e:
        print(f"Error: {{e}}")

if __name__ == "__main__":
    open_file()
"""
    elif macro_type == "run_command":
        return f"""
# El Gato Stream Deck Macro Script
# Macro Type: Run Command
# Command: {macro_action}

import subprocess

def run_command():
    try:
        subprocess.run('{macro_action}', shell=True, check=True)
        print(f"Executed command: {macro_action}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {{e}}")

if __name__ == "__main__":
    run_command()
"""
    elif macro_type == "key_press":
        return f"""
# El Gato Stream Deck Macro Script
# Macro Type: Key Press
# Key: {macro_action}

import pyautogui

def press_key():
    try:
        pyautogui.press('{macro_action}')
        print(f"Pressed key: {macro_action}")
    except Exception as e:
        print(f"Error: {{e}}")

if __name__ == "__main__":
    press_key()
"""
    else:
        return "Unsupported macro type"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
