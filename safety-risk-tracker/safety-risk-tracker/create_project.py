import os

# Create directory structure
os.makedirs("app/routers", exist_ok=True)
os.makedirs("tests", exist_ok=True)

# Create requirements.txt
with open("requirements.txt", "w") as f:
    f.write("fastapi==0.104.1\nuvicorn==0.24.0\nsqlalchemy==2.0.23\npydantic==2.5.0\npython-multipart==0.0.6\npydantic-settings==2.1.0")

# Create empty __init__.py files
open("app/__init__.py", "w").close()
open("app/routers/__init__.py", "w").close()
open("tests/__init__.py", "w").close()

print("Project structure created!")
