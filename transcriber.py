from googleapiclient.discovery import build
from google.oauth2 import service_account

# Define the required scope for Google Drive access
SCOPES = ['https://www.googleapis.com/auth/drive']
# Path to your service account JSON file
SERVICE_ACCOUNT_CREDENTIALS = 'credentials.json'
# Parent folder ID in Google Drive (empty string for root)
PARENT_FOLDER_ID = ""


def create_drive_service():
    try:
        # Create credentials using service account
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_CREDENTIALS, scopes=SCOPES)

        # Build the Drive API service
        service = build('drive', 'v3', credentials=credentials)
        return service

    except Exception as e:
        print(f"Error creating Drive service: {str(e)}")
        return None


def list_files(service):
    try:
        # Call the Drive v3 API to list files
        results = service.files().list(
            pageSize=10,
            fields="nextPageToken, files(id, name)"
        ).execute()

        files = results.get('files', [])

        if not files:
            print('No files found.')
        else:
            print('Files:')
            for file in files:
                print(f"{file['name']} ({file['id']})")

    except Exception as e:
        print(f"Error listing files: {str(e)}")


def main():
    service = create_drive_service()
    if service:
        list_files(service)


if __name__ == '__main__':
    main()