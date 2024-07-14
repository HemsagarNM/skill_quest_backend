clone the repository 
```bash
git clone https://github.com/hizinberg/SkillQuest.git
```

create a new virtual environment 
```bash
python -m venv <name of virtual environment>
```

navigate to the environment folder 
```bash
cd <name of virtual environment>/scripts
```

activate the environment 
```bash
./activate
```

go to the cloned directory 
install the requirements
```bash
pip install -r requirements.txt
```

follow the comment steps in setup.py
after that run the server
```bash
uvicorn main:app
```
