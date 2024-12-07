from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from helper_functions.data_analysis_helper import analyze_file

app = Flask(__name__)
CORS(app)

# Define the folder to save the uploaded files
UPLOAD_FOLDER = 'raw_files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed file extensions (you can modify this list based on your requirements)
ALLOWED_EXTENSIONS = {'csv', 'xlsx', 'txt', 'json'}

# Check if the file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route to upload the file and analyze it
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        # Secure the filename to prevent directory traversal attacks
        
        # Ensure the directory exists
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])

        # Save the file to the defined folder
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Use the helper function to process the file
        result = analyze_file(file_path)

        if result["success"]:
            return jsonify({"message": "File successfully uploaded!", "analysis": result["summary"]}), 200
        else:
            return jsonify({"error": result["error"]}), 400

    else:
        return jsonify({"error": "File type not allowed"}), 400

if __name__ == '__main__':
    app.run(debug=True)
