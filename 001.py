import time
import random

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

driver: WebDriver = webdriver.Chrome()    # Chrome浏览器
driver.get("http://202.206.48.112:8016/login.aspx")
print("更新:最多支持到200条记录")
print("输入学号")
driver.find_element_by_id("txtUserName").send_keys(input())
print("输入密码")
driver.find_element_by_id("txtPwd").send_keys(input())
print("输入验证码 回车")
driver.find_element_by_id("txtYzm").send_keys(input())
driver.find_element_by_id("btnLogin").click()
driver.implicitly_wait(30)
driver.get("http://202.206.48.112:8016/TeacherEvaluation/NoticeStu.aspx")
driver.maximize_window()
search_window = driver.current_window_handle
driver.find_element_by_xpath("/html/body/div/button").click()
driver.implicitly_wait(30)

def lilunke(i):

    time.sleep(5)
    j = random.randint(1, 3)
    driver.find_element_by_xpath(
        "/html/body/fieldset/div/div/div[1]/div[3]/div[2]/table/tbody/tr[" + str(i) + "]/td/div/div/a[1]/i").click()
    driver.implicitly_wait(30)
    driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div[1]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="sub-question-C167Ry46XOa77DHVTH8G"]/div[2]/div[' + str(j) + ']').click()
    driver.find_element_by_xpath('//*[@id="sub-question-C167Rm46YHgGP10O02BE"]/div[2]/div[1]').click()
    driver.find_element_by_xpath('//*[@id="sub-question-C167Rg473Ld1UVQC58SF"]/div[2]/div[2]').click()

    driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/div[1]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="sub-question-C167Rk4AD2lKK02UQPF3"]/div[2]/div[1]').click()
    driver.find_element_by_xpath('//*[@id="sub-question-C167Rd4AKFgNSP0R7XCB"]/div[2]/div[1]').click()
    driver.find_element_by_xpath('//*[@id="sub-question-C167Ru4AV8a7S8YKKRC2"]/div[2]/div[2]').click()
    driver.find_element_by_xpath('//*[@id="sub-question-C167Rr4B6LdLWAWPB46C"]/div[2]/div[2]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="sub-question-C167Rp4B7QhYCGBQYPFA"]/div[2]/div[1]').click()
    driver.find_element_by_xpath('//*[@id="sub-question-C167Rx4BENcB7FMOWA5D"]/div[2]/div[1]').click()
    driver.find_element_by_xpath('//*[@id="sub-question-C167Re4BFDbQ6IECQ6M7"]/div[2]/div[1]').click()

    driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[3]/div[1]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="sub-question-C167Rs4KWFm8DKB468MH"]/div[2]/div[1]').click()
    driver.find_element_by_xpath('//*[@id="sub-question-C167Ry4LATb3V8Q1S1NR"]/div[2]/div[1]').click()
    driver.find_element_by_xpath('//*[@id="sub-question-C167Rr4LFUqMBFYGGB56"]/div[2]/div[1]').click()
    driver.find_element_by_xpath('//*[@id="sub-question-C167Rp4LIErQY0Y52MXA"]/div[2]/div[1]').click()

    driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[4]/div[1]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="sub-question-C167Rg4LGBsHI7P74TGW"]/div[2]/div[1]').click()
    driver.find_element_by_xpath('//*[@id="sub-question-C167Ri4LZMiWQ2IGW31E"]/div[2]/div[1]').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[6]/button[1]').click()
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div[4]/div[3]/a').click()
    time.sleep(5)

def shixi(i):

    time.sleep(5)
    j = random.randint(1, 3)
    driver.find_element_by_xpath(
        "/html/body/fieldset/div/div/div[1]/div[3]/div[2]/table/tbody/tr[" + str(i) + "]/td/div/div/a[1]/i").click()
    driver.implicitly_wait(30)

    driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div[1]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="sub-question-C16AOp30LBaXOHQWADUI"]/div[2]/div[' + str(j) + ']').click()
    driver.find_element_by_xpath('//*[@id="sub-question-C16AOa30N7hM43RI0708"]/div[2]/div[1]').click()

    driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/div[1]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="sub-question-C16AOr30U6lGVOUU62GR"]/div[2]/div[1]').click()
    driver.find_element_by_xpath('//*[@id="sub-question-C16AOb30VYrEA1XXQE7S"]/div[2]/div[1]').click()
    driver.find_element_by_xpath('//*[@id="sub-question-C16AOd30WZn0G544TORH"]/div[2]/div[2]').click()
    driver.find_element_by_xpath('//*[@id="sub-question-C16AOq30YVt450B72GER"]/div[2]/div[' + str(j) + ']').click()


    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[3]/div[1]').click()
    driver.find_element_by_xpath('//*[@id="sub-question-C16AOk313YgKXEVST493"]/div[2]/div[1]').click()
    driver.find_element_by_xpath('//*[@id="sub-question-C16AOe314KgX1GOM5TNK"]/div[2]/div[1]').click()

    driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[4]/div[1]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="sub-question-C16AOi3158qHEOLECGBS"]/div[2]/div[1]').click()
    driver.find_element_by_xpath('//*[@id="sub-question-C16AOm316VcN4RGQQYSL"]/div[2]/div[1]').click()

    driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[5]/button[1]').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[4]/div[3]/a').click()
    time.sleep(2)
def start(begin,end):
    for k in range(int(begin), int(end)+1):
        print("当前总条目" + str(k))
        i = k % 10
        if i == 0:
            i = 10
        if k >= 1 and k <= 10:
            h = 1
        if k >= 11 and k <= 20:
            h = 2
        if k >= 21 and k <= 30:
            h = 3
        if k >= 31 and k <= 40:
            h = 4
        if k >= 41 and k <= 50:
            h = 5
        if k >= 51 and k <= 60:
            h = 6
        if k >= 61 and k <= 70:
            h = 7
        if k >= 71 and k <= 80:
            h = 8
        if k >= 81 and k <= 90:
            h = 9
        if k >= 91 and k <= 100:
            h = 10
        if k >= 101 and k <= 110:
            h = 11
        if k >= 111 and k <= 120:
            h = 12
        if k >= 121 and k <= 130:
            h = 13
        if k >= 131 and k <= 140:
            h = 14
        if k >= 141 and k <= 150:
            h = 15
        if k >= 151 and k <= 160:
            h = 16
        if k >= 161 and k <= 170:
            h = 17
        if k >= 171 and k <= 180:
            h = 18
        if k >= 181 and k <= 190:
            h = 19
        if k >= 191 and k <= 200:
            h = 20

        print(i)
        print("当前页面" + str(h))
        print("当前页面条目" + str(i))
        driver.find_element_by_xpath('/html/body/fieldset/div/div/div[2]/div/div/span[3]/input').clear()
        driver.find_element_by_xpath('/html/body/fieldset/div/div/div[2]/div/div/span[3]/input').send_keys(str(h))
        driver.find_element_by_xpath('/html/body/fieldset/div/div/div[2]/div/div/span[3]/button').click()
        time.sleep(3)
        s = driver.find_element_by_xpath(
            '/html/body/fieldset/div/div/div[1]/div[2]/table/tbody/tr[' + str(i) + ']/td[5]/div').text

        if s == '理论课':
            print(s)
            lilunke(i)

        if s == '见习课':
            print(s)
            shixi(i)



print("请输入分几段评分")
a=1
b = input()
while a <=   int(b):
    print("本次开始条目")
    begin = input()
    print("本次结束条目")
    end = input()
    if int(begin) > int(end):
        print("输入错误")
    else:
        start(begin, end)
    a = a+1








