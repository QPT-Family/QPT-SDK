# Author: Acer Zhang
# Datetime: 2023/10/28
# Copyright belongs to the author.
# Please indicate the source for reprinting.
import os
import shutil
import glob
import subprocess

VERSION = 39
ENV_PATH = f"QEnvPython/{VERSION}/QPT_SDK/QEnvPython/python{VERSION}"


# ToDO 删除TK下的idlelib和Demo - 放在确认列表中

def install_pip(path):
    arg = f'{os.path.join(os.path.abspath("./"), path, "python.exe")}'
    result = subprocess.run([arg, f"{os.path.abspath('./')}/get-pip.py"], stdout=subprocess.PIPE)
    print(result.stdout.decode())


def clean_cache(path):
    file_list = glob.glob(os.path.join(os.path.abspath('./'), path) + '/**/__pycache__', recursive=True)
    for item in file_list:
        shutil.rmtree(item)
    file_list = glob.glob(os.path.join(os.path.abspath('./'), path, "Scripts") + "/pip3*")
    for item in file_list:
        os.remove(item)


def edit_pth(path):
    text = (f"python{VERSION}.zip" +
            """
.
./Lib
./Lib/site-packages
./Lib/ext
./DLLs
./libs
./tcl
../resources
Scripts
import site
""")
    with open(os.path.join(path, f"python{VERSION}._pth"), "w", encoding="utf-8") as f:
        f.write(text)


def make_dir(path):
    os.makedirs(os.path.join(path, "Lib/site-packages"), exist_ok=True)


if __name__ == '__main__':
    make_dir(ENV_PATH)
    install_pip(ENV_PATH)
    edit_pth(ENV_PATH)
    clean_cache(ENV_PATH)
