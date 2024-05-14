from fastapi import FastAPI, Form, Request
from fastapi.responses import FileResponse, RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from fastapi.staticfiles import StaticFiles
from urllib.parse import quote
from utils import get_db_data, change_db_data
from json import dumps

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key="SECRET_KEY")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home_page(request: Request):
    return FileResponse("static/homepage.html")

@app.post("/signin")
async def login(request: Request, username: str = Form(default=None), password: str = Form(default=None)):
    # check username and password
    db_data = get_db_data("SELECT password, id, username, name FROM member WHERE username = %s;", (username, ))
    if db_data != []:
        if db_data[0][0] == password:
            request.session["SIGNED-IN"] = True
            request.session["member_id"] = db_data[0][1]
            request.session["username"] = db_data[0][2]
            request.session["name"] = db_data[0][3]
            print(request.session)
            return RedirectResponse(status_code=303, url="/member")
    else:
        error_message = "帳號或密碼輸入錯誤"
        return RedirectResponse(status_code=303, url=f"/error?message={quote(error_message)}")

@app.get("/member")
async def member_page(request: Request):
    # 檢查登陸狀態
    if not request.session.get("SIGNED-IN"):
        return RedirectResponse("/")
    # 顯示留言
    name = request.session["name"]
    messages = get_db_data("SELECT member.name, message.content, message.id FROM message INNER JOIN member ON member.id = message.member_id;")
    return templates.TemplateResponse("member.html", {
        "request": request, 
        "login_message": f"{name}，歡迎登入系統",
        "title": "歡迎光臨，這是會員頁",
        "logout": "登出系統",
        "messages": messages,
        "name": name
    })
    
@app.get("/error")
async def error_page(request: Request, message: str):
    return templates.TemplateResponse("result.html", {
        "request": request, 
        "message": message,
        "title": "失敗頁面",
        "logout": "返回首頁"
    })

@app.get("/signout")
async def signout(request: Request):
    if request.session["SIGNED-IN"]:
        request.session.pop("member_id")
        request.session.pop("username")
        request.session.pop("name")
    request.session["SIGNED-IN"] = False
    print(request.session)
    return RedirectResponse("/")

@app.post("/signup")
async def signup(request: Request, 
                 name: str = Form(), 
                 username: str = Form(), 
                 password: str = Form()):
    db_username = get_db_data("SELECT username FROM member WHERE username = %s;", (username, ))
    if db_username != []:
        error_message = "帳號已被使用"
        return RedirectResponse(status_code=303, url=f"/error?message={quote(error_message)}")
    change_db_data("INSERT INTO member (name, username, password) VALUES (%s, %s, %s)", (name, username, password))
    return RedirectResponse(status_code=303, url="/")
    
@app.post("/createMessage")
async def creat_message(request: Request, content: str = Form()):
    member_id = request.session["member_id"]
    change_db_data("INSERT INTO message(member_id, content) VALUES (%s, %s);", (member_id, content))
    return RedirectResponse(status_code=303, url="/member")

@app.post("/deleteMessage")
async def delete_message(request: Request):
    form_data = await request.form()
    message_id = form_data['message_id']
    change_db_data("DELETE FROM message WHERE id = %s;", (message_id, ))
    return RedirectResponse(status_code=303, url="/member")

@app.get("/api/member")
async def member_query(request: Request, username: str):
    data = get_db_data("SELECT id, name, username FROM member WHERE username = %s", (username, ))
    if data == []:
        response_data = {
            "data": "null"
        }
        return JSONResponse(content=response_data)
    else:
        member_id = data[0][0]
        name = data[0][1]
        username = data[0][2]
        response_data = {
            "data":{
                "id": member_id,
                "name": name,
                "username": username
            }
        }
        return JSONResponse(content=response_data)