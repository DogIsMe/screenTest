# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 14:12:15 2021

@author: tt
"""
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import pyautogui as g


my_sender='1514317161@qq.com'    # 发件人邮箱账号
my_pass = 'cueutwmxunrficfi'              # 发件人邮箱密码
my_user='henanyidoubi@163.com'      # 收件人邮箱账号，我这边发送给自己

def mail(text ='出错了！'):
    try:
        msg=MIMEText(text,'plain','utf-8')
        msg['From']=formataddr(["FromRunoob",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["FK",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="脚本运行情况"                # 邮件的主题，也可以说是标题
 
        server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print("邮件发送失败")
        return
    print("邮件发送成功")

g.PAUSE =1
#等待次数
wait_times = 20

# x= g.locateOnScreen('xuan_shang_tu_biao.png')

# print(x)


#定位窗口坐标
pos_1 =g.locateOnScreen('lu_shi_chuan_shuo_wen_zi.png', grayscale=True,confidence=0.5)
qu_yu =(pos_1.left,pos_1.top,1912-pos_1.left,809-pos_1.top)
print(qu_yu)

record_message = ''

def shu_biao_init():
    g.moveTo(qu_yu[0],qu_yu[1])

def get_tu_pian_position(url):
    for i in range(5):
        box= g.locateOnScreen(url,grayscale=True,confidence=0.5,region=qu_yu)
        if box:
            return g.center(box)
    return None
 
def get_p_1(map_id):
    pos = get_tu_pian_position('pin_xi_zhi_di.png')
    if map_id==1:
        print(pos)
 

def click_png(url):
    shu_biao_init()
    pos = get_tu_pian_position(url)
    if pos:
        g.sleep(1)
        g.click(pos)
        g.sleep(1)
        # g.click(pos)
        return True
    else:
        return False

def wait_click_png(url):
    for i in range(wait_times):
        if not click_png(url):
            g.sleep(1)
        else:
            return True
    return False 



def fin_png(url):
    for i in range(wait_times):
        if get_tu_pian_position(url)== None:
            g.sleep(1)
        else:
            return True
   
    return False

def wait_error():
    global record_message
    if not wait_click_png('kai_shi_an_niu_1.png'):
        t = '等待点击开始按钮时报错!'
        record_message = record_message + '\n' +  t
        mail(record_message)
        raise Exception (t)



def wait_dan_dou_sheng_li():
    shu_biao_init()
    for i in range(wait_times):
        if not click_png('zhan_dou_sheng_li_1.png'):
            if get_tu_pian_position ('jiu_xu_an_niu_2.png') == None:
                g.sleep(1)
            else:
                return False
        else:
            return True
    return False 

def shi_fang_ji_neng_1():
    print('释放技能1')
    #按下技能1
    g.click(qu_yu[0]+380,qu_yu[1]+370)
    g.click(qu_yu[0]+480,qu_yu[1]+235)
    click_png('jiu_xu_an_niu_1.png')
    
def zhan_dou():
     global record_message
     record_message = record_message +'战斗!'
     print(record_message)
     g.sleep(5)
     shu_biao_init()
     if not wait_click_png('yi_deng_chang_1.png'):
         t = '等待已登场按钮报错!'
         record_message = record_message+'\n'+ t
         mail(record_message)
         raise Exception(t)
     shu_biao_init()
     if not fin_png('jiu_xu_an_niu_3.png'):
         t='无法找到就绪按钮！'
         record_message = record_message+'\n'+ t
         mail(record_message)
         raise Exception (t)
     shi_fang_ji_neng_1()
     ji_neng_1_times = 1
     while wait_dan_dou_sheng_li() == False:
         shi_fang_ji_neng_1()
         ji_neng_1_times +=1
         if ji_neng_1_times > 10:
             t = '释放技能一大于10次了'
             record_message = record_message+'\n'+ t
             mail(record_message)
             raise Exception(t)
         

def xuan_ze_bao_zang():
    global record_message
    record_message = record_message + '选择宝藏'
    print(record_message)    
    #选择宝藏1
    g.sleep(5)
    g.click(qu_yu[0]+420,qu_yu[1]+380)
    g.click(qu_yu[0]+620,qu_yu[1]+635)
    g.sleep(5)

def guan_qia_1():
    global record_message
    record_message ='关卡1'
    print(record_message)
    g.click(qu_yu[0]+370,qu_yu[1]+370)         
    wait_error()
    
    zhan_dou()
    g.sleep(2)
    xuan_ze_bao_zang()
    
def guan_qia_2():
    global record_message
    record_message ='关卡2'
    print(record_message)
    #关卡2   
    g.click(qu_yu[0]+280,qu_yu[1]+385)
    g.click(qu_yu[0]+485,qu_yu[1]+385)
    g.click(qu_yu[0]+470,qu_yu[1]+385)
    g.click(qu_yu[0]+275,qu_yu[1]+385)
    g.click(qu_yu[0]+550,qu_yu[1]+385)
    g.click(qu_yu[0]+210,qu_yu[1]+385)
    
    wait_error()
    
    zhan_dou()
    g.sleep(2)
    xuan_ze_bao_zang()

def guan_qia_3():
    global record_message
    record_message ='关卡3'
    print(record_message)
    g.click(qu_yu[0]+170,qu_yu[1]+410)
    g.click(qu_yu[0]+370,qu_yu[1]+410)
    g.click(qu_yu[0]+570,qu_yu[1]+410)
    wait_error()
    
    zhan_dou()
    g.sleep(2)
    #选择宝藏1
    xuan_ze_bao_zang()
    

def boss_guan_qia():
    global record_message
    record_message ='boss关卡'
    print(record_message)
    g.click(qu_yu[0]+370,qu_yu[1]+190)
    wait_error()
    
    zhan_dou()
    g.sleep(15)
 
def tong_guan_jiang_li():
    global record_message
    record_message ='通关奖励'
    print(record_message)
    g.click(qu_yu[0]+540,qu_yu[1]+265)
    g.click(qu_yu[0]+320,qu_yu[1]+590)
    g.click(qu_yu[0]+780,qu_yu[1]+590)
    g.click(qu_yu[0]+550,qu_yu[1]+445)
    g.sleep(5)
 
# if get_tu_pian_position('pin_xi_zhi_di_xuan_shang_1.png'):
#     click_png('pin_xi_zhi_di_xuan_shang_1.png')
# else:
#     pass
#     # click_png('pin_xi_zhi_di_xuan_shang_2.png')

# click_png('pu_tong_nan_du.png') 
# click_png('xuan_ze_an_niu_1.png')

countTime =0
# click_png('1-1-xuan_zhong_1.png')
# while False:
while True:
    if not wait_click_png('1-1-xuan_zhong_2.png'):
        t ='选择1-1关卡报错了'
        mail(t)
        raise Exception(t)
    g.sleep(1)
    if not wait_click_png('xuan_ze_an_niu_2.png'):
        t ='队伍选择按钮报错了'
        mail(t)
        raise Exception(t)
    g.sleep(1)
    # if not click_png('dui_wu_1.png'):
    #     print("2")
    #     break
    if not wait_click_png('xuan_ze_an_niu_2.png'):
        t ='关卡选择按钮报错了'
        mail(t)
        raise Exception(t)
    g.sleep(1)
    # if not click_png('suo_ding_an_niu.png'):
    #     print("4")
    #     break
    
    guan_qia_1()
    guan_qia_2()
    
    guan_qia_3()
    
    boss_guan_qia()
    g.sleep(3)
    tong_guan_jiang_li()
    
    g.click(qu_yu[0]+510,qu_yu[1]+650)
    g.sleep(5)
    countTime = countTime+1
    print(str(countTime)+'次完成')
# print(g.position())
# x = get_tu_pian_position('jiu_xu_an_niu_2.png')
# print(x)
# mail()














