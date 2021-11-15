import os

dirs = [
    os.path.join("data","raw"),
    os.path.join("data","processed"),
    "notebooks",
    "saved_models",
    "src"
]

for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True) #True : check dir created or not if not then create
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:
        pass 

files = [
    "dvc.yaml",  
    "params.yaml",
    ".gitignore",  #all the things we wont like to push on github those file name we keep inside it. 
    os.path.join("src","__init__.py"), #read as python package
    "README.md"
]

for file_ in files:
    with open(file_,"w") as f:
        pass