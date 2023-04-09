import time
def nut(p):
    nu=[]
    n=[]
    for i in p:
        if i.isdigit()==True:
            n.append(i)
        else:
            j=''
            x=j.join(n)
            if x!='':
                nu.append(x)
            n=[]
    if len(nu)==1:
        if 'minute' in p:
            nu.append("0")
        elif 'second'in p:
            nu.insert(0,'0')
    return nu
def timers(mn,sc):
    tim=(int(mn)*60)+int(sc)
    x=time.sleep(tim)
    n="Time's up"
    return n
def fultim(p):
    ti=nut(p)
    mn,sc=ti[0],ti[1]
    b=timers(mn,sc)
    return b
