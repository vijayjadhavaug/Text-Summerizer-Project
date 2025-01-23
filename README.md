# Text-Summarizer-Project
NLP Application using Hugging face transformer

packages
sacreblue - For Evaluation Matrix. For text summarizaion, we use row matrix and to use row matrix we need this library.
py7zr - For transformers

if you want to publish your library in Pypi then we use setup.py

ConfigBox is a convenient way to access values from dictionary object.
traditionalyy you would do like this:
d1 = {"Key": "Value", "key1":"value1"}
to access value of key1 i use d1['key1']

with configBox, i access it d1.key1

## WORKFLOW

1. update config.yaml --> data ingestion by creating folder and inserting data file
2. update params.yaml
3. update entity --> defin return type of a function using dataclass
4. update config
5. update components
6. update pipeline
7. update main.py
8. update app.py

Dataclass: You don’t need to manually define __init__, __repr__, and __eq__.

e.g.
from dataclasses import dataclass 
    @dataclass
    class Student:
        age:int
        name:str

    s1 = Student(20,"vijay")
    print(s1)

traditional way

class Student:
    def __init__(self,age,name):
        self.age = age
        self.name = name

    def __repr__(self):
        return f"Student(name = {self.name}, age = {self.age})
    
s1 = Student(20,"vijay")
print(s1)