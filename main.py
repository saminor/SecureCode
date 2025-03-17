####################
##Coded-By-Saminor##
####################


########
##Main##
########

from fastapi import FastAPI, File, UploadFile
import subprocess

app = FastAPI()

@app.post("/analyze/")
async def analyze_code(file: UploadFile = File(...)):
    content = await file.read()
    with open("temp_code.py", "wb") as f:
        f.write(content)

    result = subprocess.run(["bandit", "-r", "temp_code.py"], capture_output=True, text=True)
    return {"analysis": result.stdout}


#############
##SonarQube##
#############

import requests

SONARQUBE_URL = "http://localhost:9000"
SONARQUBE_TOKEN = "your_sonarqube_token"

def send_to_sonarqube(file_path: str):
    headers = {"Authorization": f"Basic {SONARQUBE_TOKEN}"}
    with open(file_path, "rb") as file:
        response = requests.post(
            f"{SONARQUBE_URL}/api/projects/create",
            headers=headers,
            files={"file": file}
        )
    return response.json()