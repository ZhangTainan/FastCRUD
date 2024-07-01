import json
import os

# 获取当前文件所在目录
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# 拼接文件路径
FILE_PATH = os.path.join(SCRIPT_DIR, 'student.json')


def load_students():
    """加载学生数据"""
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)


def save_students(students):
    """保存学生数据到文件"""
    with open(FILE_PATH, 'w', encoding='utf-8') as file:
        json.dump(students, file, ensure_ascii=False, indent=4)


def add_student(student):
    """添加学生"""
    students = load_students()
    students.append(student)
    save_students(students)


def delete_student(student_id):
    """删除学生"""
    students = load_students()
    students = [student for student in students if student['id'] != student_id]
    print(students)
    save_students(students)


def update_student(updated_student):
    """更新学生信息"""
    students = load_students()
    for index, student in enumerate(students):
        if student['id'] == updated_student["id"]:
            students[index] = updated_student  
    save_students(students)


def get_student(student_id):
    """获取学生信息"""
    students = load_students()
    for student in students:
        if student['id'] == student_id:
            return student
    return None


def list_students(keyword:str="", page:int=1, size:int=5):
    """列出所有学生"""
    students = load_students()
    def filter_by_keyword(student):
        """根据关键字过滤学生,模糊查询name、major与gender字段"""
        return keyword in student["name"] or keyword in student["major"] or keyword in student["gender"]
    
    result_students=list(filter(filter_by_keyword, students))[(page-1)*size:page*size]
    return result_students


# 示例用法
if __name__ == "__main__":
    # 添加学生
    new_student = {
        "id": "3",
        "name": "王五",
        "age": "22",
        "gender": "男",
        "major": "信息安全"
    }
    add_student(new_student)
    print("添加学生成功")

    # 更新学生
    updated_data = {
        "age": "23",
        "major": "网络安全"
    }
    update_student("3", updated_data)
    print("更新学生信息成功")

    # 获取学生
    student = get_student("3")
    print(f"获取学生信息: {student}")

    # 列出所有学生
    students = list_students()
    print("所有学生信息:")
    for student in students:
        print(student)

    # 删除学生
    delete_student("3")
    print("删除学生成功")
