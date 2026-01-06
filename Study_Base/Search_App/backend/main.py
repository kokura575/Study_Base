from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

@app.get("/api/search")
def search(q: str):
    if not q:
        return []
    
    results = []
    
    for root, dirs, files in os.walk(BASE_DIR):
        if "Search_App" in dirs:
            dirs.remove("Search_App")
        if ".git" in dirs:
            dirs.remove(".git")
            
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                        if q.lower() in content.lower():
                            idx = content.lower().find(q.lower())
                            start = max(0, idx - 40)
                            end = min(len(content), idx + len(q) + 40)
                            snippet = "..." + content[start:end].replace("\n", " ") + "..."
                            
                            rel_path = os.path.relpath(full_path, BASE_DIR)
                            results.append({
                                "file_name": file,
                                "path": rel_path,
                                "full_path": full_path,
                                "snippet": snippet
                            })
                except Exception as e:
                    print(f"Error reading {full_path}: {e}")
                    
    return results

@app.post("/api/open")
def open_file(item: dict):
    path = item.get("path")
    if not path:
        return {"error": "No path provided"}
    
    # Security check: Ensure path is within BASE_DIR
    target_path = os.path.join(BASE_DIR, path)
    if not os.path.normpath(target_path).startswith(BASE_DIR):
        return {"error": "Invalid path"}

    if os.path.exists(target_path):
        try:
            os.startfile(target_path)
            return {"status": "success"}
        except Exception as e:
            return {"error": str(e)}
    return {"error": "File not found"}

app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
