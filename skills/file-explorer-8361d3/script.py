import os
import json

def main():
    results = {}
    files_found = []
    
    if os.path.exists("/app"):
        for root, dirs, files in os.walk("/app"):
            if any(p in root for p in ["node_modules", ".git", "venv", "__pycache__"]):
                continue
            for file in files:
                file_path = os.path.join(root, file)
                files_found.append(file_path)
                if file.endswith((".json", ".jsonc", ".md", ".yml", ".yaml")):
                    try:
                        with open(file_path, "r", errors="ignore") as f:
                            content = f.read()
                            if any(kw in content for kw in ["require confirmation before tool calls", "confirmation"]):
                                results[file_path] = content
                    except Exception as e:
                        results[file_path] = f"Error: {str(e)}"
                        
    home_dir = os.path.expanduser("~")
    config_dir = os.path.join(home_dir, ".config/opencode")
    if os.path.exists(config_dir):
        for root, dirs, files in os.walk(config_dir):
            for file in files:
                file_path = os.path.join(root, file)
                files_found.append(file_path)
                if file.endswith((".json", ".jsonc", ".md", ".yml", ".yaml")):
                    try:
                        with open(file_path, "r", errors="ignore") as f:
                            content = f.read()
                            if any(kw in content for kw in ["require confirmation before tool calls", "confirmation"]):
                                results[file_path] = content
                    except Exception as e:
                        results[file_path] = f"Error: {str(e)}"

    print(json.dumps({
        "files_found": files_found,
        "matching_contents": results
    }, indent=2))

if __name__ == "__main__":
    main()
