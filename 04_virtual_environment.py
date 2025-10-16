# Commands for the virtual environment

# Мини-шпаргалка

# Создать проект:

# Bash
# mkdir project && cd project
# python3 -m venv .venv && source .venv/bin/activate
# pip install fastapi uvicorn[standard]

# Запустить сервер:

# Bash
# uvicorn main:app --reload

# Сделать первый коммит:

# Bash
# git init
# git add .
# git commit -m "Initial commit"

# Даже с pyenv всё равно создаём venv под используемую версию Python для каждого проекта:

# Bash
# rm -rf .venv
# python -m venv .venv
# source .venv/bin/activate
# pip install --upgrade pip
# pip install fastapi uvicorn[standard]
