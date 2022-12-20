from flask import Flask, render_template, json, request

app = Flask(__name__)


@app.route('/post')
def CC_page():
    return render_template("createpost.html")
  
@app.route('/')
def index_page():
  return render_template("celotajs.html")


app.run(host='0.0.0.0', port=81)
