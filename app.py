from flask import Flask, request, jsonify, send_file
import requests
import os
import json
from flask_cors import CORS  # Import CORS

app = Flask(__name__)

# Enable CORS for the entire app
CORS(app)

# Helper function to fetch GitHub issue
def fetch_github_issue(owner, repo, issue_id):
    try:
        url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_id}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching issue {issue_id} from {owner}/{repo}: {e}")
        return None

# Endpoint to immediately fetch issues and download as JSON file
@app.route("/fetchIssues", methods=["POST"])
def fetch_issues():
    data = request.json
    repo_url = data["repoUrl"]
    issue_ids = data["issueIds"]

    owner, repo = repo_url.split("/")[-2], repo_url.split("/")[-1]
    
    issues_data = []
    for issue_id in issue_ids:
        issue_data = fetch_github_issue(owner, repo, issue_id)
        if issue_data:
            issues_data.append(issue_data)
    
    if not os.path.exists("issues"):
        os.makedirs("issues")
    
    # Saving the issues data into a JSON file
    filename = f"{owner}.{repo}.issues.json"
    with open(os.path.join("issues", filename), "w") as f:
        json.dump(issues_data, f, indent=4)
    
    # Return the file for download
    return send_file(
        os.path.join("issues", filename),
        as_attachment=True,
        download_name=filename
    )

# Hello endpoint
@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello, world!"})

# Run the Flask app
if __name__ == "__main__":
    print("hello")
    app.run(debug=True, host="0.0.0.0", port=5000)
