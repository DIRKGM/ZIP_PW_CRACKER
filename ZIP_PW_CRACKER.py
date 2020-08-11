##############################################################################
#                                                                            #                           
#                          ZIP Password Cracker                              #
#                                                                            #
#                                                                            #
##############################################################################
import zipfile
import itertools
import sting
from threading import Thread
import traceback

def crack(zip, pwd):
    try:
        zip.extractall(pwd=str.encode(pwd))
        print('Sucesess: Paswword is:' + pwd)
    except:
        pass
        
zipfile=zipfile.ZipFile("ZipFile Path") <--Zipfile Pfad eintragen-->
myletters = string.ascii_letters + string.digits + string.punctuation <-- Buchstaben, Zahlen, Sonderzeichen-->
for i in range (1,10) <--Password Länge-->
    for j in map(''.join, itertolls.product(myletters, repeat=i)):
        t=Thread(target=crack, args=(zipfile, j))
        t.start()