#===============================================================================
# 配置文件:机密信息保存
#===============================================================================

DEBUG = True                # 开启debug模式

HOST = '0.0.0.0'            # 主机
PORT = 5001                 # 端口

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/db_flask'     # 数据库连接；不需要注册，Flask框架会自动读取

SECRET_KEY = 'cijemuogmm'   # 消息闪现密钥；不需要注册，Flask框架会自动读取

# Email的配置文件
MAIL_SERVER = 'smtp.qq.com'             # 电子邮箱的地址
MAIL_PORT = 465                 
MAIL_USE_SSL = True 
MAIL_USE_TSL = False
MAIL_USERNAME = 'admin@qq.com'          # qq邮箱地址
MAIL_PASSWORD = '123456'                # qq邮箱的授权码
MAIL_SUBJECT_PREFIX = '[鱼书]'
MAIL_SENDER = '鱼书 <hello@yushu.im>'












































