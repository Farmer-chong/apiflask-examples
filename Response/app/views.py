# -*- coding: utf-8 -*-
'''
    :file: views.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2021/12/02 10:33:44
'''
from apiflask import APIBlueprint, output, Schema, abort, input
from marshmallow.fields import String

from app.utils import make_resp, Result

test_bp = APIBlueprint("test", __name__)

mock_data = [{
    "username": "admin",
    "password": "admin"
}, {
    "username": "admin-2",
    "password": "admin"
}]


class MockData(Schema):
    username = String()
    password = String()


@test_bp.get("/")
@output(MockData(many=True))
def index():
    try:
        # 注释掉下面一行，测试abort返回错误
        # raise Exception
        return make_resp(mock_data, status_code=400)
    except Exception:
        """通过abort，返回错误"""
        abort(500, message="nothing", extra_data=make_resp(None))


@test_bp.route("/test")
def test():
    # 链式调用构建响应
    data = Result.ok().setData(mock_data).to_dict()
    return data


class InputSchema(Schema):
    # 通过example字段给出示例，使api文档更友好
    data = String(example="this is a example data string.")


@test_bp.post("/post")
@input(InputSchema)
def post(data):
    return data
