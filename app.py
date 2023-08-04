from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'

@app.route('/upload', methods=['POST'])
def upload_file():
    data = request.json

    if 'file' not in data:
        return jsonify({'error': 'No file part in the request'}), 400

    file_data = data['file']

    # Decode the Base64 encoded file content
    file_content = base64.b64decode(file_data)

    # Save the file to a desired location (e.g., 'uploads/' directory)
    with open('uploads/uploaded_file.pdf', 'wb') as f:
        f.write(file_content)

    return jsonify({'message': 'File uploaded successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
