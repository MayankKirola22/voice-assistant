import time
da={'Mon':'monday','Tue':'Tuesday','Wed':'Wednesday','Thu':'Thursday','Fri':'Friday','Sat':'Saturday','Sun':'Sunday'}
mo={'Jan':'January','Feb':'February','Mar':'March','Apr':'April','May':'May','Jun':'June','Jul':'July','Aug':'August','Sep':'September','Oct':'October','Nov':'November','Dec':'December'}
def yer():
    ti=time.ctime(time.time())
    n=ti[20:24]
    return n
def day():
    ti=time.ctime(time.time())
    x=ti[0:3]
    n=da[x]
    return n
def mont():
    ti=time.ctime(time.time())
    x=ti[4:7]
    n=mo[x]
    return n
def date():
    ti=time.ctime(time.time())
    n=ti[8:10]+mont()+yer()
    return n
def tim():
    ti=time.ctime(time.time())
    hr=int(ti[11:13])
    mn=ti[14:16]
    a='A M'
    if hr>12:
        a='PM'
        hr-=12
    n=str(hr)+'        '+mn+a
    return n
