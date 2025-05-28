# FastApi-playground
A FastAPI lab for prototyping ideas, testing features, and deepening API knowledge.





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
