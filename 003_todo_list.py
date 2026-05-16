import json
import sys
sys.stdout.reconfigure(encoding='utf-8')
def load_todos():
    try:
        with open("todos.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
def save_todos(todos):
    with open("todos.json", "w") as f:
        json.dump(todos, f)
def main():
    todos = load_todos()  # 启动时加载

    while True:
        print("\n📋 待办事项清单")
        print("1. 查看清单")
        print("2. 添加待办")
        print("3. 完成待办")
        print("4. 退出")

        choice = input("请选择（1-4）：").strip()

        if choice == "1":
            if len(todos) == 0:
                print("暂无待办事项")
            else:
                for i, task in enumerate(todos):
                    print(f"{i+1}. {task}")

        elif choice == "2":
            task = input("请输入待办事项：").strip()
            todos.append(task)
            save_todos(todos)
            print(f"✅ 已添加：{task}")

        elif choice == "3":
            if len(todos) == 0:
                print("暂无待办事项")
            else:
                for i, task in enumerate(todos):
                    print(f"{i+1}. {task}")
                try:
                    num = int(input("请输入完成的序号："))
                    completed = todos.pop(num - 1)
                    save_todos(todos)
                    print(f"✅ 已完成：{completed}")
                except ValueError:
                    print("请输入有效数字")
                except IndexError:
                    print("序号不存在")

        elif choice == "4":
            save_todos(todos)
            break

        else:
            print("请输入 1-4")

main()