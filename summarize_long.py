import requests
import time

# Replace with your Azure endpoint and subscription key
#endpoint = "https://<your-endpoint>.cognitiveservices.azure.com/"
subscription_key = "axxxxxxxxxxxxxxxxxxxxxx"
endpoint = "https://xxxxxxxxxxx.cognitiveservices.azure.com/"
api_key = "xxxxxxxxxxxxxxxxxxxxxxx"

# Define the URL for creating the job
url = f"{endpoint}/language/analyze-text/jobs?api-version=2022-05-01"

with open('long_transkript.txt', 'r') as file:
    # Read the contents of the file into a variable
    file_contents = file.read()

# Text to be summarized
text_to_summarize = file_contents

# Define the headers
headers = {
    "Ocp-Apim-Subscription-Key": subscription_key,
    "Content-Type": "application/json"
}

# Define the request body
body = {
    "analysisInput": {
        "documents": [
            {"id": "1", "language": "en", "text": "Your text to summarize goes here."}
        ]
    },
    "tasks": {
        "extractiveSummarizationTasks": [
            {
                "parameters": {
                    "model-version": "latest",
                    "sentenceCount": 3
                }
            }
        ]
    }
}

# Send the POST request to create the job
response = requests.post(url, headers=headers, json=body)
response.raise_for_status()

# Get the operation location from the response headers
operation_location = response.headers["operation-location"]

# Poll the operation location to get the job status and results
while True:
    result_response = requests.get(operation_location, headers=headers)
    result_response.raise_for_status()
    result = result_response.json()

    # Check if the job is completed
    if result["status"] == "succeeded":
        break
    elif result["status"] == "failed":
        raise Exception("Job failed")

    # Wait before polling again
    time.sleep(5)

# Print the results
print(result)
