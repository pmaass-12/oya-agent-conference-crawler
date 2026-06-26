import os
import json

def main():
    cwd = os.getcwd()
    paths = [
        cwd,
        os.path.join(cwd, ".opencode"),
        os.path.expanduser("~/.config/opencode")
    ]
    
    files_list = []
    contents = {}
    
    for path in paths:
        if not os.path.exists(path):
            files_list.append(f"Directory does not exist: {path}")
            continue
        files_list.append(f"Scanning directory: {path}")
        try:
            for root, dirs, files in os.walk(path):
                if 'node_modules' in root or '.git' in root:
                    continue
                for file in files:
                    file_path = os.path.join(root, file)
                    display_path = file_path
                    if file_path.startswith(cwd):
                        display_path = "." + file_path[len(cwd):]
                    elif file_path.startswith(os.path.expanduser("~")):
                        display_path = "~" + file_path[len(os.path.expanduser("~")):]
                    
                    files_list.append(display_path)
                    
                    if file.endswith(('.json', '.jsonc', '.yml', '.yaml', '.md', '.txt', 'config')):
                        try:
                            with open(file_path, 'r', errors='ignore') as f:
                                contents[display_path] = f.read()
                        except Exception as e:
                            contents[display_path] = f"Error reading file: {str(e)}"
        except Exception as e:
            files_list.append(f"Error scanning {path}: {str(e)}")
            
    print(json.dumps({
        "scanned_directories": paths,
        "files_found": files_list,
        "contents": contents
    }, indent=2))

if __name__ == "__main__":
    main()
