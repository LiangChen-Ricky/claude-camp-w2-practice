while True:
    num1 = input("请输入第一个数字（或 quit 退出）：").strip().lower()
    
    if num1 == "quit":
        print("👋 再见！")
        break
    
    try:
        num1 = float(num1)
    except ValueError:
        print("❌ 请输入有效数字")
        continue
    
    operator = input("请输入运算符（+ - * /）：").strip()
    
    try:
        num2 = float(input("请输入第二个数字：").strip())
        
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2   # ← 除以0会触发什么异常？
        else:
            print("❌ 不支持的运算符")
            continue
            
        print(f"结果：{result}")
        
    except ValueError:
        print("❌ 请输入有效数字")
    except ZeroDivisionError:
        print("❌ 不能除以零！")