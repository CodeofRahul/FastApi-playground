from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def hello():
    return {'message':'Hello world!'}

@app.get('/about')
def about():
    return {'message': 'Rahul is a Consultant, Helping Businesses Deploy, Monitor & Scale ML Models...'}