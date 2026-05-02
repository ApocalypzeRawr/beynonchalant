from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    data_diri = {
        "nama_lengkap": "Bayu Setyawan",
        "npm": "50425194",
        "jabatan": "Backend Developer | Hardware Integrator",
        "deskripsi": "I am a dedicated Informatics student specialized in building robust backend systems with Python and Flask. My goal is to bridge the gap between complex hardware solutions and seamless user experiences.",
        "lokasi": "Indonesia"
    }
    return render_template('index.html', data=data_diri)

if __name__ == '__main__':
    app.run(debug=True)