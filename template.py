import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:, %(message)s:')

project_name = 'textsummerizer'

file_list = [
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init_.py',
    f'src/{project_name}/utils/__init_.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/logging/__init_.py',
    f'src/{project_name}/config/__init_.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init_.py',
    f'src/{project_name}/entity/__init_.py',
    f'src/{project_name}/constants/__init_.py',
    'config/config.yaml',
    'params.yaml',
    'app.py',
    'main.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynp'
]

for filepath in file_list:
    filepath = Path(filepath)
    file_dir, file_name = os.path.split(filepath)

    if file_dir != '':
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Created {file_dir} at {filepath}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0 ):
        with open(filepath, 'w') as file:
            pass
        logging.info(f"Created a empty file with filename{filepath}")

    else:
        logging(f"{file_name} already exsits")