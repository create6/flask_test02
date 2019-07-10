from flask import Flask
from user import user_bp
app = Flask(__name__)



#3，把蓝图对象注册到app中
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run()