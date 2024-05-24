from flask import Flask, render_template, request
from dati import dabut_rindas, pierakstit_klat

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/teksts")
def teksts():
    return render_template("teksts.html")

@app.route("/saraksts")
def saraksts():
    saraksts = ["Ligma", "Joe", "Georgs"]
    bildes = ["https://pbs.twimg.com/media/Dibvn16VQAAnzRx.jpg", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQx7Z6wLxWZIosq06EIboRWg_04CgcZbmlvU2aY7Ia2SQ&s", "https://s.abcnews.com/images/US/george-floyd-ap-jt-200529_hpMain_2_16x9_992.jpg"]
    kopejais_saraksts = [["Ligma", "https://pbs.twimg.com/media/Dibvn16VQAAnzRx.jpg"],["Joe", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQx7Z6wLxWZIosq06EIboRWg_04CgcZbmlvU2aY7Ia2SQ&s"], ["Georgs", "https://s.abcnews.com/images/US/george-floyd-ap-jt-200529_hpMain_2_16x9_992.jpg"]]
    faila_rindas = dabut_rindas()
    for rinda in faila_rindas:
        elements = rinda.split(", ")
        kopejais_saraksts.append(elements)
   
    return render_template("saraksts.html", vardi = saraksts, bildes = bildes, garums=len(saraksts), visi=kopejais_saraksts)

@app.route("/info", methods=['POST', 'GET'])
def info():
    if request.method == "POST":
        rinda =""
        nosaukums = request.form["nosaukums"]
        adrese = request.form["adrese"]
        rinda = nosaukums + ", " + adrese
        print(nosaukums)
        pierakstit_klat(rinda)
    return render_template("info.html")





if __name__ == '__main__':
    app.run(port = 5000)

print("Sveiki")