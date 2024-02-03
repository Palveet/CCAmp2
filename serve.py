from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_post():
    subprocess.Popen(['python3', 'stress_cpu.py'])
    return 'CPU stress test initiated.', 202

@app.route('/', methods=['GET'])
def handle_get():
    hostname = socket.gethostname()
    private_ip = socket.gethostbyname(hostname)
    return 'This server\'s private IP address is: ' + private_ip, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
