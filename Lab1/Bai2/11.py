def doiGiay(s):
    giay = 0
    phut = 0
    gio = 0
    if(s < 60):
        giay = s
        print(f"{gio}h : {phut}m : {giay}s")
    elif(s < 3600 and s >= 60):
        phut = int((s - s % 60) / 60)
        giay = int(s % 60)
        print(f"{gio}h : {phut}m : {giay}s")
    else:
        gio = int((s - s % 3600) / 3600)
        phut = int(((s % 3600) - (giay % 3600) % 60) / 60)
        giay = int(s - phut * 60 - gio * 3600)
        print(f"{gio}h : {phut}m : {giay}s")

doiGiay(3700)