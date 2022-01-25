
import time

def cozme(string):
    z=0
    a=" "
    dizi2=string.split(" ")
    print(dizi2)
    for i in dizi2:
        #print(i)
        
        if "2012" in i or string in "A":
            a=a+"a"
            z=z+1

        if "210002" in i or string in "B":
            a=a+"b"
            z=z+1
    
        if "210102" in i or string in"Ç":
            a=a+"c"
            z=z+1
    
    
        if "21002" in i or string in "D":
            a=a+"d"
            z=z+1

        if "202" in i or string in "E":
            a=a+"e"
            z=z+1
    
        if "200102" in i or string in "F":
            a=a+"f"
            z=z+1
    
    
        if "21102" in i or string in "G":
            a=a+"g"
            z=z+1

        if "200002" in i or string in "H":
            a=a+"h"
            z=z+1
    
        if "2002" in i or string in"I":
            a=a+"i"
            z=z+1
    
    
        if "201112" in i or string in "J":
            a=a+"j"
            z=z+1

        if "21012" in i or string in "K":
            a=a+"k"
            z=z+1
    
        if "201002" in i or string in"L":
            a=a+"l"
            z=z+1
    
    
        if "2112" in i or string in "M":
            a=a+"m"
            z=z+1

        if "2102" in i or string in "N":
            a=a+"n"
            z=z+1
    
        if "21112" in i or string in"ö":
            a=a+"o"
            z=z+1
    
    
        if "201102" in i or string in "P":
            a=a+"p"
            z=z+1

        if "20102" in i or string in "R":
            a=a+"r"
            z=z+1
    
        if "20002" in i or string in"ş":
            a=a+"s"
            z=z+1
    
    
        if "212" in i or string in "T":
            a=a+"t"
            z=z+1

        if "20012" in i or string in "ü":
            a=a+"u"
            z=z+1
    
        if "200012" in i or string in"V":
            a=a+"v"
            z=z+1
    
    
        if "210112" in i or string in "Y":
            a=a+"y"
            z=z+1

        if "211002" in i or string in "Z":
            a=a+"z"
            z=z+1
    
        
        if "2010102" in i or string in ".":
            a=a+"."
            z=z+1

        if "210012" in i or string in "X":
            a=a+"x"
            z=z+1
    
        if "20112" in i or string in"W":
            a=a+"w"
            z=z+1
        if "20000002" in i or string in"":
            a=a+" "
            z=z+1
        if "2011112" in i :
            a=a+"1"
            z=z+1
        if "2001112" in i :
            a=a+"2"
            z=z+1
        if "2000112" in i :
            a=a+"3"
            z=z+1
        if "2000012" in i :
            a=a+"4"
            z=z+1
        if "2000002" in i :
            a=a+"5"
            z=z+1
        if "2100002" in i :
            a=a+"6"
            z=z+1
        if "2110002" in i :
            a=a+"7"
            z=z+1
        if "2111002" in i :
            a=a+"8"
            z=z+1
        if "2111102" in i :
            a=a+"9"
            z=z+1
        if "2111112" in i :
            a=a+"0"
            z=z+1
            
        #print (a)



    return a
while 1:
    metin=input("  ")
    metin.upper()
    metin2=cozme(metin)
    print(metin2)
    time.sleep(0.1)
