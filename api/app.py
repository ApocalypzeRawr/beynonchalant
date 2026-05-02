from flask import Flask, render_template
import os

# Mengarahkan Flask agar bisa membaca folder templates dan static di luar folder api
app = Flask(__name__, 
            template_folder='../templates', 
            static_folder='../static')

@app.route('/')
def home():
    # Data diri untuk mahasiswa Informatika
    data_diri = {
        "nama_lengkap": "Bayu Setyawan",
        "npm": "50425194",
        "deskripsi": "I am an enthusiastic Information Technology student, passionate about building robust systems with Java and Python."
    }
    return render_template('index.html', data=data_diri)