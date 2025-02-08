from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()

# Обслуживание статических файлов
app.mount("/", StaticFiles(directory="static", html=True), name="static")


@app.get("/favicon.ico")
def favicon():
    return {"message": "No favicon available"}


@app.get("/")
def root():
    return HTMLResponse("""
        <html>
            <head><title>My App</title></head>
            <body>
                <h1>Welcome to my FastAPI app!</h1>
            </body>
        </html>
    """)