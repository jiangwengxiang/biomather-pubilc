""" This is the chemistry computing functions
from verison is bate 0.2.0 deveioping bate
you need to know that this is only for test 
if you want to try our app,you should find the cpp file or html file 
Copyright (c) 2025 by jourious. All rights reserved.
we think that you should know that we do not provide this file as a service
请务必注意：请勿对其中的化学术语进行混淆
有关化学中相关术语的英中文对照，以及关于本文件中函数名，变量名的选择，详见此文件夹中的about-chemistry.md文件
"""

# these lists are using to store the chemistry date
list_chemistry_element = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne","Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca"]
list_chemistry_element_chinese = ["氢","氦","锂"]
list_chemistry_element_relative_atomic_mass = [1.01, 4.00, 6.94, 9.01]
list_chemistry_element_relative_atomic_mass_int = [1, 4, 7, 9, 11, 12, 14, 16, 19, 20, 23, 24, 27, 28, 31, 32, 35, 40, 39, 40]

def get_chemistry_element_number(element):
    """
    此函数用于获取化学元素的原子序数(元素符号)
    输入：元素符号
    输出：原子序数
    """
    if element in list_chemistry_element:
        chemistry_element_number = int(list_chemistry_element.index(element)) + 1
        return chemistry_element_number
    else:
        return "元素不存在"
def get_chemistry_element_number_chinese(element_chinese):
    """
    此函数用于获取化学元素的原子序数(元素中文)
    输入：元素中文
    输出：原子序数
    """
    if element_chinese in list_chemistry_element_chinese:
        chemistry_element_number = int(list_chemistry_element_chinese.index(element_chinese)) + 1
        return chemistry_element_number
    else:
        return "元素不存在"

def get_chemistry_element_relative_atomic_mass(element):
    """
    此函数用于获取化学元素的相对原子质量(元素符号)
    输入：元素符号
    输出：相对原子质量
    """
    if element in list_chemistry_element:
        chemistry_element_relative_atomic_mass = list_chemistry_element_relative_atomic_mass[list_chemistry_element.index(element)]
        return chemistry_element_relative_atomic_mass
    else:
        return "元素不存在"

def get_chemistry_element_relative_atomic_mass_int(element):
    """
    此函数用于获取化学元素的相对原子质量(元素符号)
    输入：元素符号
    输出：相对原子质量(整数)
    """
    if element in list_chemistry_element:
        chemistry_element_relative_atomic_mass = list_chemistry_element_relative_atomic_mass_int[list_chemistry_element.index(element)]
        return chemistry_element_relative_atomic_mass
    else:
        return "元素不存在"


def math_gram_to_mol_int(gram,element):
    """
    此函数用于将克转换为摩尔
    注意：此处的元素使用的是整数型的相对原子质量
    输入：克，元素符号
    输出：摩尔
    """
    atomic_mass = get_chemistry_element_relative_atomic_mass_int(element)
    if atomic_mass == "元素不存在":
        return "元素不存在"
    else:
        atomic_mass = int(atomic_mass)
        gram = int (gram)
        mol = float (gram/atomic_mass)
        return mol

def math_mol_to_gram_int(mol,element):
    """
    此函数用于将摩尔转换为克
    注意：此处的元素使用的是整数型的相对原子质量
    输入：摩尔，元素符号
    输出：克
    """
    atomic_mass = get_chemistry_element_relative_atomic_mass_int(element)
    if atomic_mass == "元素不存在":
        return "元素不存在"
    else:
        atomic_mass = int(atomic_mass)
        mol = int (mol)
        gram = float (mol*atomic_mass)
        return gram

def parse_chemical_formula(formule, start_index=0):
    """
    解析化学式并计算相对分子质量（支持小括号）
    """
    total_mass = 0
    i = start_index
    
    while i < len(formule):
        if formule[i] == '(':
            # 递归处理括号内的内容
            bracket_result, new_index = parse_chemical_formula(formule, i + 1)
            total_mass += bracket_result
            i = new_index
            
            # 检查括号后的数字倍数
            count = 1
            if i < len(formule) and formule[i].isdigit():
                num_str = ""
                while i < len(formule) and formule[i].isdigit():
                    num_str += formule[i]
                    i += 1
                count = int(num_str)
                total_mass += bracket_result * (count - 1)  # 已经加过一次，所以乘以(count-1)
            
        elif formule[i] == ')':
            # 返回括号内的计算结果和当前位置
            return total_mass, i + 1
            
        elif formule[i].isalpha():
            # 处理元素符号
            if i + 1 < len(formule) and formule[i:i+2] in list_chemistry_element:
                element = formule[i:i+2]
                i += 2
            else:
                element = formule[i]
                i += 1
            
            # 检查数字下标
            count = 1
            if i < len(formule) and formule[i].isdigit():
                num_str = ""
                while i < len(formule) and formule[i].isdigit():
                    num_str += formule[i]
                    i += 1
                count = int(num_str)
            
            # 获取原子质量
            atomic_mass = get_chemistry_element_relative_atomic_mass_int(element)
            if atomic_mass != "元素不存在":
                total_mass += atomic_mass * count
            else:
                return f"错误: 元素 {element} 不存在", i
                
        else:
            i += 1
    
    return total_mass, i

def math_relative_molecular_mass(formule):
    """
    此函数用于计算相对分子质量
    输入：化学式
    输出：相对分子质量
    """
    result, _ = parse_chemical_formula(formule)
    return result