这个项目使用json模拟数据库，是一个比较好的练习项目。可以练习css、js、axios，同时可以对FastAPI有一个认识。

1. 使用vscode 打开整个文件夹
2. 启动后端
   1. 新建一个终端
   2. `cd back-end` 进入后端目录
   3. `python -m venv venv`创建虚拟环境（防止污染自己的环境）
   4. .`/venv/script/activate`激活虚拟环境
   5. `pip install -r requirements.txt`安装依赖包
   6. 启动后端的两种方式
      1. `python main.py`
      2. `uvicorn main:app --reload --port 8000`带热更新（即修改代码后服务会自动重载）
   7. 后端接口文档地址[http://127.0.0.1:8000/docs](http://127.0.0.1:6000) ,如果加载不出来尝试使用外网。
3. 启动前端
   1. 在vscode中安装插件`Live Service`

![image.png](https://cdn.nlark.com/yuque/0/2024/png/25539371/1718879396828-b74a829f-925d-4ccf-8689-4a33e1981bac.png#averageHue=%23252424&clientId=u1763e595-55f9-4&from=paste&height=285&id=u3f35eabb&originHeight=428&originWidth=414&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=39809&status=done&style=none&taskId=u635b6a9a-27e3-4c9f-aa02-81a78442b7f&title=&width=276)

   2. 使用Live Server 打开 `front-end/index.html`

![image.png](https://cdn.nlark.com/yuque/0/2024/png/25539371/1718879327558-e9a1013d-9fab-4090-aabc-f9104f93a372.png#averageHue=%23222221&clientId=u1763e595-55f9-4&from=paste&height=628&id=u68ba7161&originHeight=942&originWidth=1266&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=181597&status=done&style=none&taskId=ud6511986-ab88-4a59-b348-09cb4e6ae5a&title=&width=844)
