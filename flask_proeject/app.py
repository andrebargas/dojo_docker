from flask import render_template, send_from_directory
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import base64
import os
import requests

app = Flask(__name__)
app.secret_key = 'some secret key'

ALLOWED_EXTENSIONS = set(['pdf'])

# client = pymongo.MongoClient('host', PORT)
# db = client["db"]
# documentos_col = db["collection"]



@app.route('/')
def main():
    return render_template('home.html')


@app.route('/insere')
def insere():
    # new_mongo_entry = {"conteudo": 1}
    #
    # status = documentos_col.insert_one(new_mongo_entry)
    return render_template('home.html')



if __name__ == "__main__":
    app.run()
