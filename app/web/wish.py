from flask.globals import current_app
from flask_login import login_required, current_user

from flask import flash,redirect,url_for,render_template
from app.models.base import db
from . import web
from app.view_models.trade import MyTrades


# 加入心愿清单中
@web.route('/wish/book/<isbn>')  
@login_required
def save_to_wish(isbn):
    if current_user.can_save_to_list(isbn):   
        with db.auto_commit():
            wish = Wish()
            wish.uid = current_user.id
            wish.isbn = isbn
            db.session.add(wish)
    else:
        print('这本书已经添加到你要赠送的清单或已经存在于你的心愿清单，请不要重复添加！')
        flash('这本书已经添加到你要赠送的清单或已经存在于你的心愿清单，请不要重复添加！')
    return redirect(url_for('web.book_detail', isbn=isbn))
        

@web.route('/my/wish')
def my_wish():
    uid = current_user.id
    wishes_of_mine = Wish.get_user_wishes(uid)
    isbn_list = [wish.isbn for wish in wishes_of_mine]
    gift_count_list = Wish.get_gifts_count(isbn_list)
    view_model = MyTrades(wishes_of_mine, gift_count_list)
    return render_template('my_wishes.html',wishes=view_model.trades)


# 解决循环导入问题
from app.models.wish import Wish















































