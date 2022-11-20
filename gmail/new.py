# Imports
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import base64
from email.mime.text import MIMEText


# Authenticate
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly','https://www.googleapis.com/auth/gmail.modify']

token = {
    "token": "ya29.a0AeTM1ieI88h-2Io4jF8L_lBKpCJd2u5AIKE_fIcUNkSDFAC0DwEyXU-j6LeNSRNqpFAdWRSWPfaK20iNK_V_MEmku_SGzB8l3IrRAw6acadrAkntDiTLRHkw82srEbIGeyCsLQaBKgBh9d0M08lkezKAx0nfaCgYKAXwSARISFQHWtWOmajoTT4Nr9yK82FO3q8evxQ0163", 
    "refresh_token": "1//0g-afMaCT-EjXCgYIARAAGBASNwF-L9Irjqv5wPNP4bboDFBs_W9xBiS7zLLAJjVP5tikzsieUneDoDregxr6iAbzMNO--QPGWh8", 
    "token_uri": "https://oauth2.googleapis.com/token", 
    "client_id": "534271263620-nrnme5u8dhvjedo6loaus6gvb7724uio.apps.googleusercontent.com", 
    "client_secret": "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", 
    "scopes": ["https://mail.google.com/"], 
    "expiry": "2022-11-09T11:25:40.597884Z"
    }

# Authenticate with a variable
creds = Credentials.from_authorized_user_info(token, SCOPES)

# If you choose to authenticate with a file, use this line instead
#creds = Credentials.from_authorized_user_file('token.json', SCOPES)

service = build('gmail', 'v1', credentials=creds)
print(service)
results = service.users().messages().list(userId='me',maxResults=10).execute()
mes_list = results.get('messages',[])

print(mes_list)
