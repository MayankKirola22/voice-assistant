import pyttsx3
def tts(message):
    engine=pyttsx3.init()
    voice='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
    engine.setProperty('rate', 150)
    engine.setProperty('voice', voice)
    engine.say('{}'.format(message))
    engine.runAndWait()
