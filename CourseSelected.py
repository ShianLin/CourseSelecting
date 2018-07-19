#!python3
#coding:utf8
'a class selected module '
__author__ = 'shianlin'
#引号中的中文、全大写替换成对应的

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import sys
import threading


class CourseSelect:
    def __int__(self):
        pass

    def loginToSelectCource(self,id,pwd):
        self.url="网址"
        self.browser =webdriver.Chrome()
        browser=self.browser
        page =browser.get(self.url)
        username=browser.find_element_by_id('username')
        password=browser.find_element_by_id('password')
        username.send_keys(id)
        password.send_keys(pwd)
        loginBtn=browser.find_element_by_xpath("XPATH")
        loginBtn.submit()
        time.sleep(20)#check to reduce time
        kcgl=browser.find_element_by_xpath('XPATH')
        kcgl.click()#get in


    def select(self,xpath):
        browser=self.browser
        url="登陆后的网址"
        browser.get(url)
    #    trytime=0
        while True:
            xk=browser.find_element_by_xpath(xpath)
            xk.click()
            time.sleep(8)
            knows=browser.switch_to_alert()
            if knows.text=="选课成功！":
                knows.accept()
                break
                browser.quit()
            else:
    #            print(knows.text)
                knows.accept()
    #            trytime+=1
    #            print(trytime)



id='自己的id'
pwd='自己的密码'
xpath="XPATH"
xk =CourseSelect()
xk.loginToSelectCource(id,pwd)
xk.select(xpath)



'''
问题一：不停点那个地方导致（选课-退选）：“选课成功”终结；else继续
二：无法比较之后再选:盲选，给定Xpath
三：对话框跳出之后刷新页面(不用)
方案：
1.登陆
2.同时进行(写一个大的)

基本解决，之后再：
1.写个大的，可以同时选课并且控制结束
2.优化时间

'''
