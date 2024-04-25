from fastapi import FastAPI, Form, Request
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.add_middleware(SessionMiddleware, secret_key="SECRET_KEY")


@app.get("/")
async def home_page():
    return FileResponse("homepage.html")

@app.get("/styles.css")
async def css():
    return FileResponse("styles.css")

def js_string(url: str):
    return "<script>window.location.href = \"" + url + "\";</script>"

@app.post("/signin")
async def login(request: Request, username: str = Form(default=None), password: str = Form(default=None)):
    if username == "test" and password == "test":
        request.session["SIGNED-IN"] = True
        return HTMLResponse(js_string("/member"))
    elif username == None or password == None:
        return HTMLResponse(js_string("/error?message=請輸入帳號和密碼"))
    else:
        return HTMLResponse(js_string("/error?message=帳號或密碼輸入錯誤"))
    
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