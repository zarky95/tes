from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/dashboard')
def dashboard():
    data = pd.read_csv('sales.csv')
    summary = data.groupby('product').sum()
    return render_template('dashboard.html', tables=[summary.to_html()])