from flask import Flask, render_template, request
from PIL import Image
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods = ["POST"])
def compress_image():
    if "image" not in request.files:
        return "No image uploaded"
    
    image = request.files["image"]
    if image.filename == "":
        return "No file selected"
    
    img = Image.open(image)
    # img = img.resize((200,200))
    filepath = os.path.join(UPLOAD_FOLDER, image.filename)
    img.save(filepath)

    # print("Imgae Size:", img.size)
    # print("Imgae Format:", img.format)
    # print("Image Mode: ", img.mode)
    print(image.filename)
    return render_template("index.html", filename = image.filename)

app.run(debug = True)