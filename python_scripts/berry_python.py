import requests


URL = "linkapi"
TOKEN = "token numero"

response = requests.post(URL,
                         json={
  "query": """ query { 
                me {
                    
                    }
                    } """
  })
print (response.text)
