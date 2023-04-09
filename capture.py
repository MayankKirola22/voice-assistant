import cv2
import ttsp
import sttp
def cap():
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        cv2.imshow('frame', frame)
        videoCaptureObject.release()
        ttsp.tts('Do you want to save this image?')
        ans=sttp.stt()
        if 'yes' in ans or 'yea' in ans or "of course" in ans:
            cv2.imwrite("NewPicture.jpg",frame)
            ttsp.tts('picture saved.')
        elif 'no' in ans or 'nah' in ans or "not" in ans:
            ttsp.tts('ok,sure.')
        result = False
    cv2.destroyAllWindows()
