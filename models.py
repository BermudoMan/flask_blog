from app import db
from datetime import datetime
import re
from slugify import slugify


# s - заголовок поста - строка (pythex.org)
# выделение ненужных символов и их замена на '-'

#def slugify(s):
	# pattern = r'[^\w+]'
	# return re.sub(pattern, '-', s)
	

class Post(db.Model):
	# свойства
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(140))
	slug = db.Column(db.String(140), unique=True)
	body = db.Column(db.Text)
	created = db.Column(db.DateTime, default=datetime.now())


	# конструктор
	def __init__(self, *args, **kwargs):
		# конструктор класса предка
		super(Post, self).__init__(*args, **kwargs)
		self.generate_slug()


	def generate_slug(self):
		# url генерируется из текста заголовка - 'slugify'
		if self.title:
			self.slug = slugify(self.title)


	def __repr__(self):
		return '<Post id: {}, title: {}>'.format(self.id, self.title)