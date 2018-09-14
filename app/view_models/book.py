#===============================================================================
# view_model：对视图函数返回的结果进行处理
#===============================================================================

class BookViewModel:
    def __init__(self, book):
        self.isbn = book['isbn']
        self.title = book['title']
        self.publisher = book['publisher']
        self.pages = book['pages']
        self.author = ','.join(book['author'])
        self.price = book['price']
        self.summary = book['summary']
        self.image = book['image']
        
    # 书本介绍，通过"/"连接各个字段,@property将函数视作属性进行调用
    @property
    def introduce(self):
        introduces = filter(lambda x: True if x else False,[self.author,self.publisher,self.price])
        return '/'.join(introduces)
    
        
class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''
    
    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]


# 旧的类
class BookViewModel2:
    # 描述特征（类变量，实例变量）
    # 描述行为（方法）
    @classmethod
    def package_single(cls,data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = 1
            returned['books'] = cls.__cut_book_data(data)
        return returned
    
    
    @classmethod
    def package_collection(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = len(data['books'])
            returned['books'] = [cls.__cut_book_data(book) for book in data['books']]# 遍历所有数据并对所有数据进行处理后加入到books中
        return returned


    # 裁剪数据
    @classmethod
    def __cut_book_data(cls, data):
        book = {
                'title': data['title'],
                'publisher': data['publisher'],
                'pages': data['pages'],
                'author': ','.join(data['author']),# 使用逗号连接每一个作者
                'price': data['price'],
                'summary': data['summary'],
                'image': data['image']
            }
        return book























































































