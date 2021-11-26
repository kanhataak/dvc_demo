 create env
 ```bash
 conda create -n env_name python=3.7 -y
 ```



install the req
```bash
pip install -r requirements.txt
```

download the data from
```bash
git init   
```
when we enter then see all green 

```bash
dvc init  
```
some of the file will be created like .dvc , .dvcignore etc

```bash
dvc add data_given\winequality.csv
```

we are adding the data


```bash
git add .
```
whatever given in current dir add to the staging area

```bash
git commit -m "first commit"
```

```bash
git add . && git commit -m "update readme.md"
```

Create a git Repo

git remote add origin https://github.com/kanhataak/dvc_demo.git

Till this point we are in master branch so we have to change it in main branch below command

```bash
git branch -M main
```

```bash
git push origin main
```
In order to reproduce the all stages from dvc.yaml file excute the below command

```bash
dvc repro
```
In order to track that how your model is behaving

```bash
 dvc metrics show
 ```
To check the difference of the performance of the model

```bash
dvc metrics diff
```
for testing are using tox am

create your own library

```bash
 python setup.py sdist bdist_wheel
 ```
tox command
```bash
tox
```
for rebuilding

```bash
tox -r
```
pytest

```bash
pytest -c
```
setup command
```bash
pip install -e .
```

tox command -
```bash
tox
```
for rebuilding -
```bash
tpx -r
```
pytest commamd
```bash
pytest -v
```
setup commands -
```bash
pip install -e .
```
 if build your own package commands-
 ```bash
 python setup.py sdist bdist wheel
 ```
