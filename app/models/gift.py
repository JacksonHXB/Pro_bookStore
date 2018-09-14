#===============================================================================
# Gift模型
#===============================================================================
from flask.globals import current_app
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, desc, func
from sqlalchemy.orm import relationship

from app.models.base import Base,db
from app.spider.yushu_book import YuShuBook
from app.models.wish import Wish
from collections import namedtuple

# 快速生成一个对象
EachGiftWishCount = namedtuple('EachGiftWishCount', ['count', 'isbn'])  # 参数一为对象名，参数二为属性列表

class Gift(Base):
    __tablename__ = 'tb_gift'
    id = Column(Integer, primary_key=True)
    tb_user = relationship('User') # 引用User模型 
    uid = Column(Integer, ForeignKey('tb_user.id')) # 用户ID（外键）
#     # 因为数据是直接从API中获取的，所以这里的关联不一样
#     book1 = relationship('Book')
#     bid = Column(Integer, ForeignKey('book1.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False) # 礼物是否被送出，False表示礼物默认没有被送出去
    
    # 获取用户的所有礼物
    @classmethod
    def get_user_gifts(cls, uid):
        gifts = Gift.query.filter_by(uid=uid, launched=False).order_by(desc(Gift.create_time)).all()
        return gifts
    
    # 获取最近的礼物
    @classmethod
    def recent(cls):
        recent_gift = Gift.query.filter_by(
            launched=False
        ).group_by(
            Gift.isbn
        ).order_by(
            desc(Gift.create_time)
        ).limit(
            current_app.config['RECENT_BOOK_COUNT']
        ).distinct().all()
        return recent_gift
    
    # 通过ISBN码获取图书
    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first
    
    # 获取心愿的礼物总数
    @classmethod
    def get_wish_counts(cls, isbn_list):
        # 根据传入的一组ISBN，到wish表中计算出某个礼物的wish心愿数量
        count_list = db.session.query(
            func.count(Wish.id),
            Wish.isbn
        ).filter(
            Wish.launched==False, 
            Wish.isbn.in_(isbn_list),
            Wish.status==1
        ).group_by(
            Wish.isbn
        ).all()# 跟上面的查询大同小异
#     # 返回对象
#     count_list = [EachGiftWishCount(w[0],w[1]) for w in count_list]
    # 字典
    count_list = [{'count':w[0],'isbn':w[1]} for w in count_list]
    return count_list















































