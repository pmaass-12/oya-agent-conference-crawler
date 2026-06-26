import os
import json

def main():
    try:
        with open("/app/user/kb/oya-agent-outreach-playbook.md", "r") as f:
            content = f.read()
        print(json.dumps({"content": content}))
    except Exception as e:
        print(json.dumps({"error": str(e)}))

if __name__ == "__main__":
    main()
