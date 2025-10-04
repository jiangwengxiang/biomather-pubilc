import tkinter as tk
from tkinter import ttk
import random
import time

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("理学王者 - 登录")
        self.root.geometry("600x400")
        self.root.resizable(True, True)
        
        # 设置主题
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TButton", font=(("Micsoft Yahei UI"), 12), padding=5)
        self.style.configure("TLabel", font=(("Micsoft Yahei UI"), 12), background="#f0f0f0")
        self.style.configure("Title.TLabel", font=(("Micsoft Yahei UI"), 24, "bold"))
        
        # 创建主框架
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # 标题
        title_label = ttk.Label(
            self.main_frame,
            text="理学王者",
            style="Title.TLabel"
        )
        title_label.pack(pady=50)
        
        # 功能选择按钮
        btn_frame = ttk.Frame(self.main_frame)
        btn_frame.pack(pady=20)
        
        function_buttons = [
            ("数学计算训练", self.start_math_trainer),
            ("化学计算", self.start_chemistry_computing)
        ]
        
        for text, command in function_buttons:
            btn = ttk.Button(
                btn_frame,
                text=text,
                width=20,
                command=command
            )
            btn.pack(pady=10, fill=tk.X)
        
        # 退出按钮
        exit_btn = ttk.Button(
            self.main_frame,
            text="退出",
            command=self.root.destroy
        )
        exit_btn.pack(pady=20)
    
    def start_math_trainer(self):
        """启动数学计算训练应用"""
        self.root.destroy()
        root = tk.Tk()
        app = MathTrainerApp(root)
        root.mainloop()
        
    def start_chemistry_computing(self):
        """启动化学计算应用"""
        self.root.destroy()
        root = tk.Tk()
        app = ChemistryComputingApp(root)
        root.mainloop()

class MathTrainerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("理学王者 - 数学计算训练")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # 设置主题
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TButton", font=(("Micsoft Yahei UI"), 12), padding=5)
        self.style.configure("TLabel", font=(("Micsoft Yahei UI"), 12), background="#f0f0f0")
        self.style.configure("Title.TLabel", font=(("Micsoft Yahei UI"), 14, "bold"))
        
        # 初始化变量
        self.current_frame = None
        self.training_mode = ""
        self.question_count = 10
        self.questions = []
        self.current_question = 0
        self.score = 0
        self.start_time = 0
        self.timer_id = None
        
        # 创建主菜单
        self.create_main_menu()
    
    def create_main_menu(self):
        """创建主菜单界面"""
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = ttk.Frame(self.root)
        self.current_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # 标题
        title_label = ttk.Label(
            self.current_frame,
            text="数学计算训练大师",
            style="Title.TLabel"
        )
        title_label.pack(pady=20)
        
        # 描述
        desc_label = ttk.Label(
            self.current_frame,
            text="选择训练模式",
            font=(("Arial"), 14)
        )
        desc_label.pack(pady=10)
        
        # 模式选择按钮
        btn_frame = ttk.Frame(self.current_frame)
        btn_frame.pack(pady=20)
        
        modes = [
            ("自由训练", self.start_free_training),
            ("考试模式", self.start_exam_mode),
            ("几何计算", self.start_geometry_calculation)
        ]
        
        for text, command in modes:
            btn = ttk.Button(
                btn_frame,
                text=text,
                width=15,
                command=command
            )
            btn.pack(pady=10, fill=tk.X)
        
        # 返回按钮
        back_btn = ttk.Button(
            self.current_frame,
            text="返回主功能菜单",
            command=self.return_to_main_menu
        )
        back_btn.pack(pady=20)
        
    def start_free_training(self):
        """开始自由训练"""
        self.training_mode = "free"
        self.show_question_count_selection()
        
    def start_exam_mode(self):
        """开始考试模式"""
        self.training_mode = "exam"
        self.show_question_count_selection()
        
    def show_question_count_selection(self):
        """显示题目数量选择界面"""
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = ttk.Frame(self.root)
        self.current_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        title_label = ttk.Label(
            self.current_frame,
            text="选择题目数量",
            style="Title.TLabel"
        )
        title_label.pack(pady=20)
        
        # 数量选择按钮
        btn_frame = ttk.Frame(self.current_frame)
        btn_frame.pack(pady=20)
        
        counts = [10, 20, 30, 50, 100]
        
        for count in counts:
            btn = ttk.Button(
                btn_frame,
                text=f"{count}题",
                width=10,
                command=lambda c=count: self.start_training(c)
            )
            btn.pack(pady=5, fill=tk.X)
        
        # 返回按钮
        back_btn = ttk.Button(
            self.current_frame,
            text="返回",
            command=self.create_main_menu
        )
        back_btn.pack(pady=20)
        
    def start_training(self, question_count):
        """开始训练"""
        self.question_count = question_count
        self.questions = []
        self.current_question = 0
        self.score = 0
        self.start_time = time.time()
        
        # 生成题目
        self.generate_questions()
        
        # 显示第一题
        self.show_question()
        
        # 如果是考试模式，开始计时
        if self.training_mode == "exam":
            self.update_timer()
            
    def generate_questions(self):
        """生成数学题目"""
        for _ in range(self.question_count):
            # 随机选择运算符
            operation = random.choice(["+", "-", "*", "/"])
            
            # 根据运算符生成合适范围的数字
            if operation == "+":
                num1 = random.randint(1, 100)
                num2 = random.randint(1, 100)
                answer = num1 + num2
            elif operation == "-":
                num1 = random.randint(1, 100)
                num2 = random.randint(1, num1)  # 确保结果为正
                answer = num1 - num2
            elif operation == "*":
                num1 = random.randint(1, 20)
                num2 = random.randint(1, 20)
                answer = num1 * num2
            else:  # division
                # 确保结果为整数
                answer = random.randint(1, 20)
                num2 = random.randint(1, 10)
                num1 = answer * num2
            
            # 存储题目和答案
            self.questions.append({
                "question": f"{num1} {operation} {num2} = ?",
                "answer": answer
            })
            
    def show_question(self):
        """显示当前题目"""
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = ttk.Frame(self.root)
        self.current_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # 显示进度
        progress_label = ttk.Label(
            self.current_frame,
            text=f"第 {self.current_question + 1}/{self.question_count} 题",
            font=(("Arial"), 12)
        )
        progress_label.pack(pady=10)
        
        # 如果是考试模式，显示计时器
        if self.training_mode == "exam":
            self.timer_label = ttk.Label(
                self.current_frame,
                text="00:00",
                font=(("Arial"), 14)
            )
            self.timer_label.pack(pady=10)
        
        # 显示题目
        question_label = ttk.Label(
            self.current_frame,
            text=self.questions[self.current_question]["question"],
            font=(("Arial"), 18)
        )
        question_label.pack(pady=20)
        
        # 答案输入框
        answer_frame = ttk.Frame(self.current_frame)
        answer_frame.pack(pady=20)
        
        answer_label = ttk.Label(answer_frame, text="答案：")
        answer_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        self.answer_entry = ttk.Entry(answer_frame, width=20)
        self.answer_entry.grid(row=0, column=1, padx=10, pady=10)
        self.answer_entry.focus()
        
        # 提交按钮
        submit_btn = ttk.Button(
            self.current_frame,
            text="提交",
            command=self.check_answer
        )
        submit_btn.pack(pady=20)
        
        # 绑定回车键提交
        self.current_frame.bind("<Return>", lambda event: self.check_answer())
        
    def check_answer(self):
        """检查答案是否正确"""
        try:
            user_answer = int(self.answer_entry.get().strip())
        except ValueError:
            # 显示错误消息
            error_label = ttk.Label(
                self.current_frame,
                text="请输入有效的数字！",
                foreground="red"
            )
            error_label.pack(pady=10)
            return
        
        correct_answer = self.questions[self.current_question]["answer"]
        
        # 检查答案
        if user_answer == correct_answer:
            self.score += 1
            result_text = "正确！"
            result_color = "green"
        else:
            result_text = f"错误！正确答案是 {correct_answer}"
            result_color = "red"
        
        # 显示结果
        result_label = ttk.Label(
            self.current_frame,
            text=result_text,
            foreground=result_color,
            font=(("Arial"), 14)
        )
        result_label.pack(pady=10)
        
        # 延迟后进入下一题或显示结果
        self.current_frame.after(1000, self.next_question)
        
    def next_question(self):
        """进入下一题或显示结果"""
        self.current_question += 1
        
        if self.current_question < self.question_count:
            # 显示下一题
            self.show_question()
        else:
            # 显示结果
            self.show_result()
            
    def show_result(self):
        """显示训练结果"""
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = ttk.Frame(self.root)
        self.current_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # 停止计时器
        if self.training_mode == "exam" and self.timer_id:
            self.root.after_cancel(self.timer_id)
        
        # 计算用时
        elapsed_time = time.time() - self.start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        
        # 显示结果
        title_label = ttk.Label(
            self.current_frame,
            text="训练完成！",
            style="Title.TLabel"
        )
        title_label.pack(pady=20)
        
        result_text = f"总题数：{self.question_count}\n"
        result_text += f"答对题数：{self.score}\n"
        result_text += f"正确率：{(self.score / self.question_count * 100):.1f}%\n"
        result_text += f"用时：{minutes}分{seconds}秒"
        
        result_label = ttk.Label(
            self.current_frame,
            text=result_text,
            font=(("Arial"), 14),
            justify=tk.LEFT
        )
        result_label.pack(pady=20, anchor=tk.CENTER)
        
        # 按钮
        btn_frame = ttk.Frame(self.current_frame)
        btn_frame.pack(pady=20)
        
        restart_btn = ttk.Button(
            btn_frame,
            text="重新开始",
            command=lambda: self.start_training(self.question_count)
        )
        restart_btn.pack(side=tk.LEFT, padx=10)
        
        menu_btn = ttk.Button(
            btn_frame,
            text="返回菜单",
            command=self.create_main_menu
        )
        menu_btn.pack(side=tk.LEFT, padx=10)
        
        back_btn = ttk.Button(
            btn_frame,
            text="返回主功能菜单",
            command=self.return_to_main_menu
        )
        back_btn.pack(side=tk.LEFT, padx=10)
        
    def update_timer(self):
        """更新计时器"""
        elapsed_time = time.time() - self.start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        
        # 更新标签
        if hasattr(self, 'timer_label'):
            self.timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
        
        # 继续计时
        self.timer_id = self.root.after(1000, self.update_timer)
        
    def start_geometry_calculation(self):
        """开始几何计算"""
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = ttk.Frame(self.root)
        self.current_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        title_label = ttk.Label(
            self.current_frame,
            text="几何计算",
            style="Title.TLabel"
        )
        title_label.pack(pady=20)
        
        # 几何计算选项
        btn_frame = ttk.Frame(self.current_frame)
        btn_frame.pack(pady=20)
        
        geometry_options = [
            ("计算圆面积", self.calculate_circle_area),
            ("计算矩形面积", self.calculate_rectangle_area),
            ("计算梯形面积", self.calculate_trapezoid_area),
            ("计算球体积", self.calculate_ball_volume),
            ("计算棱柱体积", self.calculate_prism_volume)
        ]
        
        for text, command in geometry_options:
            btn = ttk.Button(
                btn_frame,
                text=text,
                width=15,
                command=command
            )
            btn.pack(pady=10, fill=tk.X)
        
        # 返回按钮
        back_btn = ttk.Button(
            self.current_frame,
            text="返回",
            command=self.create_main_menu
        )
        back_btn.pack(pady=20)
        
    def create_input_dialog(self, title, params, calculate_func):
        """创建输入对话框"""
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = ttk.Frame(self.root)
        self.current_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        title_label = ttk.Label(
            self.current_frame,
            text=title,
            style="Title.TLabel"
        )
        title_label.pack(pady=20)
        
        # 输入框
        input_frame = ttk.Frame(self.current_frame)
        input_frame.pack(pady=20)
        
        entries = []
        
        for i, (label_text, default_value) in enumerate(params):
            label = ttk.Label(input_frame, text=f"{label_text}：")
            label.grid(row=i, column=0, padx=10, pady=10, sticky="w")
            
            entry = ttk.Entry(input_frame, width=20)
            entry.grid(row=i, column=1, padx=10, pady=10)
            entry.insert(0, str(default_value))
            entries.append(entry)
            
        # 结果显示
        self.result_var = tk.StringVar()
        result_label = ttk.Label(
            self.current_frame,
            textvariable=self.result_var,
            font=(("Arial"), 14)
        )
        result_label.pack(pady=20)
        
        # 计算按钮
        calc_btn = ttk.Button(
            self.current_frame,
            text="计算",
            command=lambda: self.perform_calculation(entries, calculate_func)
        )
        calc_btn.pack(pady=10)
        
        # 返回按钮
        back_btn = ttk.Button(
            self.current_frame,
            text="返回",
            command=self.start_geometry_calculation
        )
        back_btn.pack(pady=20)
        
    def perform_calculation(self, entries, calculate_func):
        """执行计算"""
        try:
            # 获取输入值
            values = []
            for entry in entries:
                value = float(entry.get().strip())
                values.append(value)
            
            # 执行计算
            result = calculate_func(*values)
            
            # 显示结果
            self.result_var.set(f"计算结果：{result}")
            
        except ValueError:
            self.result_var.set("请输入有效的数字！")
        except Exception as e:
            self.result_var.set(f"计算错误: {str(e)}")
    
    def squ_cir(self, r, pi):
        """计算圆面积"""
        if pi == 0:
            return f"{r}²π"
        else:
            area = 3.1415926535 * r * r
            return f"{area:.{pi}f}"
    
    def squ_square(self, a, b):
        """计算矩形面积"""
        return f"{a * b}"
    
    def squ_trapezoid(self, a, b, h):
        """计算梯形面积"""
        return f"{(a + b) * h / 2}"
    
    def vol_ball(self, r, pi):
        """计算球体积"""
        if pi == 0:
            return f"(4/3){r}³π"
        else:
            volume = 4/3 * 3.1415926535 * r * r * r
            return f"{volume:.{pi}f}"
    
    def vol_prism(self, s, h):
        """计算棱柱体积"""
        return f"{s * h}"
    
    def return_to_main_menu(self):
        """返回主功能菜单"""
        self.root.destroy()
        root = tk.Tk()
        app = LoginApp(root)
        root.mainloop()

class ChemistryComputingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("理学王者 - 化学计算")
        self.root.geometry("1080x600")
        self.root.resizable(True, True)
        
        # 设置主题
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TButton", font=(("Micsoft Yahei UI"), 12), padding=5)
        self.style.configure("TLabel", font=(("Micsoft Yahei UI"), 12), background="#f0f0f0")
        self.style.configure("Title.TLabel", font=(("Micsoft Yahei UI"), 14, "bold"))
        
        # 初始化变量
        self.current_frame = None
        self.training_mode = ""
        self.question_count = 10
        self.questions = []
        self.current_question = 0
        self.score = 0
        self.start_time = 0
        
        # 化学元素数据列表
        self.list_chemistry_element = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne","Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca"]
        self.list_chemistry_element_chinese = ["氢","氦","锂"]
        self.list_chemistry_element_relative_atomic_mass = [1.01, 4.00, 6.94, 9.01]
        self.list_chemistry_element_relative_atomic_mass_int = [1, 4, 7, 9, 11, 12, 14, 16, 19, 20, 23, 24, 27, 28, 31, 32, 35, 40, 39, 40]
        
        self.create_main_menu()
    
    def create_main_menu(self):
        """创建主菜单界面"""
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = ttk.Frame(self.root)
        self.current_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        title_label = ttk.Label(
            self.current_frame,
            text="化学计算大师", 
            style="Title.TLabel"
        )
        title_label.pack(pady=20)
        
        desc_label = ttk.Label(
            self.current_frame,
            text="在这里，你将练成化学计算大师！",
            font=(("Arial"), 14)
        )
        desc_label.pack(pady=10)
        
        # 创建计算功能按钮
        btn_frame = ttk.Frame(self.current_frame)
        btn_frame.pack(pady=20)
        
        chemistry_options = [
            ("相对分子质量计算", self.calculate_molecular_mass),
            ("克与摩尔转换", self.gram_mol_conversion),
            ("元素信息查询", self.query_element_info),
            ("化学训练模式", self.start_chemistry_training)
        ]
        
        for text, command in chemistry_options:
            btn = ttk.Button(
                btn_frame,
                text=text,
                width=20,
                command=command
            )
            btn.pack(pady=10, fill=tk.X)
        
        # 返回按钮
        back_btn = ttk.Button(
            self.current_frame,
            text="返回主功能菜单",
            command=self.return_to_main_menu
        )
        back_btn.pack(pady=20, fill=tk.X)
        
    def return_to_main_menu(self):
        """返回主功能菜单"""
        self.root.destroy()
        root = tk.Tk()
        app = LoginApp(root)
        root.mainloop()
        
    def calculate_molecular_mass(self):
        """相对分子质量计算界面"""
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = ttk.Frame(self.root)
        self.current_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        title_label = ttk.Label(
            self.current_frame,
            text="相对分子质量计算",
            style="Title.TLabel"
        )
        title_label.pack(pady=20)
        
        # 创建输入框架
        input_frame = ttk.Frame(self.current_frame)
        input_frame.pack(pady=20)
        
        formula_label = ttk.Label(input_frame, text="请输入化学式：")
        formula_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        formula_entry = ttk.Entry(input_frame, width=30)
        formula_entry.grid(row=0, column=1, padx=10, pady=10)
        
        # 结果显示
        result_var = tk.StringVar()
        result_label = ttk.Label(
            self.current_frame,
            textvariable=result_var,
            font=(("Arial"), 12)
        )
        result_label.pack(pady=20)
        
        def calculate():
            formula = formula_entry.get().strip()
            if not formula:
                result_var.set("请输入有效的化学式")
                return
            
            try:
                # 使用类内部方法计算相对分子质量
                mass, _ = self.parse_chemical_formula(formula)
                if isinstance(mass, str) and "错误" in mass:
                    result_var.set(mass)
                else:
                    result_var.set(f"{formula} 的相对分子质量为: {mass}")
            except Exception as e:
                result_var.set(f"计算错误: {str(e)}")
        
        # 计算按钮
        calc_btn = ttk.Button(
            self.current_frame,
            text="计算",
            command=calculate
        )
        calc_btn.pack(pady=10)
        
        # 返回菜单按钮
        back_btn = ttk.Button(
            self.current_frame,
            text="返回菜单",
            command=self.create_main_menu
        )
        back_btn.pack(pady=20)
        
    def gram_mol_conversion(self):
        """克与摩尔转换界面"""
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = ttk.Frame(self.root)
        self.current_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        title_label = ttk.Label(
            self.current_frame,
            text="克与摩尔转换",
            style="Title.TLabel"
        )
        title_label.pack(pady=20)
        
        # 创建输入框架
        input_frame = ttk.Frame(self.current_frame)
        input_frame.pack(pady=20)
        
        # 元素选择
        element_label = ttk.Label(input_frame, text="选择元素：")
        element_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        element_var = tk.StringVar(value=self.list_chemistry_element[0])
        element_menu = ttk.Combobox(
            input_frame,
            textvariable=element_var,
            values=self.list_chemistry_element,
            width=10
        )
        element_menu.grid(row=0, column=1, padx=10, pady=10)
        
        # 质量输入
        mass_label = ttk.Label(input_frame, text="克数：")
        mass_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        
        mass_entry = ttk.Entry(input_frame, width=20)
        mass_entry.grid(row=1, column=1, padx=10, pady=10)
        
        # 结果显示
        result_var = tk.StringVar()
        result_label = ttk.Label(
            self.current_frame,
            textvariable=result_var,
            font=(("Arial"), 12)
        )
        result_label.pack(pady=20)
        
        def convert_gram_to_mol():
            element = element_var.get()
            gram_text = mass_entry.get().strip()
            
            if not gram_text:
                result_var.set("请输入克数")
                return
            
            result = self.math_gram_to_mol_int(gram_text, element)
            if isinstance(result, str):
                result_var.set(result)
            else:
                atomic_mass = self.get_chemistry_element_relative_atomic_mass_int(element)
                result_var.set(f"{gram_text}克 {element} (原子量: {atomic_mass}) 等于 {result:.4f} 摩尔")
        
        def convert_mol_to_gram():
            element = element_var.get()
            mol_text = mass_entry.get().strip()
            
            if not mol_text:
                result_var.set("请输入摩尔数")
                return
            
            result = self.math_mol_to_gram_int(mol_text, element)
            if isinstance(result, str):
                result_var.set(result)
            else:
                atomic_mass = self.get_chemistry_element_relative_atomic_mass_int(element)
                result_var.set(f"{mol_text}摩尔 {element} (原子量: {atomic_mass}) 等于 {result} 克")
        
        # 转换按钮
        btn_frame = ttk.Frame(self.current_frame)
        btn_frame.pack(pady=10)
        
        gram_to_mol_btn = ttk.Button(
            btn_frame,
            text="克 -> 摩尔",
            command=convert_gram_to_mol
        )
        gram_to_mol_btn.pack(side=tk.LEFT, padx=10)
        
        mol_to_gram_btn = ttk.Button(
            btn_frame,
            text="摩尔 -> 克",
            command=convert_mol_to_gram
        )
        mol_to_gram_btn.pack(side=tk.LEFT, padx=10)
        
        # 返回菜单按钮
        back_btn = ttk.Button(
            self.current_frame,
            text="返回菜单",
            command=self.create_main_menu
        )
        back_btn.pack(pady=20)
        
    def query_element_info(self):
        """元素信息查询界面"""
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = ttk.Frame(self.root)
        self.current_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        title_label = ttk.Label(
            self.current_frame,
            text="元素信息查询",
            style="Title.TLabel"
        )
        title_label.pack(pady=20)
        
        # 创建输入框架
        input_frame = ttk.Frame(self.current_frame)
        input_frame.pack(pady=20)
        
        # 元素选择
        element_label = ttk.Label(input_frame, text="选择元素：")
        element_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        element_var = tk.StringVar(value=self.list_chemistry_element[0])
        element_menu = ttk.Combobox(
            input_frame,
            textvariable=element_var,
            values=self.list_chemistry_element,
            width=10
        )
        element_menu.grid(row=0, column=1, padx=10, pady=10)
        
        # 结果显示
        result_text = tk.Text(self.current_frame, height=10, width=50)
        result_text.pack(pady=20)
        result_text.config(state=tk.DISABLED)
        
        def query():
            element = element_var.get()
            
            # 启用文本框并清空内容
            result_text.config(state=tk.NORMAL)
            result_text.delete(1.0, tk.END)
            
            # 获取元素信息
            atomic_number = self.get_chemistry_element_number(element)
            atomic_mass = self.get_chemistry_element_relative_atomic_mass(element)
            atomic_mass_int = self.get_chemistry_element_relative_atomic_mass_int(element)
            
            # 显示结果
            result_text.insert(tk.END, f"元素符号: {element}\n")
            result_text.insert(tk.END, f"原子序数: {atomic_number}\n")
            result_text.insert(tk.END, f"相对原子质量(精确): {atomic_mass}\n")
            result_text.insert(tk.END, f"相对原子质量(整数): {atomic_mass_int}\n")
            
            # 禁用文本框以防止编辑
            result_text.config(state=tk.DISABLED)
        
        # 查询按钮
        query_btn = ttk.Button(
            self.current_frame,
            text="查询",
            command=query
        )
        query_btn.pack(pady=10)
        
        # 返回菜单按钮
        back_btn = ttk.Button(
            self.current_frame,
            text="返回菜单",
            command=self.create_main_menu
        )
        back_btn.pack(pady=20)
        
    def start_chemistry_training(self):
        """化学训练模式界面"""
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = ttk.Frame(self.root)
        self.current_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        title_label = ttk.Label(
            self.current_frame,
            text="化学训练模式",
            style="Title.TLabel"
        )
        title_label.pack(pady=20)
        
        desc_label = ttk.Label(
            self.current_frame,
            text="选择训练类型:",
            font=(("Arial"), 12)
        )
        desc_label.pack(pady=10)
        
        # 创建训练选项按钮
        btn_frame = ttk.Frame(self.current_frame)
        btn_frame.pack(pady=20)
        
        training_options = [
            ("相对分子质量计算训练", self.molecular_mass_training),
            ("克与摩尔转换训练", self.gram_mol_training),
            ("元素信息记忆训练", self.element_memory_training)
        ]
        
        for text, command in training_options:
            btn = ttk.Button(
                btn_frame,
                text=text,
                width=25,
                command=command
            )
            btn.pack(pady=10, fill=tk.X)
        
        # 返回菜单按钮
        back_btn = ttk.Button(
            self.current_frame,
            text="返回菜单",
            command=self.create_main_menu
        )
        back_btn.pack(pady=20)
        
    def molecular_mass_training(self):
        """相对分子质量计算训练"""
        # 简化实现，实际可以参考MathTrainerApp的训练模式
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = ttk.Frame(self.root)
        self.current_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        title_label = ttk.Label(
            self.current_frame,
            text="相对分子质量计算训练",
            style="Title.TLabel"
        )
        title_label.pack(pady=20)
        
        # 简单的实现，可以扩展为完整的训练模式
        desc_label = ttk.Label(
            self.current_frame,
            text="此功能正在开发中，敬请期待！",
            font=(("Arial"), 12)
        )
        desc_label.pack(pady=20)
        
        # 返回训练菜单按钮
        back_btn = ttk.Button(
            self.current_frame,
            text="返回训练菜单",
            command=self.start_chemistry_training
        )
        back_btn.pack(pady=20)
        
    def gram_mol_training(self):
        """克与摩尔转换训练"""
        # 简化实现，实际可以参考MathTrainerApp的训练模式
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = ttk.Frame(self.root)
        self.current_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        title_label = ttk.Label(
            self.current_frame,
            text="克与摩尔转换训练",
            style="Title.TLabel"
        )
        title_label.pack(pady=20)
        
        # 简单的实现，可以扩展为完整的训练模式
        desc_label = ttk.Label(
            self.current_frame,
            text="此功能正在开发中，敬请期待！",
            font=(("Arial"), 12)
        )
        desc_label.pack(pady=20)
        
        # 返回训练菜单按钮
        back_btn = ttk.Button(
            self.current_frame,
            text="返回训练菜单",
            command=self.start_chemistry_training
        )
        back_btn.pack(pady=20)
        
    def element_memory_training(self):
        """元素信息记忆训练"""
        # 简化实现，实际可以参考MathTrainerApp的训练模式
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = ttk.Frame(self.root)
        self.current_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        title_label = ttk.Label(
            self.current_frame,
            text="元素信息记忆训练",
            style="Title.TLabel"
        )
        title_label.pack(pady=20)
        
        # 简单的实现，可以扩展为完整的训练模式
        desc_label = ttk.Label(
            self.current_frame,
            text="此功能正在开发中，敬请期待！",
            font=(("Arial"), 12)
        )
        desc_label.pack(pady=20)
        
        # 返回训练菜单按钮
        back_btn = ttk.Button(
            self.current_frame,
            text="返回训练菜单",
            command=self.start_chemistry_training
        )
        back_btn.pack(pady=20)

    # ==========化学计算方法=================
    def get_chemistry_element_number(self, element):
        """
        此方法用于获取化学元素的原子序数(元素符号)
        输入：元素符号
        输出：原子序数
        """
        if element in self.list_chemistry_element:
            chemistry_element_number = int(self.list_chemistry_element.index(element)) + 1
            return chemistry_element_number
        else:
            return "元素不存在"
            
    def get_chemistry_element_number_chinese(self, element_chinese):    
        """
        此方法用于获取化学元素的原子序数(元素中文)
        输入：元素中文
        输出：原子序数
        """
        if element_chinese in self.list_chemistry_element_chinese:
            chemistry_element_number = int(self.list_chemistry_element_chinese.index(element_chinese)) + 1
            return chemistry_element_number
        else:
            return "元素不存在"
    
    def get_chemistry_element_relative_atomic_mass(self, element):
        """
        此方法用于获取化学元素的相对原子质量(元素符号)
        输入：元素符号
        输出：相对原子质量
        """
        if element in self.list_chemistry_element:
            chemistry_element_relative_atomic_mass = self.list_chemistry_element_relative_atomic_mass[self.list_chemistry_element.index(element)]
            return chemistry_element_relative_atomic_mass
        else:
            return "元素不存在"
    
    def get_chemistry_element_relative_atomic_mass_int(self, element):
        """
        此方法用于获取化学元素的相对原子质量(元素符号)
        输入：元素符号
        输出：相对原子质量(整数)
        """
        if element in self.list_chemistry_element:
            chemistry_element_relative_atomic_mass = self.list_chemistry_element_relative_atomic_mass_int[self.list_chemistry_element.index(element)]
            return chemistry_element_relative_atomic_mass
        else:
            return "元素不存在"
    
    def math_gram_to_mol_int(self, gram, element):
        """
        此方法用于将克转换为摩尔
        注意：此处的元素使用的是整数型的相对原子质量
        输入：克，元素符号
        输出：摩尔
        """
        atomic_mass = self.get_chemistry_element_relative_atomic_mass_int(element)
        if atomic_mass == "元素不存在":
            return "元素不存在"
        else:
            atomic_mass = int(atomic_mass)
            try:
                gram = int(gram)
                mol = float(gram/atomic_mass)
                return mol
            except ValueError:
                return "错误: 请输入有效的数字"
    
    def math_mol_to_gram_int(self, mol, element):
        """
        此方法用于将摩尔转换为克
        注意：此处的元素使用的是整数型的相对原子质量
        输入：摩尔，元素符号
        输出：克
        """
        atomic_mass = self.get_chemistry_element_relative_atomic_mass_int(element)
        if atomic_mass == "元素不存在":
            return "元素不存在"
        else:
            atomic_mass = int(atomic_mass)
        try:
            mol = int(mol)
            gram = float(mol*atomic_mass)
            return gram
        except ValueError:
            return "错误: 请输入有效的数字"
    
    def parse_chemical_formula(self, formule, start_index=0):
        """
        解析化学式并计算相对分子质量（支持小括号）
        """
        total_mass = 0
        i = start_index
        
        while i < len(formule):
            if formule[i] == '(':
                # 递归处理括号内的内容
                bracket_result, new_index = self.parse_chemical_formula(formule, i + 1)
                total_mass += bracket_result
                i = new_index
                
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
                if i + 1 < len(formule) and formule[i:i+2] in self.list_chemistry_element:
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
                atomic_mass = self.get_chemistry_element_relative_atomic_mass_int(element)
                if atomic_mass != "元素不存在":
                    total_mass += atomic_mass * count
                else:
                    return f"错误: 元素 {element} 不存在", i
                
            else:
                i += 1
        
        return total_mass, i
    
    def math_relative_molecular_mass(self, formule):
        """
        此方法用于计算相对分子质量
        输入：化学式
        输出：相对分子质量
        """
        result, _ = self.parse_chemical_formula(formule)
        return result
    
    def gram_to_mol(self, gram, molar_mass):
        """
        此方法用于将克转换为摩尔
        输入：克数，摩尔质量
        输出：摩尔数
        """
        try:
            gram = float(gram)
            molar_mass = float(molar_mass)
            if molar_mass == 0:
                return "错误: 摩尔质量不能为0"
            return gram / molar_mass
        except ValueError:
            return "错误: 请输入有效的数字"
    
    def mol_to_gram(self, mol, molar_mass):
        """
        此方法用于将摩尔转换为克
        输入：摩尔数，摩尔质量
        输出：克数
        """
        try:
            mol = float(mol)
            molar_mass = float(molar_mass)
            return mol * molar_mass
        except ValueError:
            return "错误: 请输入有效的数字"

# 保留原始的外部函数以便兼容性
# 这些函数将调用类内部的方法
def math_relative_molecular_mass(formule):
    """
    此函数用于计算相对分子质量
    输入：化学式
    输出：相对分子质量
    """
    temp_root = tk.Tk()
    temp_root.withdraw()  # 隐藏窗口
    temp_app = ChemistryComputingApp(temp_root)
    result, _ = temp_app.parse_chemical_formula(formule)
    temp_root.destroy()
    return result

# 为了兼容性，添加一个全局的parse_chemical_formula函数
def parse_chemical_formula(formule, start_index=0):
    """
    解析化学式并计算相对分子质量（支持小括号）
    """
    temp_root = tk.Tk()
    temp_root.withdraw()  # 隐藏窗口
    temp_app = ChemistryComputingApp(temp_root)
    result = temp_app.parse_chemical_formula(formule, start_index)
    temp_root.destroy()
    return result


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
