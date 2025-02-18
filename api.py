from fastapi import FastAPI
import asyncio
from fetch_papers import fetch_papers

app = FastAPI()

@app.get("/search")
async def search(query: str):
    """API endpoint to search papers."""
    papers = await fetch_papers(query)
    return {"papers": papers}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
