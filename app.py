from flask import Flask, render_template
app = Flask(__name__)


#assign following fxn to run when root route requested
@app.route("/")
def hello_world():
    retStr = "No hablo queso!"
    return retStr

@app.route("/occupations")
def title():
    retstr = "<h1>Ocupations in the United States</h1><br>This table shows percentages for different occupations among U.S. citizens."
    return retstr

if __name__ == "__main__":
    app.debug = True
    app.run()
