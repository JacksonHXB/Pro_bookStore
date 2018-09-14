#===============================================================================
# User模型
#===============================================================================
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Boolean, Float
from werkzeug.security import generate_password_hash, check_password_hash
from app.libs.helper import is_isbn_or_key
from app import login_manager
from app.spider.yushu_book import YuShuBook
from app.models.gift import Gift
from app.models.wish import Wish
from .base import Base
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from app.models.base import db

# 继承UserMixin来对接LoginManager，注意id这个不能变，如果变了需要重写UserMixin中的方法和属性
class User(Base, UserMixin):
    __tablename__ = 'tb_user'
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    email = Column(String(50), unique=True, nullable=True)       
    confirmed = Column(Boolean, default=False)    
    beans = Column(Float, default=0)   # 用户鱼豆
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))
    # 密码不能以明文存储
    _password = Column('password', String(128), nullable=False)

    # getter方法
    @property
    def password(self):
        return self._password
    
    # setter方法
    @password.setter
    def password(self, raw):
        # 对密码进行加密处理
        self._password = generate_password_hash(raw)
    
    # 明文密码与数据库的密文进行对比
    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    # 根据ISBN判断鱼书的书本是否存在
    def can_save_to_list(self, isbn):
        if is_isbn_or_key(isbn) != 'isbn':
            return False
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(isbn)
        if not yushu_book.first:
            return False
        gifting = Gift.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        wishing = Wish.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        # 图书既不再赠送清单中，也不在心愿清单中才能添加
        if not gifting and not wishing:
            return True
        else:
            return False
    
    # 生成token
    def generate_token(self, expiration=600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'id':self.id}).decode('UTF-8')
    
    # 更新用户密码
    @staticmethod
    def reset_password(token, new_password): 
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('UTF-8'))
        except:
            return False
        uid = data.get('id')
        with db.auto_commit():
            user = User.query.get(uid)
            user.password = new_password
        return True
        

# 通过用户ID返回用户模型，该函数是login_manager来进行管理
@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))  # 这里使用get方法，因为这里是主键
    









































