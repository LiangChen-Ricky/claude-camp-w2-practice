roster = []
while True:
    print("请选择操作：")
    print("1. 添加学员")
    print("2. 查询学员")
    print("3. 删除学员")
    print("4. 退出")
    choice = input("请输入选项（1-4）：").strip()
    if choice == "4":
        print("程序已退出")
        break
    elif choice == "1":
        name = input("请输入姓名：")
        email = input("请输入邮箱：")
        date = input("请输入加入日期：")
        student = {"姓名": name, "邮箱": email, "加入日期": date}
        roster.append(student)
        print("学员已添加！")
        
    elif choice == "2":
        if len(roster) == 0:
            print("目前没有学员")
        else:
            for student in roster:
                print(f"姓名：{student['姓名']}，邮箱：{student['邮箱']}，加入日期：{student['加入日期']}")
    elif choice == "3":
        name = input("请输入要删除的学员姓名：")
        found = False
        for student in roster:
            if student["姓名"] == name:
                roster.remove(student)
                print(f"{name} 已删除")
                found = True
                break
        if not found:
            print("找不到该学员")
    else:
        print("无效输入，请输入1-4")