import os
import sys
import random
import string
from flask import Flask, request, json
from parser.parser import parse
from flask_cors import CORS
import logging
ROOT_DIR = os.path.dirname(__file__)
PARENT_DIR = os.path.dirname(__file__) + '/' + str(os.pardir)
sys.path.append(PARENT_DIR)

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "uploads"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
cors = CORS(app)
# gunicorn_logger = logging.getLogger('gunicorn.error')
# app.logger.handler = gunicorn_logger.handlers
# app.logger.setLevel(gunicorn_logger.level)


def get_random_string(length):
    var = ''.join(
        [
            random.choice(string.ascii_letters + string.digits)
            for n in range(length)
        ]
    )
    return var


def allowed_file(filename):
    ALLOWED_EXTENSIONS = set(['pdf'])
    return '.' in filename\
        and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/ocr', methods=['POST'])
def extract_fields():
    file_path = ''
    try:
        format = request.form['format']
        file = request.files['file']

        file_path = app.config['UPLOAD_FOLDER'] + "/"\
            + get_random_string(32) + ".pdf"
        file.save(file_path)
        text, patient = parse(file_path, format)
        
        app.logger.info("-------------------------------------------------------")
        app.logger.info(patient)
        response = app.response_class(
            response=json.dumps({
                "text": text,
                "patient": patient
            }),
            status=200,
            mimetype='application/json'
        )
        os.remove(file_path)
        return response

    except Exception as e:
        response = app.response_class(
                response=json.dumps({
                    "status": 0,
                    "message": "Some error occurred",
                    "error": str(e)
                }),
                status=500,
                mimetype='application/json'
            )
        if file_path:
            os.remove(file_path)
       
        return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
