import numpy as np
import random
import os
import glob as gl
import io
dir = os.path.dirname(__file__)
dt_boyName = os.path.join(dir,"name/Boy.txt")
dt_girlName = os.path.join(dir,"name/Girl.txt")
dt_surName = os.path.join(dir,"name/Sur.txt")

def newUser(boyf,girlf,surf):
    gender = random.choice(["boy","girl"])
    sur = random.choice(surf.readlines()).strip()
    with open("User.txt","a") as f:
        f.write(f"{sur},{gender}")

def main():
    f_bN = open(dt_boyName, encoding="utf-8")
    f_gN = open(dt_girlName, encoding="utf-8")
    f_surN = open(dt_surName, encoding="utf-8")

    newUser(f_bN,f_gN,f_surN)

    f_bN.close()
    f_gN.close()
    f_surN.close()



main()