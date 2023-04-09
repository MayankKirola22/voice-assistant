import chatb
import ttsp
import sttp
ttsp.tts('''Hello
                     what can i do for you''')
while True:
        inp=sttp.stt()
        inp=inp.lower()
        x=chatb.chat(inp)
        ttsp.tts(x)
        if inp=='quit':
            break
