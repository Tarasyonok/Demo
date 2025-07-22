from fastapi import FastAPI

app = FastAPI(
    title="Demo",
    version="7.7.7",
)


@app.post("/analyze-image")
async def analyze_image():
    return "Hello World"


@app.get("/top-tags")
async def top_tags():
    return "Hello World"
