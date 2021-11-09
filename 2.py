# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 10:04:09 2021

@author: 15143
"""
import pyautogui as g
import time

kai_shi_xuan_ze =(1768,644)
xuan_ze_dui_wu =(1701, 689)
di_yi_guan_ka_xuan_ze =(1253, 389)
guan_ka_kai_shi = (1788, 646)
deng_cheng_an_niu=(1815, 396)
ji_neng_1=(1247, 389)
liang_ge_mu_biao_2 =(1352, 263)
jiu_xu = deng_cheng_an_niu
bao_zang_xuan_ze = (1310, 396)
huo_qu_bao_zang_an_niu=(1511, 660)
di_er_guan_ka_xuan_ze1 =(1417, 405)
di_er_guan_ka_xuan_ze2 =(1164, 399)
di_er_guan_ka_xuan_ze11 =(1104, 402)
di_er_guan_ka_xuan_ze12 =(1349, 399)
                         
di_san_guan_ka_xuan_ze1 =(1045, 415)
di_san_guan_ka_xuan_ze2 =(1281, 415)
di_san_guan_ka_xuan_ze3 =(1456, 415)
boss_guan_ka_xuan_ze=(1244, 212)
tong_guan_jiang_li_1 =(1409, 298)
tong_guan_jiang_li_2 =(1208, 583)
tong_guan_jiang_li_3 =(1652, 605)
tong_guan_jiang_li_wan_cheng_an_niu =(1413, 480)
xuan_shang_wan_cheng_an_niu=(1375, 669)

# print(g.position())
# g.moveTo(liang_ge_mu_biao_2)
def shi_zhan_ji_neng():
    print('释放技能1开始')
    g.click(ji_neng_1)
    time.sleep(2)
    g.click(liang_ge_mu_biao_2)
    time.sleep(2)
    g.click(jiu_xu)
    print('释放技能1结束')
    
def bao_zang_zuan_ze_fun():
    print('宝藏选择开始')
    g.click(bao_zang_xuan_ze)
    time.sleep(1)
    g.click(huo_qu_bao_zang_an_niu)
    time.sleep(3)
    print('宝藏选择结束')


def zhan_dou(times=2):
    print('战斗'+str(times)+'次开始')
    g.click(deng_cheng_an_niu)
    time.sleep(10)
    for i in range(times):
        print('第'+str(i)+'战斗开始')
        shi_zhan_ji_neng()
        time.sleep(20)
    print('战斗'+str(times)+'次结束')

def guan_ka_1():
    print('关卡1开始')
    g.click(di_yi_guan_ka_xuan_ze)
    time.sleep(0.5)
    g.click(guan_ka_kai_shi)
    time.sleep(15)
    
    zhan_dou(3)
    
    print('关卡1结束')
    pass

def guan_ka_2():
    print('关卡2开始')
    g.click(di_er_guan_ka_xuan_ze1)
    time.sleep(0.5)
    g.click(di_er_guan_ka_xuan_ze2)
    time.sleep(1)
    g.click(di_er_guan_ka_xuan_ze11)
    time.sleep(0.5)
    g.click(di_er_guan_ka_xuan_ze12)
    time.sleep(0.5)
    g.click(guan_ka_kai_shi)
    time.sleep(15)
    
    zhan_dou(3)
    print('关卡2结束')
    pass

def guan_ka_3():
    print('关卡3开始')
    g.click(di_san_guan_ka_xuan_ze1)
    g.sleep(1)
    g.click(di_san_guan_ka_xuan_ze2)
    g.sleep(1)
    g.click(di_san_guan_ka_xuan_ze3)
    g.sleep(1)
    g.click(guan_ka_kai_shi)
    time.sleep(15)
    
    zhan_dou(3)
    print('关卡3结束')
    pass

def boos_guan_ka():
    print('boss关卡开始')
    g.click(boss_guan_ka_xuan_ze)
    g.sleep(1)
    
    g.click(guan_ka_kai_shi)
    time.sleep(15)
    
    zhan_dou(4)
    print('boss关卡结束')
    pass
g.moveTo(liang_ge_mu_biao_2)

while True:
    # break
    print('开始悬赏')
    g.click(kai_shi_xuan_ze)
    time.sleep(5)
    g.click(xuan_ze_dui_wu)
    time.sleep(5)
    
    guan_ka_1()
    
    g.click()
    time.sleep(10)
    
    bao_zang_zuan_ze_fun()
    time.sleep(3)
    
    guan_ka_2()
    
    g.click()
    time.sleep(10)
    
    bao_zang_zuan_ze_fun()
    time.sleep(3)
    
    guan_ka_3()
    
    g.click()
    time.sleep(10)
    
    bao_zang_zuan_ze_fun()
    time.sleep(3)
    
    
    boos_guan_ka()

    print('boss点击屏幕')
    g.click()
    time.sleep(25)
    print('开始通过宝藏选择')
    g.click(tong_guan_jiang_li_1)
    time.sleep(1)
    g.click(tong_guan_jiang_li_2)
    time.sleep(1)
    g.click(tong_guan_jiang_li_3)
    time.sleep(1)
    print('通关宝藏选择结束')
    g.click(tong_guan_jiang_li_wan_cheng_an_niu)
    print('通关按钮')
    time.sleep(10)
    g.click(xuan_shang_wan_cheng_an_niu)
    print('悬赏完成')
    time.sleep(15)
