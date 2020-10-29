from flask import Flask, request
from flask_cors import CORS
import os
import json
from os import path
from typing import List, Dict
app = Flask(__name__)
current_path = "/"
CORS(app)

@app.route('/')
def hello_world():
   return "Hello World"

@app.route('/file')
def handle_file():
    filepath = request.args.get("path")
    with open(filepath,"r",encoding="utf-8") as f:
        return f.read()

@app.route("/save",methods=["POST"])
def handle_save():
    content = request.json["content"]
    filepath = request.args.get("path")
    import pdb; pdb.set_trace()
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
        return "saved"




@app.route('/list')
def handle_listing():
    current_dir = os.getcwd()
    dirpath = request.args.get("path")

    os.chdir(dirpath)

    files = os.listdir()
    files_info = []
    for filename in files:
        filetype = "file" if path.isfile(filename) else "dir"
        file_info = {"name" : filename,"type" : filetype}
        files_info.append(file_info)
    os.chdir(current_dir)
    return json.dumps(files_info)

    
if __name__ == "__main__":
    app.run()
