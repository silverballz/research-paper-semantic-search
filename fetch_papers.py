import aiohttp
import asyncio
import os
from dotenv import load_dotenv

# Load API Key (if available)
load_dotenv()
SEMANTIC_SCHOLAR_API = "https://api.semanticscholar.org/graph/v1/paper/search"

async def fetch_papers(query, limit=10):
    """Fetch research papers from Semantic Scholar API asynchronously."""
    params = {"query": query, "limit": limit, "fields": "title,abstract,authors,year,citationCount,url"}

    async with aiohttp.ClientSession() as session:
        async with session.get(SEMANTIC_SCHOLAR_API, params=params) as response:
            return await response.json()

# Test fetching papers
if __name__ == "__main__":
    query = "deep learning"
    results = asyncio.run(fetch_papers(query))
    print(results)
