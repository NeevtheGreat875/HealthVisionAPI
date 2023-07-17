from flask import Flask, request
import imagerec

app = Flask(__name__)

@app.route('/callback', methods=['POST'])
def callback():
    image_file = request.data.decode('latin1')
    pred,con = imagerec.imagerecognise(image_file,"BrainTumuorModel.h5",labelpath="BrainTumuorLabels.txt")

    return str(pred)

if __name__ == '__main__':
    app.run()
