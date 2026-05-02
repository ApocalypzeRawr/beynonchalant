from flask import Flask, render_template
import os

app = Flask(__name__, 
            template_folder='../templates', 
            static_folder='../static')

@app.route('/')
def home():
    data_diri = {
        "nama_lengkap": "Bayu Setyawan",
        "npm": "50425194",
        "deskripsi": "I am an enthusiastic Information Technology student, passionate about building robust systems with Java and Python. I thrive on solving complex computational problems and am dedicated to creating efficient software solutions."
    }
    return render_template('index.html', data=data_diri)