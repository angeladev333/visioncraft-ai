from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from roboflow import Roboflow
import requests
import os
import uuid


app = Flask(__name__)
api = Api(app)



@app.route('/')
def index():
    data ={
        'Type':'Person',
        'Age':18
    }
    return data

@app.route('/yolo')
def yolo():
    rf = Roboflow(api_key="KnKjHINSt6Is99kC3IXv")
    project = rf.workspace().project("vision-artificial-dataset")
    model = project.version(1).model

    # infer on a local image
    results = model.predict("server\\multiple_parts.jpg", confidence=10, overlap=30).json()
    results = results.get('predictions')
    parts = []
    for item in results:
        parts.append(item.get("class"))
    parts = list(set(parts))
    return parts

@app.route('/generate_pdf')
def generate_page():
    return "Hello World"

def generate_unique_filename(filename):
    _, extension = os.path.splitext(filename)
    unique_filename = str(uuid.uuid4()) + extension
    return unique_filename

@app.route("/upload_image", methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image = request.files['image']
    # Process and save the image as needed
    # For example, you can save it to a specific directory
    
    if image.filename == '':
        return jsonify({'error': 'No image uploaded'}), 400
    
    upload_folder = "tmp/"
    new_filename = generate_unique_filename(image.filename)

    uploaded_file_path = os.path.join(upload_folder, new_filename)

    image.save(uploaded_file_path)

    #use uploaded_file_path to do something

    return jsonify({'message': 'Image uploaded successfully'})

if __name__ == '__main__':
    app.run()

@app.route('/upload_to_ipfs')
def upload_to_ipfs():
    file = open("server\\multiple_parts.jpg", "rb")
    response = requests.post(
        "https://api.nftport.xyz/v0/files",
        headers={"Authorization": '4eee2cb8-3210-407c-9d3f-fbb8dcf09995'},
        files={"file": file}
    )
    return response.json()


if __name__ == '__main__':
    app.run(debug=True)