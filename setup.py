from setuptools import setup, find_packages

setup(
    name='ExcelOpera',
    version='1.0.0',
    description='this package can insert a object to excel',
    author='baiyu',
    author_email='zhh_baiyu@163.com',
    license='MIT License',
    url="https://github.com/BaiYu96/ExcelOpera.git",

    # 依赖包
    install_requires=[
        "pywin32"
    ],

    # 包包含的文件
    packages=find_packages('src')
)
