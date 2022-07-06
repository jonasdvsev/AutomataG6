from flask import Flask, render_template,request
from regex1stringchecker import Regex1checkString
from regex2stringchecker import Regex2checkString
app = Flask(__name__)


@app.route('/',methods=["GET","POST"])
def index():
    return render_template("index.html",Statess=["0"],Traced=False,regexinputinfo="regex")



@app.route('/regex/<regexinputinfo>',methods=["GET","POST"])
def regexoutput(regexinputinfo):
    if request.method == "POST":
        Traced = True
        regexinputinfo=regexinputinfo;
        return render_template("index.html",Statess=["0"], Traced=Traced, regexinputinfo=regexinputinfo)
    return render_template("index.html")

@app.route('/traceoutput',methods=["GET","POST"])
def traceoutput():
    if request.method == "POST":
        convinput1 = request.form.get("StringInputRegex1")
        convinput2 = request.form.get("StringInputRegex2")

        if convinput1 != "r1":
            States = Regex1checkString(convinput1)
            traced = True
            regexinput = "regex1"
            print(States)

        elif convinput2 != "r2":
            States = Regex2checkString(convinput2)
            traced = True
            regexinput = "regex2"



    return render_template("outputfile.html", Statess=States, Traced=traced, regexinputinfo=regexinput)




if __name__ == "__main__":
    app.run(debug=True)

