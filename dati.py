def ierakstit(teksts):
    fails = open("teksts.txt","w", encoding="utf-8") # r - read; w - write; a - append
    fails.write(teksts+"\n")
    fails.close()

ierakstit("Es esmu boss")

# ierakstit("Es esmu boss")
    
def pierakstit_klat(teksts):
    fails = open("teksts.txt", "a", encoding="utf-8")
    fails.write(teksts+"\n")
    fails.close()
    return

pierakstit_klat("Neesmu ligma")

def nolasit_visu():
    fails = open("teksts.txt", "r", encoding="utf-8")
    teksts = fails.read()
    return teksts

print(nolasit_visu())

def dabut_rindas():
    fails = open("teksts.txt", "r", encoding="utf-8")
    rindas = fails.readlines()

    for i in range(len(rindas)):
        rindas[i] = rindas[i].strip()
        
    return rindas
        


saraksts=(dabut_rindas())
print(saraksts)

ierakstit = ("Ligma", "https://pbs.twimg.com/media/Dibvn16VQAAnzRx.jpg")
pierakstit_klat = ("Joe", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQx7Z6wLxWZIosq06EIboRWg_04CgcZbmlvU2aY7Ia2SQ&s")
pierakstit_klat = ("Georgs", "https://s.abcnews.com/images/US/george-floyd-ap-jt-200529_hpMain_2_16x9_992.jpg")