from flask import Flask, render_template
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-script')
def run_script():
    script_path = os.path.join(os.getcwd(), 'people_counter.py')
    prototxt_path = os.path.join(os.getcwd(), 'detector', 'MobileNetSSD_deploy.prototxt')
    model_path = os.path.join(os.getcwd(), 'detector', 'MobileNetSSD_deploy.caffemodel')
    input_path = os.path.join(os.getcwd(), 'utils', 'data', 'tests', 'test_1.mp4')
    
    command = [
        'python', script_path, '--prototxt', prototxt_path, 
        '--model', model_path, '--input', input_path
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    return f"<pre>{result.stdout}\n{result.stderr}</pre>"

if __name__ == '__main__':
    app.run(debug=True)
