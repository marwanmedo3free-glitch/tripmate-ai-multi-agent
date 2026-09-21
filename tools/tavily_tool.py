from tavily import TavilyClient
import os
from dotenv import load_dotenv
load_dotenv()

print("TAVILY KEY EXISTS:", bool(os.getenv("TAVILY_API_KEY")))

api_key=os.getenv("TAVILY_API_KEY")

client=TavilyClient(api_key)

if api_key:
    tavily_client = TavilyClient(api_key=api_key)
else:
    tavily_client = None



def tavily_search(query):
    response=client.search(
        query=query,
        max_results=5
    )
    
    results=[]
    
    for i, r in enumerate(response["results"],1):
        title=r.get("title","unknown")
        url=r.get("url","")
        snippet=r.get("content","").strip()
        
        if len(snippet)>300:
            snippet=snippet[:300].rsplit(" ",1)[0] + "..."
        results.append(f"{i}. **{title}**\n  {url}\n {snippet}")
        
    return "\n\n".join(results)