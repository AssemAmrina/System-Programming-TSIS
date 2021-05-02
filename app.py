from flask import Flask
import os
import subprocess
import requests
import weather_parser
import json
from ctypes import *

# Setting up for a callable C++ function:
# libCalc = CDLL("./libcalci.so")
# print(libCalc.greet())


app = Flask(__name__)

@app.route('/weather')
def index():
    days = weather_parser.foo()
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(days, f, ensure_ascii=False, indent=4)
    subprocess.call(["g++", "hello.cpp"])
    subprocess.call("./a.out")
    return json.dumps(days)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
