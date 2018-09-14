#===============================================================================
# 图书视图函数
#===============================================================================
import json

from flask import jsonify, request, render_template,flash
from app.forms.book import SearchForm  # 导入验证模块
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookViewModel, BookCollection
from app.models.gift import Gift
from app.models.wish import Wish

from . import web  # 导入蓝本模块

# 测试
@web.route('/test')
def test():
    r = {
        'name': '黄小兵',
        'age': 23
    }
    flash('消息闪现1!')
    flash('消息闪现2!')
    flash('消息闪现3!')
    return render_template('test2.html', data=r)


# 搜索图书，q表示普通关键字；page表示分页
@web.route('/book/search')# http://localhost:5001/book/search?q=2342434&page=1
def search():
    print(request.args)# 获取参数值
    
    # 验证传递过来的参数
    form = SearchForm(request.args)
    books = BookCollection()
    if form.validate():
        print('search()参数验证通过！')
        # 获取验证通过后的值,从验证器中取值
        q = form.q.data.strip()
        page = form.page.data
        
        # 获取关键字的类型
        isbn_or_key = is_isbn_or_key(q)
        
        yushu_book = YuShuBook()
        # 通过关键字获取图书
        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        elif isbn_or_key == 'key':
            yushu_book.search_by_keyword(q, page)
            
        books.fill(yushu_book, q)
        # Flask提供的返回JSON的做法，return json.dumps(result),200,{'content-type':'application/json'}原生返回JSON数据的做法
#         return jsonify(books.__dict__)# python不能直接序列化对象books
#         return json.dumps(books, default=lambda o:o.__dict__)   # 通过匿名函数将不能序列化的对象序列化
    else:
        flash('search()验证失败！')
    json.dumps(books, default=lambda o:o.__dict__)
    return render_template('search_result.html', books=books)


# 书籍详情页
@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    # 定义两个变量，默认是不再gifts和wishes里面
    has_in_gifts = False
    has_in_wishes = False
    
    # 获取书籍的详情数据
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)
    
    
    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()
    
    return render_template('book_detail.html',book=book,wishes=[],gifts=[])









































































