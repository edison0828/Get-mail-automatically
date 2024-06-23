from openai import OpenAI
# from config import OPENAI_API_KEY
client = OpenAI(
                api_key="sk-pyOxYsfswWkTk7RXt5IWL5nTe6a8PqAUtZy0Vz3u3ZWC0nSV",
                base_url="https://api.chatanywhere.cn"
    )

def classify_email(email_content):
    messages = [
        {"role": "system", "content": "你是一個幫忙分類電子郵件的小幫手"},
        {"role": "user", "content": f"請根據以下電子郵件內容給出一個簡潔的分類標籤（例如：工作，個人，緊急，垃圾郵件等），只要給我分類就好。\n\n郵件內容：{email_content}"}
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=20 
    )
    classification = response.choices[0].message.content.strip()
    return classification 

def reply_email(email_content):
    messages = [
        {"role": "system", "content": "你是一個幫忙生成回信草稿的助手。"},
        {"role": "user", "content": f"請根據以下電子郵件內容生成一封回信草稿。\n\n郵件內容：{email_content}"}
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=200  
    )

    reply_draft = response.choices[0].message.content.strip()
    return reply_draft



# # read file
# with open('email.txt', 'r', encoding='utf-8') as file:
#     email_content = file.read()



# classification = classify_email(email_content)
# print(classification)

# reply_draft  = reply_email(email_content)
# print(reply_draft)
