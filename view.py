from app import app
from flask import render_template


@app.route('/') #/ - корень сайта (обращение к 127.0.0.1:5000) - # {'/': 'veiw.index', '/blog': 'view.index'}
def index():
	name = 'Ivan'
	return render_template('index.html', n=name)


