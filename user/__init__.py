from flask import Blueprint

#1,创建蓝图对象
user_bp=Blueprint('user',
                  __name__,
                  static_folder='user_static',
                  static_url_path='/user_s',
                  # template_folder='user_t'
                  )

from . import views