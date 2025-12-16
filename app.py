from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
    <html>
        <head><title>Benim Bulut Uygulamam</title></head>
        <body style="font-family: Arial; text-align: center; padding: 50px;">
            <h1>Merhaba! AWS Bulut Uygulamam Çalışıyor! 🚀</h1>
            <p>Şu an saat: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            <p>Bu uygulama AWS EC2 üzerinde çalışıyor.</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
