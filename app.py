import os
from flask import Flask, request, render_template, redirect, url_for
from common.img_helper import allowed_file
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/upload/', methods=['GET', 'POST'])
def image_upload():
    result = ''
    if request.method == 'POST':
        img = request.files['photo']
        if img and allowed_file(img.filename):
            file_name = secure_filename(img.filename)
            img.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))

        result = 'test'
        # return redirect(url_for('image_upload', result=result))

    return render_template('upload.html', result=result)
