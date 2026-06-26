import os
import glob
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
    
    cwd = os.getcwd()
    
    paths_to_search = [
        cwd,
        os.path.join(cwd, ".opencode"),
        os.path.expanduser("~/.config/opencode")
    ]
    
    searched_files = set()
    
    for base_dir in paths_to_search:
        if not os.path.exists(base_dir):
            continue
        for root, dirs, files in os.walk(base_dir):
            if "node_modules" in root or ".git" in root:
                continue
            for file in files:
                file_path = os.path.join(root, file)
                if file_path in searched_files:
                    continue
                searched_files.add(file_path)
                
                try:
                    if os.path.getsize(file_path) > 1024 * 1024:
                        continue
                except Exception:
                    continue
                
                content = search_text_in_file(file_path, keywords)
                if content is not None:
                    display_path = file_path
                    if file_path.startswith(cwd):
                        display_path = "." + file_path[len(cwd):]
                    elif file_path.startswith(os.path.expanduser("~")):
                        display_path = "~" + file_path[len(os.path.expanduser("~")):]
                    results[display_path] = content

    print(json.dumps({"results": results}, indent=2))

if __name__ == "__main__":
    main()
