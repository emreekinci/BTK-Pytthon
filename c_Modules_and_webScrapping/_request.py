import requests # pip install requests
import json

# import json
# print(json.__file__)
# terminal : 
# pip --version              
# pip list
# web --> jsonplaceholder : https://jsonplaceholder.typicode.com/

result = requests.get("https://jsonplaceholder.typicode.com/todos")#    send a request to the server and get response
#result = result.text # <class 'str'>
result = json.loads(result.text) # #<class 'list'>
#print(result)
#print(type(result))
print(result[0]["title"])
print(result[0])
#print(result)
for i in result:
    if i["userId"] == 1: # filtering     by userId=1
        print(i)
