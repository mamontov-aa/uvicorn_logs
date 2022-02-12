import uvicorn
from fastapi import FastAPI
import sys

app = FastAPI()

@app.get(path="/")
async def app_health():
    return "OK"

if __name__ == "__main__":
    port = sys.argv[1] if len(sys.argv) > 1 else "8080"
    print(port)
    uvicorn.run("app:app", host="0.0.0.0", port=int(port), log_level="info", log_config="log_config.yaml")
