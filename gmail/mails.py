# Imports
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import base64
#from bs4 import BeautifulSoup

# Authenticate
token = {
    "token": "ya29.a0AeTM1ic7MyzqEjF3dckygxtgPhXGosNdWjXvfnEuxvxI7GrU8tgoYiuLvbp4r5dn2PXHZjDdfQkHWJTdH5p-bZAqLnyFLCmY-ONFeqbB3oA7OrMyI4gIvtaePIz1_Nw8BH-vKCSlXJPQx9xSPnpR8rUN6v0VaCgYKAVISARESFQHWtWOmCFQtJEoDV1bXuExadFLbSg0163", 
    "refresh_token": "1//0gBGMgiqDVSZqCgYIARAAGBASNwF-L9IrwzjPR6ym77yZy4r2QNN9GNJc6I6UFqeu3XqvnN8N-f9Y7esF3w__4twC4NOHeakeLvo", 
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
# print(service)
results = service.users().messages().list(userId='me',maxResults=500).execute()
mes_list = results.get('messages')

next_page_token = None
if 'nextPageToken' in results:
    next_page_token = results.get('nextPageToken')

while next_page_token:
    results1 = service.users().messages().list(userId='me',maxResults=500,pageToken=next_page_token).execute()
    new_list = results1.get('messages')
    for i in new_list:
        mes_list.append(i)
    print(len(new_list))
    if 'nextPageToken' not in results1:
        break
    else:
        next_page_token = results1.get('nextPageToken')

print(len(mes_list))


#print(mes_list)
#print(results.keys())
# es_list = results.get('messages')
# print(len(mes_list))





# def get_one_message():

#     results = service.users().messages().list(userId='me').execute()
#     mes_list = results.get('messages')
#     #print(mes_list)

#     id = mes_list[3]['id']
#     txt = service.users().messages().get(userId='me',id=id).execute()
#     payload = txt['payload']
#     headers = payload['headers']

#     for i in headers:
#         if i['name'] == 'Subject':
#             subject = i['value']
#         if i['name'] == 'From':
#             sender = i['value']

#     parts = payload.get('parts')[0]
#     data = parts['body']['data']
#     data = data.replace("-","+").replace("_","/")
#     decoded_data = base64.b64decode(data)

#     #Soup object for decoding the data
#     soup = BeautifulSoup(decoded_data , "html.parser")
#     print("Subject: ", subject)
#     print("From: ", sender)
#     print("Message: ", soup)
#     print('\n')

# def get_all_messages():

#     results = service.users().messages().list(userId='me').execute()
#     mes_list = results.get('messages')

#     for msg in mes_list:
#         txt = service.users().messages().get(userId='me',id=msg['id']).execute()
#         #print(txt)
        
#         try:
#             payload = txt['payload']
#             headers = payload['headers']

#             for i in headers:
#                 if i['name'] == 'Subject':
#                     subject = i['value']
#                 if i['name'] == 'From':
#                     sender = i['value']

#             parts = payload.get('parts')[0]
#             data = parts['body']['data']
#             data = data.replace("-","+").replace("_","/")
#             decoded_data = base64.b64decode(data)

#             #Soup object for decoding the data
#             soup = BeautifulSoup(decoded_data , "html.parser")
  
#             print("Subject: ", subject)
#             print("From: ", sender)
#             print("Message: ", soup)
#             print('\n')

#         except Exception as e:
#             print(e)

# if __name__ == '__main__':
#     get_one_message()