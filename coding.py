import time
# nokta 0
#cizgi 1
def yaz(s):
    print(s)
alfabe="abcdefghıijklmnoöprsştuüvyzABCDEFGHIİJKLMNOÖPRSŞTUÜVYZ"
def tanımlama(metin):
    metin.lower()
    y=0
    
    for i in metin:
        y=y+1
    print(len(metin))
    print(metin)
    dizi2=metin.split(" ")
    dizi=[]
    #dizi=[len(metin)]
    z=0
    for string in metin:
        string.lower()
        

    
        a=" "
        if string in "a" or string in "A":
            dizi.append("2012")
            z=z+1

        if string in "b" or string in "B":
            dizi.append("210002")
            z=z+1
    
        if string in "c" or string in"ç" or string in "Ç" or string in "C":
            dizi.append("210102")
            z=z+1
    
    
        if string in "d" or string in "D":
            dizi.append("21002")
            z=z+1

        if string in "e" or string in "E":
            dizi.append("202")
            z=z+1
    
        if string in "f" or string in "F":
            dizi.append("200102")
            z=z+1
    
    
        if string in "g" or string in "G":
            dizi.append("21102")
            z=z+1

        if string in "h" or string in "H":
            dizi.append("200002")
            z=z+1
    
        if string in "i" or string in"ı" or string in "İ" or string in"I":
            dizi.append("2002")
            z=z+1
    
    
        if string in "j" or string in "J":
            dizi.append("201112")
            z=z+1

        if string in "k" or string in "K":
            dizi.append("21012")
            z=z+1
    
        if string in "l" or string in"L":
            dizi.append("201002")
            z=z+1
    
    
        if string in "m" or string in "M":
            dizi.append("2112")
            z=z+1

        if string in "n" or string in "N":
            dizi.append("2102")
            z=z+1
    
        if string in "o" or string in"ö" or string in "O" or string in"Ö":
            dizi.append("21112")
            z=z+1
    
    
        if string in "p" or string in "P":
            dizi.append("201102")
            z=z+1

        if string in "r" or string in "R":
            dizi.append("20102")
            z=z+1
    
        if string in "s" or string in"ş" or string in "S" or string in"Ş":
            dizi.append("20002")
            z=z+1
    
    
        if string in "t" or string in "T":
            dizi.append("212")
            z=z+1

        if string in "u" or string in "ü" or string in "U" or string in "Ü":
            dizi.append("20012")
            z=z+1
    
        if string in "v" or string in"V":
            dizi.append("20001")
            z=z+1
    
    
        if string in "y" or string in "Y":
            dizi.append("210112")
            z=z+1

        if string in "z" or string in "Z":
            dizi.append("211002")
            z=z+1
    
        
        if string in "." or string in ".":
            dizi.append("2010102")
            z=z+1

        if string in "x" or string in "X":
            dizi.append("210012")
            z=z+1
    
        if string in "w" or string in"W":
            dizi.append("20112")
            z=z+1
        if string in "" or string in" ":
            dizi.append("20000002")
            z=z+1
        if string in "1" or string in"1":
            dizi.append("2011112")
            z=z+1
        if string in "2" or string in"2":
            dizi.append("2001112")
            z=z+1
        if string in "3" or string in"3":
            dizi.append("2000112")
            z=z+1
        if string in "4" or string in"4":
            dizi.append("2000012")
            z=z+1
        if string in "5" or string in"5":
            dizi.append("2000002")
            z=z+1
        if string in "6" or string in"6":
            dizi.append("2100002")
            z=z+1
        if string in "7" or string in"7":
            dizi.append("2110002")
            z=z+1
        if string in "8" or string in"8":
            dizi.append("2111002")
            z=z+1
        if string in "9" or string in"9":
            dizi.append("2111102")
            z=z+1
        if string in "0" or string in"0":
            dizi.append("2111112")
            z=z+1
            
    print(dizi)
    
    for i in range(len(dizi)):
        if dizi[i] in alfabe:
            dizi[i]=kıyas(dizi[i])
    
        
    
    
    
    return dizi

def kıyas(metin):
    z=0
    B=" "
    dizi=[]
    for string in metin:
        string.lower()
        

        
        a=" "
        if string in "a" or string in "A":
            B+="2012"
            z=z+1

        if string in "b" or string in "B":
            B+="210002"
            z=z+1
    
        if string in "c" or string in"ç":
            B+="210102"
            z=z+1
    
    
        if string in "d" or string in "D":
            B+="21002"
            z=z+1

        if string in "e" or string in "E":
            B+="202"
            z=z+1
    
        if string in "f" or string in "F":
            B+="200102"
            z=z+1
    
    
        if string in "g" or string in "G":
            B+="21102"
            z=z+1

        if string in "h" or string in "H":
            B+="200002"
            z=z+1
    
        if string in "i" or string in"ı":
            B+="2002"
            z=z+1
    
    
        if string in "j" or string in "J":
            B+="201112"
            z=z+1

        if string in "k" or string in "K":
            B+="21012"
            z=z+1
    
        if string in "l" or string in "L":
            B+="201002"
            z=z+1
    
    
        if string in "m" or string in "M":
            B+="2112"
            z=z+1

        if string in "n" or string in "N":
            B+="2102"
            z=z+1
    
        if string in "o" or string in"ö":
            B+="21112"
            z=z+1
    
    
        if string in "p" or string in "P":
            B+="201102"
            z=z+1

        if string in "r" or string in "R":
            B+="20102"
            z=z+1
    
        if string in "s" or string in"ş":
            B+="20002"
            z=z+1
    
    
        if string in "t" or string in "T":
            B+="212"
            z=z+1

        if string in "u" or string in "ü":
            B+="20012"
            z=z+1
    
        if string in "v" or string in"V":
            dB+="20001"
            z=z+1
    
    
        if string in "y" or string in "Y":
            B+="210112"
            z=z+1

        if string in "z" or string in "Z":
            B+="211002"
            z=z+1
    
        
        if string in "." or string in ".":
            B+="2010102"
            z=z+1

        if string in "x" or string in "X":
            B+="210012"
            z=z+1
    
        if string in "w" or string in"W":
            B+="20112"
            z=z+1
        #for j in range(len(sifre)):
            #a=a+str(dizi[j])+" " 
    return B
    
sifree=" "
y=0
b=" "
while 1:
    metin=input("yazı")
    for i in metin:
        sifree=sifree+i 
   
        
    sifre=tanımlama(sifree)
    sifree=" "
    #print (metin)
    metin=" "
    print(sifre)
    mesaj=str(sifre)
    #yeni=.join(sifre)
    #print(type(mesaj))
    #print(mesaj)
    mesaj.replace("["," ")
    mesaj.replace("]"," ")
    #print(mesaj)
    #sifre.remove(' ')
    for j in range(len(sifre)):
        
        if sifre[j]==' ' or sifre[j]=='':
            sifre.pop(j)
        else:
            b=b+str(sifre[j])+" "
        

    print(b)
    b=" "
    time.sleep(0.1)
        
    

    


        
        
