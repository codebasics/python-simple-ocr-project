import os
import sys
import logging
from flask import Flask, request, json
from utils.generic_utils import get_random_string, allowed_file
from parser.parser import parse
from flask_cors import CORS
ROOT_DIR = os.path.dirname(__file__)
PARENT_DIR = os.path.dirname(__file__) + '/' + str(os.pardir)
sys.path.append(PARENT_DIR)

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "uploads"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
cors = CORS(app)


@app.route('/ocr', methods=['POST'])
def ocr():
    file_path = ''
    try:
        format = request.form['format']
        file = request.files['file']

        file_path = app.config['UPLOAD_FOLDER'] + "/"\
            + get_random_string(32) + ".pdf"
        file.save(file_path)
        text, data, error = parse(file_path, format) # noqa
        
        app.logger.info("----------------------------------")
        app.logger.info(f"Data: {data}")
        app.logger.info("----------------------------------")
        response = app.response_class(
            response=json.dumps({
                "text": text,
                "data": data
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
