from pathlib import Path

#Current Working Directory
root = Path(".")

#Folders to create
folders = [
    "app/api",
    "app/core",
    "app/rag",
    "app/services",
    "data",
    "templates",
    "static",
    "uploads",
    "tests",
]

#Files to create
files = [
    "app/main.py",    
    "ingest_sample_knowledgeBase.py",
    "run.py",
    ".env",
]

#Create Folders
for folder in folders:
    (root / folder).mkdir(parents=True, exist_ok=True)
    
#Create Files
for file in files:
     (root / file).touch(exist_ok=True)   
     
     
print("Project Structure is created successfully!")     