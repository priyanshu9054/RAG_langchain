import requests

# response= requests.post(
#     "http://127.0.0.1:8000/essay/invoke", 
#     json={'input':{'topic':"future of llms"}}
#     )
# print(response.json())

response= requests.post(
    "http://127.0.0.1:8000/essay/invoke", 
    json={'input':{'topic':"Which company has best chance of wining in large language models rat race?"}}
    )
print(response.json()['Output'])