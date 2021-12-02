# -*- coding: utf-8 -*-
'''
    :file: app.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2021/08/04 16:22:45
'''

from flask import request
from apiflask import APIFlask, input, output, abort
from apiflask.decorators import doc
from marshmallow.fields import Raw
from schema import UserInSchema, UserOutSchema, IconInSchema


app = APIFlask(__name__)

# 数据库
USERS = [{
    "username": "farmer",
    "pwd": "admin",
    "url": "https://blog.farmer233.top"
}]

@app.post("/register")
# input默认是从json中获取
@input(UserInSchema)
@output(UserOutSchema)
def register(data):
    USERS.append(data)
    return data

@app.post("/append")
# 从form获取表单数据
@input(UserInSchema, location="form")
@output(UserOutSchema)
def append(data):
    USERS.append(data)
    return data

@app.post("/login")
@input(UserInSchema)
def login(data):
    password = data.get("pwd")
    for user in USERS:
        if user["pwd"] == password:
            token = "This is a token."
            return {"token": token, **data}

    abort(404, "用户未注册")

# @app.post("/icon")
# @input(IconInSchema, location="files")
# @doc(description="上传头像")
# def icon(data):
#     print(data)
#     print(request.files.get("icon"))
#     return {"ok": 'ok'}

@app.post("/icon")
@input({"icon": Raw(type="file", required=True)}, location="files")
@doc(description="上传头像")
def icon(data):
    print(data.get("icon"))
    return {"ok": 'ok'}
