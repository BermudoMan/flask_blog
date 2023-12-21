from flask import Blueprint
from flask import render_template

posts = Blueprint('posts', __name__, template_folder='templates') # posts - название блюпринта, первый аргумент передается в base.html для создания ссылки

@posts.route('/')
def index(): # название передается в url_for в базовом шаблоне
	return render_template('posts/index.html')