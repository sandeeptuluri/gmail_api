# Imports
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import base64
from bs4 import BeautifulSoup

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

service = build('gmail', 'v1', credentials=creds)
print(service)
results = service.users().messages().list(userId='me').execute()
mes_list = results.get('messages')
print(len(mes_list))