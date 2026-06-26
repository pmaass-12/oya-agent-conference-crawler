import os
import json

def main():
    file_path = "/app/user/kb/oya-agent-outreach-playbook.md"
    try:
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            print(json.dumps({"success": True, "content": content}))
        else:
            print(json.dumps({"success": False, "error": f"File {file_path} not found"}))
    except Exception as e:
        print(json.dumps({"success": False, "error": str(e)}))

if __name__ == "__main__":
    main()
