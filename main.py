import os
from flask import Flask, flash, request, redirect, url_for, jsonify
from flask_api import status
from werkzeug.utils import secure_filename
from mrz import getMRZData

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return writeError("No file present"), status.HTTP_400_BAD_REQUEST
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return writeError("No file present"), status.HTTP_400_BAD_REQUEST
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            uploaded_filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(uploaded_filepath)
            try: 
                mrz_data = getMRZData(uploaded_filepath)
            except Exception as e:
                print(e)
                return writeError("Something wrong"), status.HTTP_500_INTERNAL_SERVER_ERROR
            finally:
                os.remove(uploaded_filepath)
            return jsonify(mrz_data), status.HTTP_200_OK
        else:
            return writeError("Not a valid file"), status.HTTP_

    #Only POST
    return writeError("Method not allowed"), status.HTTP_405_METHOD_NOT_ALLOWED

def writeError(message):
    return jsonify({"Error": message})

if __name__ == '__main__':
    app.run(debug=True)
