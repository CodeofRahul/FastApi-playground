# FastApi-playground
A FastAPI lab for prototyping ideas, testing features, and deepening API knowledge.

![Fastapi 8](https://github.com/user-attachments/assets/cf28c33f-eba2-4562-a1f8-ce02e09c1afa)

![Fastapi 7](https://github.com/user-attachments/assets/de5730b6-9fbe-4f2d-a061-c5eba6731f1d)

![Fastapi 6](https://github.com/user-attachments/assets/574a192d-2d68-4a30-af85-d6817e5bdf43)

![Fastapi 5](https://github.com/user-attachments/assets/08d4b9ec-d6ff-43ea-86cb-dd7061c71e3e)

![Fastapi 4](https://github.com/user-attachments/assets/380c1b44-e4ca-4c5e-af6d-47009bbad433)

![Fastapi 3](https://github.com/user-attachments/assets/21a25096-17e5-4288-b238-8dfe5c542ca2)

![Fastapi 2](https://github.com/user-attachments/assets/65a5d86e-b424-4d42-a9c8-154176f7fab9)

![Fastapi 1](https://github.com/user-attachments/assets/5bf32338-a69c-48b3-b597-fd32351ead8e)


## Bash Environment Commands

- To Create a file

```bash

touch <file_name>
# Example: touch Test_Excercise.py
```

- Run python (.py) file:

```bash
python file_name.py

```

- To Create a virtual environment

```bash

python -m venv <env_name>
# Example: python -m venv playground
```

- Activate the virtual environment

```bash

source <env_name>/bin/activate  # for macos
source <env_name>/Scripts/activate
# Example for macos: source playground/bin/activate
# Example for window bash: source playground/Scripts/activate
```
- Deactivate the virtual environment

```bash

deactivate
```

- Delete the environment

```bash

rm -rf <env_name>
# Example: rm -rf playground
```

- Useful Bash Tips for Environment Management

List Python virtual environments if stored in a folder (e.g., `~/venvs`)

```bash

ls ~/venvs
```

Find all virtual environments on your system (search for `activate` scripts)

```bash

find ~ -type f -name "activate"
```

Quick script to list venv env names inside `~/venvs`

```bash

for dir in ~/venvs/*; do
  if [ -f "$dir/bin/activate" ]; then
    echo "$(basename "$dir")"
  fi
done
```

## Pip Commands

- To install requirements.txt = `pip install -r requirements.txt`
- To check install packages = `pip list`
- To check detailed about package = `pip show package_name`
- To install package = `pip install package_name`
- To uninstall package = `pip uninstall package_name`
- To save all packages of env to a requirements.txt file = `pip freeze > requirements.txt`

## Git commands

- To add all file = `git add .`
- To add any particular file = `git add <file_name>`
- To commit = `git commit -m "commit message"`
- To push the code = `git push origin main`
