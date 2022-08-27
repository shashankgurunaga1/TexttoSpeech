import traceback
from flask import Flask,render_template,request
from flask_cors import cross_origin
import pyttsx3


app=Flask(__name__)


def text_to_speech(text, gender):
    
    voice_dict = {'Male': 0, 'Female': 1}
    code = voice_dict[gender]

    print("code", code)

    engine = pyttsx3.init()
    print("engine initialization")

    # Setting up voice rate
    engine.setProperty('rate', 125)

    # Setting up volume level  between 0 and 1
    engine.setProperty('volume', 0.8)

    # Change voices: 0 for male and 1 for female
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[code].id)

    engine.say(text)
    engine.runAndWait()


@app.route('/',methods=['GET','POST']) 
def mainpage():
        msg="Enter the text to Translate!"
        return render_template('frontpage.html',msg=msg)



@app.route('/text_conversion',methods=['GET','POST']) 
def text_conversion():
    print("inside text_conversion")
    try:
        if request.method == 'POST':
            text = request.form['speech']
            gender = request.form['voices']
            print("text", text)
            print("gender", str(gender))
            gender1=str(gender)
            try:
                text_to_speech(text, gender1)
                msg="Voice Translation Successful!"
                print("msg   ",msg)
                return render_template('frontpage.html', msg=msg)
            except:
                print("inside text to speech except")
                traceback.print_exc()
                msg="voice conv not succesful111111"
                return render_template('frontpage.html', msg=msg)



    except:
        print("inside text conversion except")
        traceback.print_exc()
        msg="voice conv not succesful"
        return render_template('frontpage.html', msg=msg)

        

if __name__ == "__main__":
    app.run(port=8000, debug=True)