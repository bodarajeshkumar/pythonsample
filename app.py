from flask import Flask, request, jsonify
import base64
import PyPDF2

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
    
    pdf_file_path = "uploads/uploaded_file.pdf"
    extracted_text = extract_text_from_pdf(pdf_file_path)
    print(extracted_text)

    return jsonify({'message': extracted_text}), 200

def extract_text_from_pdf(pdf_path):
    text = ""

    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        num_pages = pdf_reader.numPages

        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            text += page.extract_text()

    return text

if __name__ == '__main__':
    app.run(debug=True)
