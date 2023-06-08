# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     conftest
   Description :
   Author :       zhangxj
   date：          2023/6/8
-------------------------------------------------
   Change Activity:
                   2023/6/8:
-------------------------------------------------
"""
import pytest
import os
import yaml


@pytest.fixture(scope="session")
def env(request):
    config_path = os.path.join(request.config.rootdir,
                               "configs",
                               request.config.getoption("environment"),
                               "config.yaml")
    with open(config_path) as f:
        env_config = yaml.load(f.read(), Loader=yaml.SafeLoader)
    return env_config


def pytest_addoption(parser):
    parser.addoption("--env",
                     action="store",
                     dest="environment",
                     default="test",
                     help="environment: test or prod")
