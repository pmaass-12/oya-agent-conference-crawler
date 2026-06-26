import os
import json

def main():
    results = []
    # Fast walk of /app
    for root, dirs, files in os.walk("/app"):
        # Prune slow directories in-place
        dirs[:] = [d for d in dirs if d not in ["node_modules", ".git", "venv", "__pycache__", "dist", "build"]]
        for file in files:
            if "playbook" in file.lower() or "oya-agent" in file.lower():
                results.append(os.path.join(root, file))
    print(json.dumps({"results": results}))

if __name__ == "__main__":
    main()
