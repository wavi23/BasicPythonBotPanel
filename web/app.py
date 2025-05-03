from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

# Load configuration from config.py
app.config.from_pyfile('config.py')
title = app.config['TITLE']
nav_logo = app.config['NAV_LOGO']
nav_title = app.config['NAV_TITLE']
nav_discord_url = app.config['NAV_DISCORD_URL']

@app.route('/')
def index():
	return render_template('index.html', title=title, nav_logo=nav_logo, nav_title=nav_title, nav_discord_url=nav_discord_url)

if __name__ == "__main__":
    app.run(debug=True)