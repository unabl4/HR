# https://app.codesignal.com/challenge/QTiyM5zk2mHmC8aox

def fallBack(t):
    g=t.split(':')
    h=int(g[0])
    if h in (0,12):
        g[1]=g[1][:2]+('AM' if t[-2:] == 'PM' else 'PM')
    g[0]=str((h-2)%12+1)
    return ':'.join(g) 
