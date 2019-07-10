#!/root/.virtualenvs/flask_py3/bin/python3

from flask import Flask

# app = Flask(__name__)

#config
# <Config {'SERVER_NAME': None, 'SECRET_KEY': None, 'SESSION_COOKIE_HTTPONLY': True,
# 'JSONIFY_PRETTYPRINT_REGULAR': False, 'PROPAGATE_EXCEPTIONS': None, 'EXPLAIN_TEMPLATE_LOADING': False,
# 'PERMANENT_SESSION_LIFETIME': datetime.timedelta(31), 'SESSION_COOKIE_NAME': 'session',
# 'TRAP_HTTP_EXCEPTIONS': False, 'MAX_CONTENT_LENGTH': None, 'SESSION_REFRESH_EACH_REQUEST': True,
# 'SESSION_COOKIE_PATH': None, 'ENV': 'development', 'SESSION_COOKIE_DOMAIN': None,
# 'TRAP_BAD_REQUEST_ERRORS': None, 'TESTING': False, 'USE_X_SENDFILE': False,
# 'JSONIFY_MIMETYPE': 'application/json', 'APPLICATION_ROOT': '/', 'PREFERRED_URL_SCHEME': 'http',
# 'PRESERVE_CONTEXT_ON_EXCEPTION': None, 'JSON_AS_ASCII': True, 'MAX_COOKIE_SIZE': 4093,
# 'SESSION_COOKIE_SECURE': False, 'SESSION_COOKIE_SAMESITE': None, 'DEBUG': False,
# 'TEMPLATES_AUTO_RELOAD': None, 'JSON_SORT_KEYS': True, 'SEND_FILE_MAX_AGE_DEFAULT': datetime.timedelta(0, 43200)}>


#config-1
# app.config['DEBUG'] = True  #config 可以视作一个字典
# print(app.config)

#config-2
# class Config(object):
#     DEBUG = True
# app.config.from_object(Config)
# print(app.config)

#config-3
# app.config.from_pyfile('config.ini')
# print(app.config['DEBUG'])

#从环境变量中加载,在terminal中输入
#export A=10
# print(app.config['DEBUG'])

#从环境变量中加载，单次打开终端有效
# app.config.from_envvar('MY_CONFIG')
class Config(object):
    REDIS='redis://127.0.0.1:6379/0'
class DebugConfig(Config):
    REDIS = 'redis://127.0.0.1:6379/1'


#工厂函数
def createFlaskApp(config):
    app=Flask(__name__)
    app.config.from_object(Config)
    app.config.from_envvar('MY_CONFIG')

    return app


app=createFlaskApp(DebugConfig)



@app.route('/')
def index():
    return 'hello'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
