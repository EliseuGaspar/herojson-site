from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/documentação')
def docs():
	return render_template('documentacao.html')

@app.route('/contribuição')
def contributions():
	return render_template('contributions.html')