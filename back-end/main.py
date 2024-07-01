import uvicorn
from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from student import *

app = FastAPI(
    title="学生管理系统",  # 文档标题
    description="一个简单的学生管理系统接口，提供增删改查等功能。",  # 文档描述
    version="1.0.0"  # 版本号
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有域
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有方法
    allow_headers=["*"],  # 允许所有头部
)

# 这里创建一个router,prefix指定这个router所有请求接口的前缀
router = APIRouter(prefix="/students", tags=["学生管理接口"])


class Student(BaseModel):
    ''' 定义一个学生的Model,用于接收请求体 '''
    id: int
    name: str
    age: int
    gender: str
    major: str

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "major": self.major
        }

    def __str__(self) -> str:
        return f"({self.id},{self.name},{self.age},{self.gender},{self.major})"


@router.get("/", summary="查询学生", description="根据id获取学生信息")
async def get(id: int) -> dict:
    student = get_student(id)
    if student is None:
        return {
            "message": "学生不存在"
        }
    return student


@router.post("/", summary="添加学生", description="根据传入的请求体添加学生")
async def post(student: Student) -> dict:
    add_student(student.to_dict())
    return {
        "message": "添加成功"
    }


@router.patch("/", summary="修改学生", description="根据id修改学生")
async def patch(student: Student) -> dict:
    update_student(student.to_dict())
    return {
        "message": "更新成功"
    }


@router.delete("/", summary="删除学生", description="根据id删除学生")
async def delete(id: int) -> dict:
    delete_student(id)
    return {
        "message": "删除成功"
    }


@router.get(
    "/list",
    summary="获取学生列表",
    description="获取学生列表,可根据keyword模糊查询,根据page,size进行分页"
)
async def list(keyword: str = "", page: int = 1, size: int = 5) -> list:
    students = list_students(keyword, page, size)
    return students


app.include_router(router)
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
