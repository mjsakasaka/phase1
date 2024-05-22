from fastapi import FastAPI, Form, Request, Response
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from fastapi.staticfiles import StaticFiles
from urllib.parse import quote

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key="SECRET_KEY")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home_page(request: Request):
    return FileResponse("static/homepage.html")

@app.post("/signin")
async def login(request: Request, username: str = Form(default=None), password: str = Form(default=None)):
    if username == "test" and password == "test":
        request.session["SIGNED-IN"] = True
        print(request.session)
        return Response(status_code=302, headers={"Location": "/member"})
    elif username == None or password == None:
        error_message = "請輸入帳號和密碼"
        return Response(status_code=302, headers={"Location": f"/error?message={quote(error_message)}"})
    else:
        error_message = "帳號或密碼輸入錯誤"
        return Response(status_code=302, headers={"Location": f"/error?message={quote(error_message)}"})

@app.get("/member")
async def member_page(request: Request):
    if not request.session.get("SIGNED-IN"):
        return RedirectResponse("/")
    return templates.TemplateResponse("result.html", {
        "request": request, 
        "message": "恭喜您，成功登入系統",
        "title": "歡迎光臨，這是會員頁",
        "logout": "登出系統"
    })
    
@app.get("/error", response_class=HTMLResponse)
async def error_page(request: Request, message: str):
    return templates.TemplateResponse("result.html", {
        "request": request, 
        "message": message,
        "title": "失敗頁面",
        "logout": "返回首頁"
    })

@app.get("/signout")
async def signout(request: Request, response: RedirectResponse):
    request.session["SIGNED-IN"] = False
    response.delete_cookie("session")
    return RedirectResponse("/")


# 计算平方
@app.get("/square/{input_val}")
async def get_square(request: Request, input_val: int):
    square = int(input_val) ** 2
    return templates.TemplateResponse("result.html", {
        "request": request, 
        "message": square,
        "title": "正整數平方計算結果",
        "logout": ""
    })
