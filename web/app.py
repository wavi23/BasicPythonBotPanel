from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

app.config.from_pyfile('config.py')
title = app.config['TITLE']
nav_logo = app.config['NAV_LOGO']
nav_title = app.config['NAV_TITLE']
nav_discord_url = app.config['NAV_DISCORD_URL']

card1_title = app.config['CARD1_TITLE']
card1_desc = app.config['CARD1_DESC']

card2_title = app.config['CARD2_TITLE']
card2_desc = app.config['CARD2_DESC']

card3_title = app.config['CARD3_TITLE']
card3_desc = app.config['CARD3_DESC']

card4_title = app.config['CARD4_TITLE']
card4_desc = app.config['CARD4_DESC']

@app.route('/')
def index():
	return render_template('index.html', title=title, nav_logo=nav_logo, nav_title=nav_title, nav_discord_url=nav_discord_url, card1_title=card1_title, card1_desc=card1_desc, card2_title=card2_title, card2_desc=card2_desc, card3_title=card3_title, card3_desc=card3_desc, card4_title=card4_title, card4_desc=card4_desc)

if __name__ == "__main__":
    app.run(debug=True)