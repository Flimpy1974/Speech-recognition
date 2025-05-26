import openai

# Replace with your key and endpoint


with open('./result/parl1.mp4.rtf', 'r') as file:
    # Read the contents of the file into a variable
    file_contents = file.read()

# Text to be summarized
text_to_summarize = "Summarize the following text in german:\n---\n"+file_contents+"\n---"




use_azure_active_directory = False  # Set this flag to True if you are using Azure Active Directory
if not use_azure_active_directory:
    endpoint = "https://xxxxxxxxxxx.openai.azure.com/"
    api_key = "8xxxxxxxxxxxxxxxxxxxxxxxx"

    client = openai.AzureOpenAI(
        azure_endpoint=endpoint,
        api_key=api_key,
        api_version="2023-09-01-preview"
    )

# Call the OpenAI API for summarization
response = client.chat.completions.create(
    model="gpt-35-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": text_to_summarize}
    ]
)

# response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "Summarize the following text:\n\n{text_to_summarize}"}
#     ]
# )

# Print the summary
summary = response.choices[0].message.content
print("Summary:", summary)

with open('./result/parl1.mp4_summary.txt', 'w') as file:
    # Write text to the file
    file.write(summary)