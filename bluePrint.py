from flask import Flask,render_template,Blueprint

app = Flask(__name__)

#1,创建蓝图对象
user_bp=Blueprint('user',__name__)

#2使用蓝图定义路由
@user_bp.route('/index')
def index():
    return render_template('my_collect.html')

#3，把蓝图对象注册到app中
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run()