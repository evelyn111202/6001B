from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return(render_template("index.html"))

@app.route("/prediction",methods=["GET","POST"])
def prediction():
    q = float(request.form.get("q"))
    model = joblib.load('dbs.jl')
    pred = model.predict([[q]])
    r = pred[0][0]
    return(render_template("prediction.html", r=r))

if __name__=="__main__":
    app.run()