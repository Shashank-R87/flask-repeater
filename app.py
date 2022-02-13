from flask import Flask
from flask import request,render_template

app = Flask(__name__)

@app.route('/',methods =["GET","POST"])
def handle_request():
    text = str(request.args.get("input"))
    return render_template("index.html",data = text)
