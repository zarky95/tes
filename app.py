from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.secret_key = 'kunci_rahasia_anda'  # Ganti dengan kunci unik

# Dummy data untuk proyek
projects = [
    {
        "title": "Aplikasi Web E-commerce",
        "description": "Aplikasi toko online dengan Flask dan MySQL.",
        "image": "https://live.staticflickr.com/2774/4399421398_87191e276a_b.jpg"
    },
     {
        "title": "Aplikasi Ngarang",
        "description": "Ngarang bos.",
        "image": "https://live.staticflickr.com/2774/4399421398_87191e276a_b.jpg"
    },
    {
        "title": "Sistem Analisis Data",
        "description": "Analisis data menggunakan Python Pandas.",
        "image": "https://live.staticflickr.com/2450/5858018040_07813b7134_b.jpg"
    }
]

# Form Kontak
class ContactForm(FlaskForm):
    name = StringField('Nama', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Pesan', validators=[DataRequired()])
    submit = SubmitField('Kirim')

# Halaman Home
@app.route('/')
def home():
    return render_template('index.html', projects=projects[:1])

# Halaman Projects
@app.route('/projects')
def all_projects():
    return render_template('projects.html', projects=projects)
# Halaman Kontak
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Simpan pesan ke database atau kirim email (opsional)
        return "Pesan terkirim! Terima kasih."
    return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)