import os
import json

def main():
    env_vars = dict(os.environ)
    # Redact potential secrets from environment variables
    for k in list(env_vars.keys()):
        if any(sec in k.lower() for sec in ["key", "token", "secret", "auth", "pwd", "pass"]):
            env_vars[k] = "[REDACTED]"
            
    # List files in root and other places
    root_files = []
    try:
        root_files = os.listdir('/')
    except Exception as e:
        root_files = [f"Error: {str(e)}"]
        
    app_files = []
    try:
        app_files = os.listdir('/app')
    except Exception as e:
        app_files = [f"Error: {str(e)}"]

    parent_app_files = []
    try:
        parent_app_files = os.listdir('..')
    except Exception as e:
        parent_app_files = [f"Error: {str(e)}"]

    print(json.dumps({
        "env": env_vars,
        "root_files": root_files,
        "app_files": app_files,
        "parent_app_files": parent_app_files
    }, indent=2))

if __name__ == "__main__":
    main()
