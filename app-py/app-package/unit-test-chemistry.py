from asyncio.queues import PriorityQueue


list_chemistry_element = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne","Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Fe"]
list_chemistry_element_chinese = ["氢","氦","锂"]
list_chemistry_element_relative_atomic_mass = [1.01, 4.00, 6.94, 9.01]
list_chemistry_element_relative_atomic_mass_int = [1, 4, 7, 9, 11, 12, 14, 16, 19, 20, 23, 24, 27, 28, 31, 32, 35, 40, 39, 40, 56]

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

def parse_chemical_formula(formule, start_index=0):
    """
    解析化学式并计算相对分子质量（支持括号）
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

        
if __name__ == "__main__":
    print("单测开始")
    print("H2O:", math_relative_molecular_mass("H2O"))
    print("CO2:", math_relative_molecular_mass("CO2"))
    print("NaCl:", math_relative_molecular_mass("NaCl"))
    print("H2SO4:", math_relative_molecular_mass("H2SO4"))
    print("CaCO3:", math_relative_molecular_mass("CaCO3"))
    print("Fe(OH)3:", math_relative_molecular_mass("Fe(OH)3"))
    print("Al2(SO4)3:", math_relative_molecular_mass("Al2(SO4)3"))


 