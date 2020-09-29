import os
from os.path import join, dirname
from dotenv import Dotenv

dotenv_path = join(dirname(__file__), '../.env')
Dotenv(dotenv_path)

MINDWAVE_PORT = os.environ.get("MINDWAVE_PORT")
