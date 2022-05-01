from detector import detect_objects
from gtts import gTTS as speech

from flask import Flask, request, render_template, redirect, send_file
app = Flask(__name__)

@app.route('/audio.mp3')
def load_audio():
    return send_file('audio.mp3', attachment_filename='audio.mp3')

@app.route('/detect',methods = ["GET"])
def audio_generator():
    imagename = request.args.get('imagename', '')
    objectlist = detect_objects(imagename)
    print(objectlist)

    detected_message ="Third Vision Initiated !"

    if(len(objectlist)>0):
        personcount = objectlist.count('person')
        if personcount > 1:
            detected_message += f"{personcount} people were detected !"
        else:
            detected_message += f"{personcount} person was detected !"

        for obj in objectlist:
            if(obj!="person"):
                detected_message += f"{obj} was detected! "
    else:
        detected_message += " Nothing was detected."
    print(detected_message)

    detected_speech = speech(text=detected_message,lang="en",tld="com.np",slow=False)
    #audiopath = f"audios/{imagename}.mp3"
    audiopath = f"audio.mp3"
    detected_speech.save(audiopath)

    #return f"{objectlist}"
    #return render_template("audio2.html",audio=audiopath)
    return render_template("audio.html")

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = (file.filename)
        path = f"uploads/{filename}"
        file.save(path)
        return redirect(f"/detect?imagename=uploads/{filename}", code=302)
    elif request.method =='GET':
        return render_template('index.html') 
    

if __name__  == '__main__':
    app.run(host='0.0.0.0', port=5000)
