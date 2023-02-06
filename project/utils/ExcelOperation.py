# !/usr/bin/env python
# -*-coding:utf-8 -*-

from project.utils.HttpMethod import *
from os import path
import xlwings as xw
import json
import logging
import time


def log():
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.DEBUG)  # 设置日志级别,只打印该级别以上的日志
    console = logging.StreamHandler()  # 创建一个StreamHandler，用于输出到控制台
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # 自定义输出格式
    console.setFormatter(formatter)  # 绑定格式
    logger.addHandler(console)
    # logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    return logger


"""
visible
True：可见excel
False：不可见excel

add_book
True:打开excel并且新建工作簿
False：不新建工作簿
"""


def excel_operate():
    app = xw.App(visible=False, add_book=False)
    excel = path.abspath(path.dirname(__file__)) + '/excel/test_case.xlsx'
    wb = app.books.open(excel)
    sheet = wb.sheets["Sheet1"]  # 表单
    rows = sheet.used_range.last_cell.row  # 最大行
    case_total = 0  # 用例总数
    case_success = 0  # 成功用例数
    case_fail = 0  # 失败用例数
    logger = log()

    for i in range(2, rows + 1):
        print(i)
        print(sheet.range(i,1).value)
        case_id = sheet.range(i, 1).value  # 用例编号
        case_name = sheet.range(i, 2).value  # 用例名
        request_method = sheet.range(i, 3).value  # 请求方法
        url = sheet.range(i, 4).value  # 接口地址
        data = sheet.range(i, 5).value  # 请求参数
        expected_result = sheet.range(i, 6).value  # 预期结果

        if request_method == "get":
            if data is not None:
                actual_result = HttpMethod(url + data.replace('"', '')).ex_get()
            else:
                actual_result = HttpMethod(url).ex_get()
            try:
                assert expected_result == actual_result
            except AssertionError:
                logger.warning("编号：{}用例测试失败，用例名：{}".format(case_id, case_name))
                case_fail = case_fail + 1
            else:
                logger.info("编号：{}用例测试成功，用例名：{}".format(case_id, case_name))
                case_success = case_success + 1
        if request_method == "post":
            actual_result = HttpMethod(url).ex_post(json.loads(data))
            try:
                assert expected_result == actual_result
            except AssertionError:
                logger.warning("编号：{}用例测试失败，用例名：{}".format(case_id, case_name))
                case_fail = case_fail + 1
            else:
                logger.info("编号：{}用例测试成功，用例名：{}".format(case_id, case_name))
                case_success = case_success + 1
        if request_method == "put":
            actual_result = HttpMethod(url).ex_put(json.loads(data))
            try:
                assert expected_result == actual_result
            except AssertionError:
                logger.warning("编号：{}用例测试失败，用例名：{}".format(case_id, case_name))
                case_fail = case_fail + 1
            else:
                logger.info("编号：{}用例测试成功，用例名：{}".format(case_id, case_name))
                case_success = case_success + 1
        case_total = case_total + 1
    time.sleep(1)
    print()
    print("测试完成，用例总数：{}，成功用例数：{}，失败用例数：{}，成功率：{:.2f}%".format(case_total, case_success, case_fail,
                                                              case_success / case_total * 100))

    wb.save()
    wb.close()
    app.quit()


excel_operate()
