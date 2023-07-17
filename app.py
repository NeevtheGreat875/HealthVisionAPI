from flask import Flask, request
import imagerec

app = Flask(__name__)

@app.route('/callback', methods=['POST'])
def callback():
    image_file = request.files['image']
    pred,con = imagerec.imagerecognise(image_file,"BrainTumuorModel.h5",labelpath="BrainTumuorLabels.txt")

    return str(pred)
