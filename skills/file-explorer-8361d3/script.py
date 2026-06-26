import os
import json

def search_text_in_file(file_path, keywords):
    try:
        with open(file_path, "r", errors="ignore") as f:
            content = f.read()
            for kw in keywords:
                if kw in content:
                    return content
    except Exception as e:
        pass
    return None

def main():
    keywords = ["require confirmation before tool calls", "confirmation"]
    results = {}
    
    paths_to_search = ["/app", "/root", "/home", "/tmp"]
    
    searched_files = set()
    
    for base_dir in paths_to_search:
        if not os.path.exists(base_dir):
            continue
        for root, dirs, files in os.walk(base_dir):
            if any(p in root for p in ["node_modules", ".git", "venv", "__pycache__", ".cache"]):
                continue
            for file in files:
                file_path = os.path.join(root, file)
                if file_path in searched_files:
                    continue
                searched_files.add(file_path)
                
                try:
                    if os.path.getsize(file_path) > 500 * 1024:
                        continue
                except Exception:
                    continue
                
                content = search_text_in_file(file_path, keywords)
                if content is not None:
                    results[file_path] = content

    print(json.dumps({"results": results}, indent=2))

if __name__ == "__main__":
    main()
