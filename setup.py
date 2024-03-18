from setuptools import find_packages,setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='santanu mohapatra',
    author_email='santanumohapatra497@gmail.com',
    install_requires=["openai","langchain","steamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)