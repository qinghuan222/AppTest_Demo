# !/usr/bin/env python
# -*-coding:utf-8 -*-

import requests
import json

from project.utils import Token
from project.utils import Environment


class HttpMethod(object):

    def __init__(self, url,):
        self.url = url


    def response(self, request):
        r_dict = json.loads(request.text)
        r_dict_data = r_dict.get('data')

        if r_dict.get('success') is True:  #
            print('请求成功')
            if r_dict_data is not None:
                print('响应结果:')
                print(json.dumps(r_dict_data, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': ')))

            return r_dict_data

        else:
            print('请求失败！')
            print('响应结果:')
            print(json.dumps(r_dict, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': ')))
            return

    def execute(self, data, request, method):
        if method == "get":
            self.response(request)
        elif method == "post" or "put":
            if len(data) != 0:
                print('请求参数:')
                print(json.dumps(data, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': ')))
                self.response(request)
        elif method == "delete":
            self.response(request)
            return

    def get(self):
        headers = {
            "token": Token.token
        }
        request = requests.get(Environment.url_pre + self.url, headers=headers)
        method = "get"
        self.execute(None, request, method)

    def post(self, data):
        headers = {
            "token": Token.token
        }
        request = requests.post(Environment.url_pre + self.url, headers=headers, json=data)
        method = "post"
        self.execute(data, request, method)

    def put(self, data):
        headers = {
            "token": Token.token
        }
        request = requests.put(Environment.url_pre + self.url, headers=headers, json=data)
        method = "put"
        self.execute(data, request, method)

    def delete(self):
        headers = {
            "token": Token.token
        }
        request = requests.delete(Environment.url_pre + self.url, headers=headers)
        method = "delete"
        self.execute(None, request, method)

    # wx端
    # def get1(self):
    #     headers = {
    #         "token": Token.wx_token
    #     }
    #     request = requests.get(Environment.wx_url_pre + self.url, headers=headers)
    #     method = "get"
    #     self.execute(None, request, method)
    #
    # def post1(self, data):
    #     headers = {
    #         "token": Token.wx_token
    #     }
    #     request = requests.post(Environment.wx_url_pre + self.url, headers=headers, json=data)
    #     method = "post"
    #     self.execute(data, request, method)
    #
    # def put1(self, data):
    #     headers = {
    #         "token": Token.wx_token
    #     }
    #     request = requests.put(Environment.wx_url_pre + self.url, headers=headers, json=data)
    #     method = "put"
    #     self.execute(data, request, method)
    #
    # def delete1(self):
    #     headers = {
    #         "token": Token.wx_token
    #     }
    #     request = requests.delete(Environment.wx_url_pre + self.url, headers=headers)
    #     method = "delete"
    #     self.execute(None, request, method)

    # excel操作方法
    def ex_get(self):
        headers = {
            "token": Token.token
        }
        request = requests.get(Environment.url_pre + self.url, headers=headers)
        r_dict = json.loads(request.text)
        result = r_dict.get('success')
        return result

    def ex_post(self, data):
        headers = {
            "token": Token.token
        }
        request = requests.post(Environment.url_pre + self.url, headers=headers, json=data)
        r_dict = json.loads(request.text)
        result = r_dict.get('success')
        return result

    def ex_put(self, data):
        headers = {
            "token": Token.token
        }
        request = requests.put(Environment.url_pre + self.url, headers=headers, json=data)
        r_dict = json.loads(request.text)
        result = r_dict.get('success')
        return result
