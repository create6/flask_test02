import json


from flask import Flask, request, make_response, render_template
from flask.json import jsonify
from werkzeug.routing import BaseConverter

app = Flask(__name__)

#1-1,不指定类型也是通吃
# @app.route('/<user_id>')
# def get_url(user_id):
#     return 'user_id:%s'%user_id
#1-2,
# @app.route('/<int:user_id>')
# def get_url(user_id):
#     return 'user_id:%s'%user_id

#1-3,字符串通吃
# @app.route('/<string:user_id>')
# def get_url(user_id):
#     return 'user_id:%s'%user_id
# 1-4
# @app.route('/<float:user_id>')
# def get_money(user_id):
#     return 'money:%s'%user_id

#4自定义转换器
class MobileCoverter(BaseConverter):
    regex = r'1[3-9]\d{9}'
#写入规则
app.url_map.converters['mobile']=MobileCoverter

@app.route('/<mobile:mobileNumber>')
def get_mobile(mobileNumber):
    return 'mobileNumber:%s'%mobileNumber


#5 使用request对象获取参数
@app.route('/')
def get_request():
    # print(request.args)
    # return json.dumps(request.args.to_dict())  #?search=xxxx   #/?id=8999dsfgs&ip=990d&&name=nalf
    # return request.url  # 只针对查询参数 http://47.112.108.32:5000/?sf=ljare0435tgsg.%%
    # return json.dumps(request.headers.to_list())

    #data,POST请求
    return request.data
#6,返回响应
@app.route('/aa/')
def return_res():
    # return 'hello',202,{'name':'bobo'}
    response = make_response('index')  #需要导入
    response.status_code = 250
    return response

#7，使用json模块
@app.route('/json')
def use_json():
    data ={
        'id':15,
        'name':'jackbobo'
    }
    # return json.dumps(data),200,{'Content-Type':'application/json'}
    return jsonify(id = 1  , name='cookie')

#8,jinja2模板，render_template
@app.route('/te')
def to_template():
    id = 1
    name='jackbobo'
    # return render_template('to_template.html',name=name,id=id)
    return render_template('to_template.html',name=name,id=id),202,{'token':'jj'}

#9



if __name__ == '__main__':
    app.run()