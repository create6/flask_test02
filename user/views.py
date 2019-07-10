from user import user_bp
from flask import render_template

#2使用蓝图定义路由
@user_bp.route('/collect')
def index():
    return render_template('my_collect.html')