import os
from os.path import join, dirname
from dotenv import load_dotenv
from pathlib import Path
import logging

# set logging
fmt = "%(asctime)s %(levelname)s %(module)s_%(lineno)s :%(message)s"
logging.basicConfig(level=logging.INFO, format=fmt)

logging.info("環境変数を読み込み")
home_path = str(Path(join(dirname(__file__), "../")).resolve())
os.environ["HOME_PATH"] = home_path

dotenv_path = join(home_path, ".env")
load_dotenv(dotenv_path)

os.environ["AUTH_JSON_PATH"] = join(home_path, os.getenv("AUTH_JSON_NAME"))
