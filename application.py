from flask import Flask, render_template

#init
application = Flask(__name__)

@application.route('/')
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    application.debug = True
    application.run()
