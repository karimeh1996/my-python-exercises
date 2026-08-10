
mablag =int(input("mablag ra vared conid")) 
if (mablag) > 50000 :
    takhfif= (mablag*80)/100
    print (f"20% takhfif amal shod:{takhfif}")
elif 20000 < mablag < 50000:
    takhfif= (mablag*90)/100
    print (f"10% takhfif amal shavad:{takhfif}")
elif mablag < 20000:  
    print ("takhfif amal nemeshavad")


