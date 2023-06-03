from fastapi import FastAPI
from hello import sum_xy
import logging
from data_models import SamplePostRequest

app = FastAPI()


log_format = "[%(name)s][%(levelname)-6s] %(message)s"
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.basicConfig(format=log_format)
logger = logging.getLogger('my_logger')

logger.setLevel(logging.DEBUG)
#logger.debug('This is a debug message')
#logger.info('This is an info message')
#logger.warning('This is a warning message')
#logger.error('This is an error message')
#logger.critical('This is a critical message')

@app.get("/")
def home():
    logger.info('This is an info message')
    return "Another hello"

@app.get("/sum/{c}")
def sum_xy_endpoint(c:str, a: int, b: int):
    logger.debug('This is a sum debug message')
    return c + " " + str(sum_xy(a, b))

@app.post("/predict")
def predict(request: SamplePostRequest):
    logger.debug('This is a predict debug message')
    return [request.a + request.c[0]]

@app.get("/predict")
def predict():
    return "From predict function get"

@app.get("/health")
def health_check():
    return "OK"

"""
- Create simple function in a script, like sum_xy

- Add a test case for the simple function

- Add requirements.txt file

- Create Makefile that supports install, lint, test functions.

- Add github action to lint and test the simple function.

- Creat fastapi app that has at least two endpoints, one support GET method and the other supports POST method.

- Add test cases for fastapi app's endpoints

- Add logging to the app
"""
