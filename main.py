from detector import detect_objects
from gtts import gTTS as speech

from flask import Flask, request
app = Flask(__name__)

@app.route('/detect',methods = ["GET"])
def audio_generator():
    imagename = request.args.get('imagename', '')
    objectlist = detect_objects(imagename)

    detected_message ="Tessro Aakha Initiated !"

    for obj in objectlist:
        detected_message += f"{obj} was detected! "

    detected_speech = speech(text=detected_message,lang="en",tld="com.np",slow=False)
    detected_speech.save(f"audios/{imagename}.mp3")

    return f"{objectlist}"

if __name__  == '__main__':
    app.run()
