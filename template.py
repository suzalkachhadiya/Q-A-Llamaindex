import os

from pathlib import Path

files=[
    "QAWithPDF/__init__.py",
    "QAWithPDF/data_ingestion.py",
    "QAWithPDF/embedding.PY",
    "QAWithPDF/model_api.py",
    "app.py",
    "logger.py",
    "exception.py",
    "setup.py"
]

for filepath in files:
    filepath=Path(filepath)

    filedir, filename=os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        # logging.info(f"creating Directory: {filedir} for the {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            # logging.info(f"creating empty file:{filepath}")

    else:
        pass
        # logging.info(f"{filename} is alredy created")