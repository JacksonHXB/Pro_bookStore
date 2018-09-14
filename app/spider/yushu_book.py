#===============================================================================
# 鱼书
#===============================================================================
from app.libs.httpRequest import Http_request

from flask import current_app   # 导入当前的app核心对象

class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'
    
    def __init__(self):
        self.total = 0
        self.books = []
    
    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)
    
    def __fill_collection(self, data):
        self.total = data['total']
        self.books = data['books']
    
    # 通过ISBN码进行查询
    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        result = Http_request.get(url)
        self.__fill_single(result)
    
    # 通过关键字查询
    def search_by_keyword(self, keyword, page=1):
        url = self.keyword_url.format(keyword, current_app.config['PER_PAGE'], self.calculate_start(page))
        result = Http_request().get(url)
        self.__fill_collection(result)
    
    # 计算起始页码
    def calculate_start(self, page):
        return (page-1)*current_app.config['PER_PAGE']

    # 返回结果中的第一个值
    @property
    def first(self):
        return self.books[0] if self.total>=1 else None





























