from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    # Simulasikan respons server yang berisi flag
    flag = "TI404{4lh4mdu1i114h_k3t3mu}"
    return render_template_string("""
    <!doctype html>
    <html lang="id">
    <head>
        <meta charset="utf-8">
        <title>Web What's a Netcat</title>
    </head>
    <body>
        <h1>What's a Netcat</h1>
        <p>Temukan Flag!!!:</p>
        <p>Terhubung ke jupiter.challenges.picoctf.org di port 64287 untuk mendapatkan flag:</p>
        <pre>{{ flag }}</pre>
    </body>
    </html>
    """, flag=flag)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)