from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_script', methods=['POST'])
def generate_script():
    file_path = request.json['filePath']
    macro_action = request.json['macroAction']
    
    # Generate a basic macro script based on the inputs
    script = f"""
# El Gato Stream Deck Macro Script
# File Path: {file_path}
# Macro Action: {macro_action}

import os

def perform_action():
    try:
        os.system('{macro_action} "{file_path}"')
        print(f"Action '{macro_action}' performed on '{file_path}'")
    except Exception as e:
        print(f"Error: {{e}}")

if __name__ == "__main__":
    perform_action()
"""
    
    return jsonify({'script': script})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
