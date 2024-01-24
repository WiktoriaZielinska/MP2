from flask import Flask, request
import subprocess
import socket
app = Flask(__name__)
seed = 0
@app.route('/', methods=['GET'])
def get_seed():
    return str(seed)
@app.route('/', methods=['POST'])
def update_seed():
    global seed
    seed = request.json['num']
    subprocess.Popen(['python3', 'stress_cpu.py'])
    return 'CPU Stress Test Success!.'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
