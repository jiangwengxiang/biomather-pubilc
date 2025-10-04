""" This is the physics computing functions
from verison is bate 0.2.0 deveioping bate
you need to know that this is only for test 
if you want to try our app,you should find the cpp file or html file 
Copyright (c) 2025 by jourious. All rights reserved.
we think that you should know that we do not provide this file as a service
请务必注意：此文件中的物理来自于高中物理，请勿对其中的物理量进行混淆：列如速度与速率等
本文件中使用的物理量的中英文对照及其命名详见次文件夹中的about-phy.md文件
"""

# the main promme is below
import math
import matplotlib 
# 力学计算函数如下
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
    return force / mass

def calculate_acceleration_fonction02(time, velocity):
    """计算加速度的方式二:a=v/t
    输入参数需为float类型，单位：s和m/s
    输出参数为float类型，单位：m/s^2"""
    return velocity / time

def calculate_velocity_fonction02(acceleration, time, v0):
    """计算速度的方式一:v=v0+a*t
    输入参数需为float类型，单位：m/s^2和s
    输出参数为float类型，单位：m/s"""
    return acceleration * time + v0

# 电磁学计算函数如下
"""电磁学计算函数可能由于编者学识有限，存在问题时请及时指正"""
def calculate_voltage_fonction01(current, resistance):
    """计算电压的方式一:V=I*R(适用于纯电阻电路)
    输入参数需为float类型，单位：A和Ω
    输出参数为float类型，单位：V"""
    return current * resistance

def calculate_current_fonction01(voltage, resistance):
    """计算电流的方式一:I=V/R
    输入参数需为float类型，单位：V和Ω
    输出参数为float类型，单位：A"""
    return voltage / resistance

def calculate_resistance_fonction01(voltage, current):
    """计算电阻的方式一:R=V/I
    输入参数需为float类型，单位：V和A
    输出参数为float类型，单位：Ω"""
    return voltage / current

# 行星运动定律相关计算

def calculate_universal_gravitation_function(G,mass01,mass02,distance):
    """计算万有引力的方式一:F=G*m1*m2/r^2
    输入参数需为float类型，单位：m/s^2和kg
    输出参数为float类型，单位：N"""
    if G == "G" and mass01 == "m1" and mass02 == "m2" and distance == "r":
        return "G * m1 * m2 / r**2"
    else:
        s=type(G)
        if s == str:
            if type(mass01) == str and type(mass02) == str and type(distance) == float or type(distance) == int:
                return "G * m1 * m2"/"" + r**2
            else:
                if type(mass01) == str and type(mass02) == float or type(mass02) == int and type(distance) == float or type(distance) == int:
                    return G * mass01 * mass02 / distance**2
                else:
                    return "输入参数错误"
        
