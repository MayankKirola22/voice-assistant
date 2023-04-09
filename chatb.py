#-------------------------------------------------------------------------------------import section----------------------------------------------------------------------------------------

import random
import mail
import os
import netco
import tnd
import wikipedia
import wea
import netco
import loc
import nws
import timer
import ttsp
import sttp
import time
import webbrowser
import capture
import camera
import google_searchh

#----------------------------------------------------------------------------------function section-----------------------------------------------------------------------------------------
start=-5
stop=0
def chat(inp):

    if 'hello' in inp:
        out='Hi'

    if 'how are you' in inp:
        out='I am fine Thank you.'

    elif 'quit' in inp:
        out="quitting"

    elif 'your name' in inp:
        out='My Name is Zira.'

    elif ('capture' in inp or 'take' in inp or 'shoot' in inp) and ('picture' in inp or 'image' in inp or 'photo' in inp):
        ttsp.tts('3')
        time.sleep(0.5)
        
        ttsp.tts('2')
        time.sleep(0.5)

        ttsp.tts('1')
        time.sleep(0.5)

        ttsp.tts('capturing')
        capture.cap()
        out=''

    elif 'mirror mode' in inp:
        ttsp.tts('opening mirror mode')
        ttsp.tts('press q to quit')
        camera.cam()
        out=''

    elif 'timer for' in inp:
        ttsp.tts('timer started')
        timer.fultim(inp)
        out="Time's up"

    elif 'time' in inp:
        out="The time is "+tnd.tim()

    elif "date" in inp:
        out ='today is' +tnd.date()

    elif 'year' in inp:
        out='this is '+tnd.yer()

    elif 'month' in inp:
        out ='the current month is'+tnd.mont()
    
    elif 'day' in inp:
        out='today is'+tnd.day()

    elif 'play music'  in inp:
        music_dir = 'C:\\Users\\Mayan\\Music'
        songs = os.listdir(music_dir)
        randin = random.randint(0,len(songs))
        os.startfile(os.path.join(music_dir, songs[randin]))
        out='''ok sure
        playing music
        enjoy your music'''

#-------------------------------------------------------------------------------------------online section-----------------------------------------------------------------------------------

    else:
        n=netco.netconn()

        if 'network status' in inp or 'net status' in inp:
            n=netco.netconn()
            if n==1:
                out='You are connected to internet'
            else:
                out='You are not connected to internet'

        elif n==0:
            out='please connect to internet first'

        elif n==1:

            if 'tell something about' in inp or "tell about" in inp or  'tell me about' in inp or  'tell me something about' in inp or  'say somthing about' in inp or  'tell somthing about' in inp:
                query=inp[inp.find('about')+6:len(inp)]
                results = wikipedia.summary(query, sentences=2,auto_suggest=False,features="lxml")
                p="According to Wikipedia"
                b=results
                out=p+'\n'+results

            elif 'search wikipedia for' in inp:
                query = inp[inp.find('search wikipedia for')+21:len(inp)]
                try:
                    results = wikipedia.summary(query,sentences=2,auto_suggest=False)
                    p="According to Wikipedia"
                    b=results
                    out=p+'\n'+results
                except wikipedia.exceptions.DisambiguationError as e:
                    topics = wikipedia.search(query)
                    print (query,"may refer to: ")
                    for i, topic in enumerate(topics):
                        print (i, topic)
                    choice = int(input("Enter a choice: "))
                    assert choice in range(len(topics))
                    results = wikipedia.summary(topics[choice],sentences=2,auto_suggest=False)
                    p="According to Wikipedia"
                    b=results
                    out=p+'\n'+results
                
            elif 'search google for' in inp:
                query=inp[inp.find('search google for')+18:len(inp)]
                out='''ok sure
                    searching google for'''+query
                google_searchh.searcher(query)

            elif "open youtube" in inp:
                webbrowser.open("www.youtube.com")
                out='''ok sure
                    opening youtube on chrome'''

            elif 'weather in' in inp:
                query=inp[inp.find('weather in')+11:len(inp)]
                out=wea.whe(query)

            elif 'weather' in inp:
                out= wea.whe()

            elif 'location' in inp:
                n=loc.trueloc()
                out='your current location is '+n[0]+' , '+n[1]+' , '+n[2]+' , '+n[3]+'.'

            elif 'send' in inp and'mail' in inp and 'to' in inp and 'saying that' in inp:
                query1=inp[inp.find('to')+3:inp.find('saying that')]
                query2=inp[inp.find('saying that')+12:len(inp)]
                out=mail.es(query1,query2)

            elif 'send' in inp and 'mail' in inp and 'to' in inp and 'telling him that he' in inp:
                query1=inp[inp.find('to')+3:inp.find('telling him that he')]
                query2='You'+inp[inp.find('telling him that he')+19:len(inp)]
                out=mail.es(query1,query2)
                
            elif 'send' in inp and 'mail' in inp and 'to' in inp and 'telling him that' in inp:
                query1=inp[inp.find('to')+3:inp.find('telling him that')]
                query2=inp[inp.find('telling him that')+13:len(inp)]
                out=mail.es(query1,query2)
                
            elif 'send' in inp and 'mail' in inp and 'to' in inp and 'that says' in inp:
                query1=inp[inp.find('to')+3:inp.find('that says')]
                query2=inp[inp.find('that says')+10:len(inp)]
                out=mail.es(query1,query2)

            elif 'send' in inp and 'mail' in inp and 'to' in inp:
                query1=inp[inp.find('to')+3:len(inp)]
                ttsp.tts('what should i say')
                query2=sttp.stt()
                if 'say that' in query2:
                    content=inp[inp.find('say that')+9:len(inp)]

                elif 'tell him that he' in query2:
                    content='You'+inp[inp.find('tell him that he')+17:len(inp)]

                elif 'tell him that' in query2:
                    content=inp[inp.find('tell him that')+14:len(inp)]

                else:
                    content=query2
                out=mail.es(query1,content)

            elif 'send' in inp and 'mail' in inp:
                ttsp.tts('to whom')
                query1=sttp.stt()
                if 'to' in query1:
                    reciever=query1[query1.find('to')+3:len(query)]
                else:
                    reciever=query1
                ttsp.tts('what should i say')
                query2=sttp.stt()
                if 'say that' in query2:
                    content=inp[inp.find('say that')+9:len(imp)]

                elif 'tell him that he' in query2:
                    content='You'+inp[inp.find('tell him that he')+17:len(imp)]

                elif 'tell him that' in query2:
                    content=inp[inp.find('tell him that')+14:len(imp)]

                else:
                    content=query2
                out=mail.es(reciever,content)
            
            elif 'news' in inp:
                ttsp.tts('getting news')
                lst1=nws.news()
                global stop
                global start
                start+=5
                stop+=5
                out=""
                for i in range(start,stop):
                    ttsp.tts(lst1[i])

                    if i ==len(lst1):
                        ttsp.tts("that's all for now")
                        start=-5
                        stop=0
                        
            elif "open" in inp:
                query=inp[inp.find('open ')+5:len(inp)]
                google_searchh.openner(query)
                out=f'''ok sure
                    opening {query} on chrome'''

            else:
                query = inp
                out='Here Are the results i found on web'
                google_searchh.searcher(query)
    return out

