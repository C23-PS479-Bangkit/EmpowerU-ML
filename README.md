# EmpowerU-ML
training model ML

1. create a new virtual environment with the name venv:
```
virtualenv venv
```
2. activate the virtual environment:
```
.\venv\Scripts\activate
```
3. install the dependencies by running the command:
```
pip install -r requirements.txt
```
4. After the installation is done, we can check we have correctly installed all the packages in our virtual environment:
```
pip freeze
```
We should see the same list in the file requirements.txt

5. run the app 
```
uvicorn main:app --host 127.0.0.1 --port 8000
```
## Docker Development

1. Build the container image 
```
docker build -t empoweru-ml .
```
2. Start the container
```
docker run -dp 3000:3000 empoweru-ml
```