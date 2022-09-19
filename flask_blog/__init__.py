from flask import Flask

app = Flask(__name__)
#設定 [flask_blog]フォルダ以下にあるconfig.pyの内容をconfigとして読み込みます。
app.config.from_object('flask_blog.config')

from flask_blog.views import entries