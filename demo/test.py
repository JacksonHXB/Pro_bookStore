#===============================================================================
# 上下文
#===============================================================================
from flask import Flask,current_app

app = Flask(__name__)

# 应用上下文  对象 Flask
# 请求上下文  对象 Request
# Flask核心对象存储在AppContext中
# Request核心对象存储在RequestContext中
ctx = app.app_context()
ctx.push()                  # 入栈
a = current_app
b = current_app.config['DEBUG']


# 实现了上下文协议的对象使用with，也通常被称为上下文管理器，本质上是实现了__enter__,__exit__
with app.app_context():
    a = current_app
    b = current_app.config['DEBUG']























































































