# Imports
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import base64

# Authenticate
token = {
    "token": "ya29.a0AeTM1idH3GhwMGiQJiK7R0Q7Xdrziqq4IPnDEZsNJP4Rz6XdrqLmoW7jVuMycGw2hxUKbTlp9cGhPBivFGX27wTkq9xgdLlsuERn8fRI7gHrAN-8d3sKX3uaYaraseLu9zs0ytRLiU1p86zN-yigrPOcWqh5aCgYKAVsSARMSFQHWtWOmn9A1P3mdqwq7MVlNIzOv5A0163", 
    "refresh_token": "1//0gWHqSS77F2i8CgYIARAAGBASNwF-L9IrrdNGaSFinvi-VrfbQknqiEIvqY9Q1P_8iZ3lWJloKmeAjaVN_IZtSHptITuTsukuCXo", 
    "token_uri": "https://oauth2.googleapis.com/token", 
    "client_id": "534271263620-nrnme5u8dhvjedo6loaus6gvb7724uio.apps.googleusercontent.com", 
    "client_secret": "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", 
    "scopes": ["https://mail.google.com/"]
    }

# Authenticate with a variable
creds = Credentials.from_authorized_user_info(token)

# If you choose to authenticate with a file, use this line instead
#creds = Credentials.from_authorized_user_file('token.json', SCOPES)

#Build the gmail client
service = build('gmail', 'v1', credentials=creds)

# for getting all the labels (Get Request)
def get():
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])
    for i in labels:
        print(i,'\n')

#For creating the labels (Post request)
def post(name='nood', labelListVisibility = 'labelShow', messageListVisibility='show'):
    label1={
        "labelListVisibility": labelListVisibility,
        "messageListVisibility": messageListVisibility,
        "name": name
    }

    results1 = service.users().labels().create(userId='me',body=label1).execute()
    return results1

#For updating the labels(Update Request)
def update(id = 'Label_2',name='mood', labelListVisibility = 'labelShow', messageListVisibility='show'):
    label2 = {
        "labelListVisibility": labelListVisibility,
        "messageListVisibility": messageListVisibility,
        "name": name
    }
    results3 = service.users().labels().update(userId='me',id=id,body=label2).execute()
    return results3

#For deleting the labels (Delete Request)
def delete(id='Label_1'):
    results2 = service.users().labels().delete(userId='me',id=id).execute()
    return results2



if __name__ == '__main__':
    post(name='green', labelListVisibility = 'labelShow', messageListVisibility='show')