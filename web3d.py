from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Konfigurasi direktori penyimpanan gambar
UPLOAD_FOLDER = os.path.join('static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    # Menampilkan halaman utama viewer 360
    return render_template('index.html')

if __name__ == '__main__':
    # Menjalankan server Flask secara lokal pada port 5000
    app.run(debug=True, host='0.0.0.0', port=5000)