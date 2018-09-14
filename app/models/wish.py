#===============================================================================
# Wish模型
#===============================================================================
from sqlalchemy import Column,Integer,Boolean,ForeignKey,String,desc,func
from app.models.base import Base
from sqlalchemy.orm import relationship
from app.models.base import db
from app.models.gift import Gift
from app.spider.yushu_book import YuShuBook

class Wish(Base):
    __tablename__ = 'tb_wish'
    id = Column(Integer, primary_key=True)
    tb_user = relationship('User') # 引用User模型 
    uid = Column(Integer, ForeignKey('tb_user.id')) # 用户ID（外键）
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False) # 礼物是否被送出，False表示礼物默认没有被送出去
    
    # 获取用户的心愿清单
    @classmethod
    def get_user_wishes(cls, uid):
        wishes = Wish.query.filter_by(
            uid=uid,
            launched=False
        ).order_by(
            desc(Wish.create_time)
        ).all()
        return wishes
    
    @classmethod
    def get_gifts_count(cls, isbn_list):
        count_list = db.session.query(
            Gift.launched == False,
            Gift.isbn._in(isbn_list),
            Gift.status == 1
        ),group_by(
            Gift.isbn
        ).all()
    
    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first


















































