import json
from flask import Flask,jsonify,make_response
from flask_restful import Resource,Api,reqparse



application  = Flask(__name__)
application.config['JSON_AS_ASCII'] = False
api = Api(application)


class JrWsgiServer():

    def http_badrequest(self,resp):
        return jsonify({"status": 400, "error": resp})

    def http_exception(self, e):

        import traceback
        traceback.print_exc()

        if isinstance(e, TypeError) :
            return jsonify({"status": 400, "error": '不符合要求的参数错误'})

        if isinstance(e, AssertionError):
            return jsonify({"status": 400, "error": e.args[0]})

        return jsonify({"status": 500, "error": "Internal Server Error"})

    def http_ok(self, resp):
        """
            使用jsonify时响应的Content-Type字段值为application/json，而使用json.dumps时该字段值为text/html。
            Content-Type决定了接收数据的一方如何看待数据，如何处理数据，如果是application/json，则可以直接当做json对象处理，
            若是text/html，则还要将文本对象转化为json对象再做处理"""

        # 1.默认响应application/json
        #return jsonify({"status": 200, "result": resp})

        # 2.使用元组，返回自定义的响应信息 是有顺序的，第一个响应体，第二个状态码，第三个响应头，可以从后面省但不可从前面省
        #return "Hello",200,{"Content-Type":"text/html; charset=utf-8","City":"Beijing"}


        # 3.自定义响应头为text/html 前端需要反向解析
        response = make_response(json.dumps({"status":200,"result":resp},ensure_ascii=False))
        response.headers["Content-Type"] = 'text/html; charset=utf-8'
        return response

class TaskListAPI(Resource,JrWsgiServer):

    def get(self):
        try:
            data = {}
            #assert data,'数据不能为空'
            #name = data["name"]
            #c = 11 + "jockfi"
            resp = ["人生苦短 我用Python",]

            #return self.http_badrequest('添加院线失败，请联系管理员')
        except Exception as e:
            return self.http_exception( e )


        return  self.http_ok(resp)



api.add_resource(TaskListAPI, '/index', endpoint = 'tasks')



if __name__ == '__main__':
    application.run("0.0.0.0",8088,debug=True)


