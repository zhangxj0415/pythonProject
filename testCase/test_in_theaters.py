# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_in_theaters
   Description :
   Author :       zhangxj
   date：          2023/6/8
-------------------------------------------------
   Change Activity:
                   2023/6/8:
-------------------------------------------------
"""
import requests
import pytest
from utils.commonlib import get_test_data

cases, parameters = get_test_data(r"D:\pythonproject\tangshan\data\test_in_theaters.yaml")
list_params=list(parameters)

class TestInTheaters(object):
    @pytest.mark.parametrize("case,http,expected", list(list_params), ids=cases)
    def test_in_theaters(self, env, case, http, expected):
        r = requests.request(http["method"],
                             url=env["host"]["douban"] + http["path"],
                             headers=http["headers"],
                             params=http["params"])
        response = r.json()

        assert response["count"] == expected['response']["count"]
        assert response["start"] == expected['response']["start"]
        assert response["title"] == expected['response']["title"], "实际的标题是：{}".format(response["title"])