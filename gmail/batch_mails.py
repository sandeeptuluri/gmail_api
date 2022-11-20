# Imports
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import base64
#from bs4 import BeautifulSoup

token = {
    "token": "ya29.a0AeTM1if0iQurqhZL-FVvNesD2BLq24bx3Tth7PttJ0BBGoaskBCsBkkLNQ6f1HlNFx_n3vvxs4AKTiSgLUhgTg8HbhiIP6ts7RDfuePl0asprDtF7HHBnv8azEqQXoKrvk5vvDh-wL7EhQzWlxtHn3Aq0wRdaCgYKAbsSARISFQHWtWOmwFCoAy68CYk7MF4w5UpWVA0163", 
    "refresh_token": "1//0gvy_gy-qHyZ6CgYIARAAGBASNwF-L9Irl5DVP9Op0TOzY-rLwVDao5oYL9GhUdZxTNMKgLIdduEwLdMhVDp5mo8IxNBLx0tiTSg", 
    "token_uri": "https://oauth2.googleapis.com/token", 
    "client_id": "534271263620-nrnme5u8dhvjedo6loaus6gvb7724uio.apps.googleusercontent.com", 
    "client_secret": "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", 
    "scopes": ["https://mail.google.com/"]
    }

#creds
creds = Credentials.from_authorized_user_info(token)

#building the client
service = build('gmail', 'v1', credentials=creds)
print(service)
#getting the messages ID's
results = service.users().messages().list(userId='me',maxResults=500).execute()
mes_list = results.get('messages')
print(mes_list)
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

# id_list = []
# for id in range(0, len(mes_list), 50):
#     id_list.append(mes_list[id:id+50])

# # print(id_list)

# def get_messages(a, b ,c):
#     try:
#         print(b)

#     except Exception as e:
#         print(b['snippet'])

# def messages():
#     k = 0
#     while k < len(id_list):
#         batch_request = service.new_batch_http_request()
#         for j in id_list[k]:
#             # print(j['id'])
#             batch_request.add(service.users().messages().get(userId='me',id=j['id']),callback= get_messages)
#         batch_request.execute()
#         k += 1


# if __name__ == '__main__':
#     messages()