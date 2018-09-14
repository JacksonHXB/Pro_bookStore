from flask import flash, redirect, url_for
from flask.globals import current_app
from flask.templating import render_template
from flask_login import login_required, current_user

from app.models.base import db
from app.models.gift import Gift
from app.view_models.gift import MyGifts
from app.view_models.trade import MyTrades

from . import web


@web.route('/my/gifts')
@login_required         # 使用这个装饰器，用户必须登录之后才能访问
def my_gifts():
    '''
        思路：
                循环遍历我的礼物
                取出每个礼物的ISBN编号，组成一个列表
                使用in查询去Wish表中查询在isbn列表中的心愿，并计算数量
    '''
    # 获取当前用户的ID
    uid = current_user.id
    gifts_of_mine = Gift.get_user_gifts(uid)
    isbn_list = [gift.isbn for gift in gifts_of_mine]
    wish_count_list = Gift.get_wish_counts(isbn_list)
    view_model = MyTrades(gifts_of_mine, wish_count_list)
    return render_template('my_gifts.html',gifts=view_model.trades)



# 赠送此书，将该书本放入到礼物中
@web.route('/gifts/book/<isbn>')  
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):   # 这里是判断是否是在用户的清单中
        # 如果存储出错，实行事务回滚
#         try:
#             gift = Gift()
#             gift.isbn = isbn
#             gift.uid = current_user.id  # 获取当前用户的ID，该用户存储在LoginManger中
#             current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK'] # 增加鱼豆的数量
#             db.session.add(gift)
#             db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             raise e

        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id  # 获取当前用户的ID，该用户存储在LoginManger中
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK'] # 增加鱼豆的数量
            db.session.add(gift)
    else:
        print('这本书已经添加到你要赠送的清单或已经存在于你的心愿清单，请不要重复添加！')
        flash('这本书已经添加到你要赠送的清单或已经存在于你的心愿清单，请不要重复添加！')
    # 赠送成功后跳转到原书本详情页面
    return redirect(url_for('web.book_detail', isbn=isbn))
        


# 解决循环导入问题

















































