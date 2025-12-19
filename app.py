from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    simdi = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', zaman=simdi)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
