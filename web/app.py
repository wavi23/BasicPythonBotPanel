from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

# Load configuration from config.py
app.config.from_pyfile('config.py')
title = app.config['TITLE']

@app.route('/')
def index():
	return render_template('index.html', title=title)

if __name__ == "__main__":
    app.run(debug=True)