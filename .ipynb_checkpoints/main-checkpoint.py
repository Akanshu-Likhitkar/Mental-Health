import joblib 
from fastapi import FastAPI 
from pydantic import BaseModel

model =  joblib.load("Mental_Health_Model.pkl")

app = FastAPI()

class StudentData(BaseModel):


Age
Gender
Country
Academic_Level
Most_Used_Platform
Purpose_Of_Use
Avg_Daily_Usage_Hours
Daily_Unlocks
Study_Hours
Physical_Activity_Hours
Sleep_Hours_Per_Night
Stress_Level
Mental_Health_Score
group_countries


    












@app.get("/")
def greet():

    return "Hello! Welcome to the Mental Health Prediction API."

@app.post("/predict")
def predict(data : dict):
    pass

