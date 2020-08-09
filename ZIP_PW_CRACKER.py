##############################################################################
#                                                                            #
#                           By Dirk GM                              #
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
        print('Sucesess: Paswword is' + pwd)
    except:
        if pwd == "abc":
            traceback.print_exc()

zipfile=zipfile.ZipFile("/Users/DirkG/Desktop/123.zip") --> Zipfile Path
myletters = string.ascii_letters + string.digits + string.punctuation
for i in range (3,10)
    for j in map(''.join, itertolls.product(AB´, repeat=3)):
        t=Thread(target=crack, args=(zipfile, j))
        t.start()