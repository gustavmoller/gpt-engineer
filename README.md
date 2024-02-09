# Experiments with [GPT-Engineer](https://github.com/gpt-engineer-org/gpt-engineer)

### Setup

1. Set Python version to `3.9.16`
2. Create venv: `python3 -m venv venv`
3. Activate venv: `source venv/bin/activate`
4. Install packages: `pip install -r requirements.txt`
5. Save GPT4 API key in `.env` file

### Create new code, or improve existing code

1. Add your code to a folder `<project_dir>`. Leave this folder empty to create new code. E.g. `db_monitoring`.
2. Create a file called `prompt` (no extension) inside your new folder and fill it with instructions
3. Run `gpte <project_dir>` to create new code, or `gpte <project_dir> -i` to improve your code.
