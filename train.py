from spacy.cli.project.run import project_run
from pathlib import Path
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
os.system('python -m spacy train ./cfg/config.cfg -o ./training -V')