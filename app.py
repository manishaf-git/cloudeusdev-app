# main.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>FastAPI Web UI</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f4f7f6;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .card {
                background: white;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                text-align: center;
                max-width: 400px;
                width: 100%;
            }
            h1 {
                color: #2c3e50;
                margin-bottom: 8px;
            }
            p {
                color: #7f8c8d;
                font-size: 1.1em;
            }
            .badge {
                display: inline-block;
                background-color: #2ecc71;
                color: white;
                padding: 6px 16px;
                border-radius: 20px;
                font-size: 0.85em;
                font-weight: bold;
                text-transform: uppercase;
                letter-spacing: 1px;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Hello, World! - v1</h1>
            <p>Welcome to your native FastAPI user interface.</p>
            <span class="badge">Status: Running</span>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
