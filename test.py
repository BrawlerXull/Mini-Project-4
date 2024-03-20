import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/drive"]

creds = None

flow = InstalledAppFlow.from_client_secrets_file("miniProject.json", SCOPES)
creds = flow.run_local_server()

# Save the credentials to a file for future use
with open('token.json', 'w') as token:
    token.write(creds.to_json())

try:
    service = build("drive", "v3", credentials=creds)
    response = service.files().list(
        q="name='Backup' and mimeType='application/vnd.google-apps.folder'",
        spaces='drive'
    ).execute()

    if not response['files']:
        file_metadata = {
            "name": "Backup",
            "mimeType": "application/vnd.google-apps.folder"
        }

        file = service.files().create(body=file_metadata, fields="id").execute()

        folder_id = file.get('id')
    else:
        folder_id = response['files'][0]['id']

    for file_name in os.listdir('py/files'):
        files_metadata = {
            "name": file_name,
            "parents": [folder_id]
        }

        # Check if the file already exists in the specified folder
        existing_files = service.files().list(
            q=f"name='{file_name}' and '{folder_id}' in parents",
            fields="files(id)"
        ).execute().get('files', [])

        if not existing_files:
            media = MediaFileUpload(f"py/files/{file_name}")

            # Upload the file to Google Drive
            upload_file = service.files().create(body=files_metadata, media_body=media, fields="id").execute()
            print("Backed up file:", file_name)

            # Close the file after uploading
            media.stream().close()

            # Delete the file from the system after it has been backed up
            os.remove(f"py/files/{file_name}")
            print("Deleted file from system:", file_name)
        else:
            print("File already exists in Google Drive, skipping upload:", file_name)

except HttpError as e:
    print("Error:", str(e))
