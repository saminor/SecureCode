<!DOCTYPE html>
<html>
<body>

<h1>Code Security Analysis Service</h1>

<p>A web service designed to analyze source code for security vulnerabilities, that uses SonarQube and alternative projects. 
It integrates with SonarQube to leverage its powerful analysis capabilities while providing custom static analysis features for developers.</p>

<h2>Key Features</h2>
<ul>
    <li>Static analysis of source code for multiple languages.</li>
    <li>Integration with <strong>SonarQube</strong> for advanced analysis.</li>
    <li>RESTful API for code submission and report retrieval.</li>
    <li>Modular and scalable architecture using Docker and Kubernetes.</li>
    <li>Custom analysis tools like <code>Bandit</code> and <code>Semgrep</code>.</li>
</ul>

<h2>Technologies Used</h2>
<div class="skills">
<p align="center">
  <img src="https://skillicons.dev/icons?i=py,fastapi,postgres,kubernetes,docker,nginx" /> + elk + sonarqube 
</p>
</div>

<h2>Architecture</h2>
<p>The service is built using a modular architecture:</p>
<ul>
    <li><strong>Code Submission Module:</strong> Handles file uploads via REST API.</li>
    <li><strong>Security Analysis Module:</strong> Runs static analysis using tools like Bandit and Semgrep.</li>
    <li><strong>SonarQube Management Module:</strong> Sends code to SonarQube for analysis and retrieves results.</li>
    <li><strong>Database Module:</strong> Stores logs, analysis results, and user history using PostgreSQL.</li>
    <li><strong>Reporting Module:</strong> Generates interactive reports (JSON, PDF, dashboards).</li>
</ul>

<h2>Setup Instructions</h2>

<pre>
<code>
# Clone the repository
git clone https://your-gitlab-repo-url.git

# Navigate to the project directory
cd your-project-directory

# Start the service using Docker Compose
docker-compose up --build
</code>
</pre>

<h2>Sample Code for Analysis</h2>

<pre>
<code>
from fastapi import FastAPI, File, UploadFile
import subprocess

app = FastAPI()

@app.post("/analyze/")
async def analyze_code(file: UploadFile = File(...)):
    content = await file.read()
    
    # Save the file for analysis
    with open("temp_code.py", "wb") as f:
        f.write(content)
    
    # Run static analysis using Bandit
    result = subprocess.run(["bandit", "-r", "temp_code.py"], capture_output=True, text=True)
    
    return {"analysis": result.stdout}
</code>
</pre>

<h2>Integrating with SonarQube</h2>

<pre>
<code>
import requests

SONARQUBE_URL = "http://localhost:9000"
SONARQUBE_TOKEN = "your_sonarqube_token"

def send_to_sonarqube(file_path: str):
    headers = {"Authorization": f"Basic {SONARQUBE_TOKEN}"}
    
    # Upload the code for scanning
    with open(file_path, "rb") as file:
        response = requests.post(
            f"{SONARQUBE_URL}/api/projects/create",
            headers=headers,
            files={"file": file}
        )
    
    return response.json()
</code>
</pre>

<h2>Security Considerations</h2>
<ul>
    <li>Use <strong>JWT</strong> for user authentication and role-based access control.</li>
    <li>Isolate the SonarQube service using Docker networking.</li>
    <li>Monitor system performance with <strong>Prometheus</strong> and <strong>Grafana</strong>.</li>
</ul>

<h2>Contributing</h2>
<p>We welcome contributions! Feel free to submit pull requests or open issues for feature requests and bug fixes.</p>

<h2>License</h2>
<p>This project is licensed under the <strong>MIT License</strong>.</p>

</body>
</html>
