# Author: Acer Zhang
# Datetime: 2023/10/29
# Copyright belongs to the author.
# Please indicate the source for reprinting.

from setuptools import setup

setup(
    name='QEnvPython39',
    version="3.9.13",
    packages=["QPT_SDK"],
    url='https://github.com/GT-ZhangAcer/QPT',
    license='MIT',
    author='GT-ZhangAcer',
    author_email='zhangacer@foxmail.com',
    description='QPT-Python环境打包工具 SDK',
    # python_requires='=3.9',
    include_package_data=True,
    include_dirs=["QPT_SDK"]
)
