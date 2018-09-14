#===============================================================================
# 电子邮件
#===============================================================================
from threading import Thread
from flask import current_app, render_template
from flask_mail import Message
from app import mail

# 异步函数
#------------------------------------------------------------------------------ 
def send_async_email(app, msg):
    with app.app_context():# 手动装载，否则报错
        try:
            mail.send(msg)
        except Exception as e:
            pass


# 发送电子邮件
#------------------------------------------------------------------------------ 
def send_mail(to, subject, template, **kwargs):
#     msg = Message('测试邮件', sender='admin@qq.com', body='Test',recipients=['aimUser@qq.com'])
    msg = Message('[鱼书]' + ' ' +subject, sender=current_app.config['MAIL_USERNAME'], recipients=[to])
    msg.html = render_template(template)        # 发送HTML文件
    
    # 启动异步线程
    thr = Thread(target=send_async_email, args=[current_app, msg])   # 因为这里会使用线程，所以需要将app推入栈中
    thr.start()
      
























































