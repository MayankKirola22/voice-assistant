import speech_recognition as sr
def stt():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('listening.......')
        r.pause_threshold = 1
        audio=r.listen(source)
        print('analysing....')
        try:
            n=r.recognize_google(audio)
        except Exception as e:
            n='quit'
        print(n)
        return n
