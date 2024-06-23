import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from bs4 import BeautifulSoup

import base64
import gptAPI

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def get_user_credentials(user_id):
    #  這部分是固定必要的不用動
    """獲取指定用戶的憑據."""
    creds = None
    token_file = f'token_{user_id}.json'
    
    # 如果有 token 檔案，載入保存的憑據.
    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)
    
    # 如果沒有可用的（有效的）憑據，執行 OAuth 流程.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # 保存憑據到 token 檔案.
        with open(token_file, 'w') as token:
            token.write(creds.to_json())
    
    return creds



def extract_text_from_html(html_content):
    """從 HTML 內容中提取純文本."""
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text()
    return text

def get_full_email_content(service):
    """獲取郵件的完整內容."""
    results = service.users().messages().list(userId='me', labelIds=['INBOX'], maxResults=5).execute()
    #     # result: 
#     {
#     'messages': [
#         {
#             'id': '1902ea8109630868', // 郵件的唯一標示符號
#             'threadId': '190245ae0ec4b7bd'  // 表示線程的標示符號，屬於同一個主題的轉發或回覆會有同一線程
#         }
#     ],
#     'nextPageToken': '12443339950340144510', //nextPageToken 是用於分頁的標記。在 Gmail API 中，當你的請求結果超過 maxResults 限制時，API 會返回一個 nextPageToken，你可以用這個標記來獲取下一頁的結果。 ex:  next_results = service.users().messages().list(userId='me', labelIds=['INBOX'], maxResults=10, pageToken=next_page_token).execute()
#     'resultSizeEstimate': 201 // resultSizeEstimate：一個估計值，表示符合查詢條件的郵件數量。 表示估計有 201 封郵件符合查詢條件。 可能是因為quota的原因無法一次全部拿取
#    }
    messages = results.get('messages', [])
    #     'messages': [
#     {
#         'id': '1902ea8109630868',
#         'threadId': '190245ae0ec4b7bd'
#     }
#    ]
    if not messages:
        print('沒有找到郵件.')
        return None
    msg_id = messages[0]["id"]

    try:
        message = service.users().messages().get(userId='me', id=msg_id, format='full').execute()
        payload = message.get('payload')
        parts = payload.get('parts')
        body = ""

        if not parts:
            # print(payload.get("mimeType"))
            mime_type = payload.get("mimeType")
            body = payload.get('body').get('data')
        else:
            # print(parts)
            for part in parts:
                mime_type = part.get('mimeType')
                if mime_type == 'text/plain':
                    body = part.get('body').get('data')
                    break

        if body:
            decoded_body = base64.urlsafe_b64decode(body).decode('utf-8')
            if mime_type == 'text/html': #另外處理html類型
                text_content = extract_text_from_html(decoded_body)
                return text_content
            return decoded_body
        else:
            return "郵件沒有文本內容"
    except HttpError as error:
        print(f'無法獲取郵件內容: {error}')
        return None

def main():
  # 創建憑證
  user_id = input("請輸入用戶 ID（例如，用戶的電子郵件地址）: ")
  creds = get_user_credentials(user_id)

  # 構建 Gmail API 服務對象.
  service = build('gmail', 'v1', credentials=creds) #parameter: servicename/version/credentials

  # 獲取最新郵件內容
  email_content = get_full_email_content(service)
    
  if email_content:
    #   # 將郵件內容寫入新檔案
    #   output_file = f'latest_email_{user_id}.txt'
    #   with open(output_file, 'w', encoding='utf-8') as f:
    #       f.write(email_content)
    #   print(f'最新郵件內容已寫入檔案 {output_file}')
    classification = gptAPI.classify_email(email_content)
    print(classification)

    reply_draft  = gptAPI.reply_email(email_content)
    print(reply_draft)



if __name__ == "__main__":
  main()