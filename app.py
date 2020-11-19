from flask import Flask, render_template

app = Flask(__name__) # creates Flask object from main fcn

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__': #runs Flask app
    app.run()
