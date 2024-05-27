import numpy as np
import random
import os
import sys
sys.path.append(r"D:\Project\PythonPractice\Dating")
from personal.ListPsn import Personality
dir = os.path.dirname(__file__)

dt_boyName = os.path.join(dir,"name/Boy.txt")
dt_girlName = os.path.join(dir,"name/Girl.txt")
dt_surName = os.path.join(dir,"name/Sur.txt")
dt_address = os.path.join(dir,"address/Address.txt")

def newUser(boyf,girlf,surf,addf):
    #personDt = [name,gender,age,address,psnl[4x4]]
    with open("./data/Users.txt","a",encoding="utf-8") as f:
        sur = random.choice(surf.readlines()).strip()
        gender = random.choice(["boy","girl"])
        age = random.randrange(18,25)
        address = random.choice(addf.readlines()).strip()
        personal = np.reshape(random.choice(np.array(Personality)),(-1))
        if(gender=="boy"): name = random.choice(boyf.readlines()).strip()
        else: name = random.choice(girlf.readlines()).strip()
        f.write(f"{sur} {name},{gender},{age},{address},{personal}\n")

def main():
    f_bN = open(dt_boyName, encoding="utf-8")
    f_gN = open(dt_girlName, encoding="utf-8")
    f_surN = open(dt_surName, encoding="utf-8")
    f_addr = open(dt_address, encoding="utf-8")
    newUser(f_bN,f_gN,f_surN,f_addr)
    f_bN.close()
    f_gN.close()
    f_surN.close()

for i in range(100):
    main()