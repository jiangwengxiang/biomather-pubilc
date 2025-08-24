""" This is the physics computing functions
from verison is bate 0.2.0 deveioping bate
you need to know that this is only for test 
if you want to try our app,you should find the cpp file or html file 
Copyright (c) 2025 by jourious. All rights reserved.
"""

"""we think that you should know that we do not provide this file as a service
请务必注意：此文件中的物理来自于高中物理，请勿对其中的物理量进行混淆：列如速度与速率等
本文件中使用的物理量的中英文对照及其命名详见次文件夹中的about-phy.md文件
"""

# the main promme is below
import math
import matplotlib 

def calculate_force_fonction01(mass, acceleration):
    """计算力的方式一:F=ma
    输入参数需为float类型，单位：kg和m/s^2
    输出参数为float类型，单位：N"""
    return mass * acceleration

def calculate_mass_fonction01(force, acceleration):
    """计算质量的方式一:m=F/a
    输入参数需为float类型，单位：N和m/s^2
    输出参数为float类型，单位：kg"""
    return force / acceleration

def calculate_acceleration_fonction01(mass, force):
    """计算加速度的方式一:a=F/m
    输入参数需为float类型，单位：N和kg
    输出参数为float类型，单位：m/s^2"""
    return force / mas

def calculate_acceleration_fonction01(time, velocity):
    """计算加速度的方式一:a=v/t
    输入参数需为float类型，单位：s和m/s
    输出参数为float类型，单位：m/s^2"""
    return velocity / time

def calculate_velocity_fonction02(acceleration, time, v0):
    """计算速度的方式二:v=v0+a*t
    输入参数需为float类型，单位：m/s^2和s
    输出参数为float类型，单位：m/s"""
    return acceleration * time + v0

