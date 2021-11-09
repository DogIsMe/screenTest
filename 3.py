# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 14:12:15 2021

@author: tt
"""

import pyautogui as g

g.PAUSE =1



# x= g.locateOnScreen('xuan_shang_tu_biao.png')

# print(x)

map_pin_1={
    1:'1-1',
    2:'1-2',
    3:'1-3',}
#定位窗口坐标
pos_1 =g.locateOnScreen('lu_shi_chuan_shuo_wen_zi.png', grayscale=True,confidence=0.5)
qu_yu =(pos_1.left,pos_1.top,1912-pos_1.left,809-pos_1.top)
print(qu_yu)
last_position =[]
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
    pos = get_tu_pian_position(url)
    if pos:
        last_position = pos
        g.click(pos)
        g.click(pos)
        return True
    else:
        return False

def wait_click_png(url):
    for i in range(20):
        if not click_png(url):
            g.sleep(1)
        else:
            print(str(i)+'waits')
            return True
    return False 



def fin_png(url):
    for i in range(20):
        if get_tu_pian_position(url)== None:
            g.sleep(1)
        else:
            return True
   
    return False

def shu_biao_init():
    g.moveTo(qu_yu[0],qu_yu[1])

def wait_dan_dou_sheng_li():
    shu_biao_init()
    for i in range(20):
        if not click_png('zhan_dou_sheng_li_1.png'):
            if get_tu_pian_position ('jiu_xu_an_niu_2.png') == None:
                g.sleep(1)
            else:
                return False
        else:
            print(str(i)+'waits')
            return True
    return False 

def shi_fang_ji_neng_1():
    print('释放技能1')
    #按下技能1
    g.click(qu_yu[0]+510,qu_yu[1]+370)
    g.click(qu_yu[0]+480,qu_yu[1]+235)
    click_png('jiu_xu_an_niu_1.png')
    
def zhan_dou():
     print('战斗')
     g.sleep(5)
     shu_biao_init()
     if not wait_click_png('yi_deng_chang_1.png'):
         raise Exception('yi_deng_chang_1 error')
     shu_biao_init()
     if not fin_png('jiu_xu_an_niu_3.png'):
         raise Exception ('jiu_xu_an_niu_3.png is error')
     shi_fang_ji_neng_1()
     while wait_dan_dou_sheng_li() == False:
         shi_fang_ji_neng_1()

def xuan_ze_bao_zang():
    print('选择宝藏')
    #选择宝藏1
    g.sleep(5)
    g.click(qu_yu[0]+420,qu_yu[1]+380)
    g.click(qu_yu[0]+620,qu_yu[1]+635)
    g.sleep(5)

def guan_qia_1():
    print('关卡1')
    g.click(qu_yu[0]+370,qu_yu[1]+370)         
    if not wait_click_png('kai_shi_an_niu_1.png'):
        raise Exception ('kai_shi_an_niu_1错误错误')
    zhan_dou()
    g.sleep(2)
    xuan_ze_bao_zang()
    
def guan_qia_2():
    print('关卡2')
    #关卡2   
    g.click(qu_yu[0]+280,qu_yu[1]+385)
    g.click(qu_yu[0]+485,qu_yu[1]+385)
    g.click(qu_yu[0]+470,qu_yu[1]+385)
    g.click(qu_yu[0]+275,qu_yu[1]+385)
    g.click(qu_yu[0]+550,qu_yu[1]+385)
    g.click(qu_yu[0]+210,qu_yu[1]+385)
    if not wait_click_png('kai_shi_an_niu_1.png'):
        raise Exception ('kai_shi_an_niu_1错误')
    zhan_dou()
    g.sleep(2)
    xuan_ze_bao_zang()

def guan_qia_3():
    print('关卡3')
    g.click(qu_yu[0]+170,qu_yu[1]+410)
    g.click(qu_yu[0]+370,qu_yu[1]+410)
    g.click(qu_yu[0]+570,qu_yu[1]+410)
    if not wait_click_png('kai_shi_an_niu_1.png'):
        raise Exception ('kai_shi_an_niu_1错误')
    zhan_dou()
    g.sleep(2)
    #选择宝藏1
    xuan_ze_bao_zang()
    

def boss_guan_qia():
    print('boss关卡')
    g.click(qu_yu[0]+370,qu_yu[1]+190)
    if not wait_click_png('kai_shi_an_niu_1.png'):
         raise Exception ('kai_shi_an_niu_1错误')
    zhan_dou()
    g.sleep(15)
 
def tong_guan_jiang_li():
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
        print("1")
        break
    if not wait_click_png('xuan_ze_an_niu_2.png'):
        print("5")
        break
    
    # if not click_png('dui_wu_1.png'):
    #     print("2")
    #     break
    if not wait_click_png('xuan_ze_an_niu_2.png'):
        print("3")
        break
    # if not click_png('suo_ding_an_niu.png'):
    #     print("4")
    #     break
    
    guan_qia_1()
    guan_qia_2()
    
    guan_qia_3()
    
    boss_guan_qia()
    
    tong_guan_jiang_li()
    
    g.click(qu_yu[0]+510,qu_yu[1]+650)
    g.sleep(5)
    countTime = countTime+1
    print(str(countTime)+'次完成')
# print(g.position())
# x = get_tu_pian_position('jiu_xu_an_niu_2.png')
# print(x)















