import os
import json

def main():
    results = {}
    found_files = []
    # Search the entire filesystem starting from root `/` (or maybe starting from `/app` first to avoid proc/sys/dev)
    search_paths = ["/app", "/tmp", "/home", "/var/tmp"]
    for path in search_paths:
        if os.path.exists(path):
            for root, dirs, files in os.walk(path):
                for file in files:
                    if "playbook" in file.lower() or "persona" in file.lower() or "icp" in file.lower():
                        found_files.append(os.path.join(root, file))
    
    results["found_files"] = found_files
    
    # Try to read `/app/user/kb/oya-agent-outreach-playbook.md` specifically if it exists
    playbook_path = "/app/user/kb/oya-agent-outreach-playbook.md"
    if os.path.exists(playbook_path):
        try:
            with open(playbook_path, "r", encoding="utf-8") as f:
                results["playbook_content"] = f.read()
        except Exception as e:
            results["playbook_error"] = str(e)
            
    print(json.dumps(results))

if __name__ == "__main__":
    main()
