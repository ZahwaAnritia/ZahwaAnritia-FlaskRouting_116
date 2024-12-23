from flask import Flask, redirect, url_for, request, render_template

#Membuat aplikasi flask
app = Flask(__name__)

#Halaman utama
@app.route('/') 
def home():
    return render_template('index.html')  # Menampilkan file HTML bernama 'index.html' 

@app.route('/success/<name>')  #halaman sukses dengan parameter 'name'
def success(name):
    return f'Welcome {name}!'  # Menampilkan pesan selamat datang dengan nama yang dikirim

@app.route('/login', methods=['POST', 'GET']) # Halaman login, menerima metode POST dan GET
def login():
    if request.method == 'POST': # Jika pengguna mengirim data lewat formulir (POST)
        user = request.form['nm']  # Ambil data nama dari input 'nm' di formulir
        return redirect(url_for('success', name=user)) # Arahkan ke halaman sukses dengan nama
    else: # Jika akses dengan metode GET (tanpa kirim formulir)
        return redirect(url_for('home'))  # Arahkan kembali ke halaman utama
if __name__ == '__main__':
    app.run(debug=True)  # Jalankan aplikasi dengan mode debug aktif