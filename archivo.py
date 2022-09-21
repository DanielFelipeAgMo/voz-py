from email.mime import audio
import webbrowser
import speech_recognition as sp

r = sp.Recognizer()
with sp.Microphone()as source:
    print("Hola soy tu asistente de voz")
    audio = r.listen(source)

    try:
        texto = r.recognize_google(audio)
        print("Creo que haz dicho : {} ".format(texto))
        print(texto)
        if "Colombia" in texto:
            webbrowser.open('https://www.gov.co/')
        if "Amazon" in texto:
            webbrowser.open('https://www.amazon.co/')
        if "Medellin" in texto:
            webbrowser.open('https://www.medellin.gov.co/')
    except:
        print('Sáquese esa papa de la boca que no le entiendo')
