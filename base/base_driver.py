# -*- coding: utf-8 -*-
from __future__ import print_function

"""

@file: base_driver.py.py

@time: 2017/8/19 17:10

@desc: 浏览器驱动初始化

"""

from selenium.webdriver import Remote
# host1 = hosts.cons()
# host = hosts.cons()


def browser():
    host = '192.168.154.137:4444'
    dc = {'browserName': 'phantomjs'}
    driver = Remote(command_executor='http://' + host + '/wd/hub',
                    desired_capabilities=dc)

    return driver


if __name__ == '__main__':
    dr = browser()
    dr.get("http://www.baidu.com")
    dr.quit()
