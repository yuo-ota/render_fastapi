from typing import Optional

from fastapi import FastAPI

import random
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]
    
    return {"result" : omikuji_list[random.randrange(10)]}

@app.get("/index")
def index():
    html_content = """
        <!DOCTYPE HTML>
        <html>
            <head>
                <title>ネットワークプログラミング課題ページ</title>
            </head>
            <body>
                <div style="margin-left:5vw; margin-right:5vw; margin-top: 20px; padding:20px; background-color:#eee;">
                    <h3>匿名1</h3>
                    <h4>
                        ハンドルネームの名義をGitHubで用いてきた一方で、
                        インターンの応募や授業で提出すると考えると実名の方がいい気もしてくる
                        今日この頃。
                    </h4>
                </div>
                <div style="margin-left:5vw; margin-right:5vw; margin-top: 20px; padding:20px; background-color:#eee;">
                    <h3>匿名2</h3>
                    <h4>
                        先日publicのレポジトリを見たよ～というAJの友人がいて、
                        授業のために公開することに驚かれましたね。<br>
                        確かに珍しいのかも...?
                    </h4>
                </div>
                <div style="margin-left:5vw; margin-right:5vw; margin-top: 20px; padding:20px; background-color:#eee;">
                    <h3>匿名3</h3>
                    <h4>
                        そろそろ書くことがなくなってきたので最後にします。<br>
                        最終課題のチーム制作でwebアプリケーション制作というのは要件満たせているのか気になっていますね。
                    </h4>
                </div>
            </body>
        </html>
    """
    return HTMLResponse(content=html_content, status_code=200)