from app.models.gift import Gift
from app.view_models.book import BookViewModel
from . import web
from flask import render_template


# # 最近上传书籍
# @web.route('/')
# def index():
#     recent_gifts = Gift.recent()
#     books = [BookViewModel(gift.book) for gift in recent_gifts]
#     return render_template('upLately.html', books=books)
















































