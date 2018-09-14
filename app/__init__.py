#===============================================================================
# 项目初始化
#===============================================================================
from flask import Flask
from flask_login import LoginManager
from app.models.base import db
from flask_mail import Mail

login_manager = LoginManager()
mail = Mail()


# 初始化app对象
def create_app():
    app = Flask(__name__)
#     app = Flask(__name__, static_folder='view_models/statics')在这里可以设置默认的静态文件夹的位置,在这里同样也可以指定模板文件夹
    app.config.from_object('app.secure')    
    app.config.from_object('app.setting')    
    register_blueprint(app)# 注册蓝图
    
    # 使用应用上下文注入app
    db.init_app(app)
    
    # 初始化LoginManager
    login_manager.init_app(app)  # 用户登录及权限插件
    login_manager.login_view = 'web.login'  # 如果用户权限不足，将会跳转到登录页面
    login_manager.login_message = '请先登录或注册'
    
    mail.init_app(app)      # 注册flask-mail组件
    
    with app.app_context():
        db.create_all()
#     db.init_app(app)# 注册SQAlchemy
#     db.create_all(app=app)# 生成数据表
    
    
    return app


# 注册蓝图
def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)















































