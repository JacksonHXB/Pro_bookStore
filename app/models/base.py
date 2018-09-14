#===============================================================================
# 初始化SQLalchemy
#===============================================================================

from contextlib import contextmanager
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from sqlalchemy import Column, SmallInteger, Integer


# 继承SQLAlchemy对所有的事务提交都执行事务回滚
class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

db = SQLAlchemy()       # 实例化对象


# 基本模型类
class Base(db.Model):
    __abstract__ = True                             # 将该类设置抽象类，这样Flask将不会去创建表
    create_time = Column('create_time', Integer)    # 模型创建时间，不能使用default，因为这是类变量，在类初始化时就会赋值，所以这里不能用default
    status = Column(SmallInteger, default=1)        # 用来表示数据是否被删除

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    # 遍历属性并赋值
    def set_attr(self,attrs_dict):
        for key,value in attrs_dict.items():
            # 判断属性名是否一样的
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)


    # 对时间进行转换的操作
    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None
        








































































