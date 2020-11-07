from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import cv2
import os
import uuid
import sys

print(sys.version)

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/version')
def version():
    return sys.version

@app.route('/analyze', methods = ['POST'])
def analyze():
    f = request.files['file']
    basepath = os.path.dirname(__file__)
    file_path = os.path.join(basepath, 'uploads', str(uuid.uuid4()))
    f.save(file_path)

    #TODO: add model prediction
    im = cv2.imread(file_path)
    h, w, c = im.shape
    response = [{'min_x': w / 10, 'max_x': (w / 10) * 9, 'min_y': h / 10, 'max_y': (h / 10) * 9}]

    return jsonify(response)

