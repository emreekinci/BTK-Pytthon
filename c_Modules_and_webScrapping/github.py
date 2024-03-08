import requests
import json
# https://api.github.com/users/emreekinci
# https://api.github.com/users/emreekinci/repos

# eger API üzerinden repo olusturmak istiyorsak personel token oluşturuyoruz: https://github.com/settings/tokens  --> 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

class Github:
    def  __init__(self):
        self.api_url = 'https://api.github.com'
        self.token = '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'
        
    def getUser(self, username):
        response = requests.get(self.api_url + '/users/' + username) # 'https://api.github.com/users/username'   
        return response.json()
        
    def getRepositories(self, username):
        response = requests.get(self.api_url + '/users/' + username + '/repos')
        return response.json()
    
    def createRepository(self, name):
        response = requests.post(self.api_url+'/user/repos?access_token='+ self.token, json={
            "name": name,
            "description": "This is a test repo for Python",
            "homepage": "https://github.com",
            "private": False,    
            "has_issues": True,  
            "has_projects": True,
            "has_wiki": True
        })
        return response.json()
        
github = Github()
      
while True:
    secim = input('1- Find user\n2- Get repo\n3- Create repo\n4- Exit\nSeçim: ')
    
    if secim == '4':
        break
    else:
        if secim == '1':
            username = input('username: ')
            result = github.getUser(username)
            print(f"name: {result['name']}\npublic repos:{result['public_repos']}\nfallowers: {result['followers']}")
        elif secim == '2':
            username = input('username: ')
            result = github.getRepositories(username)
            for repo in result:
                print(repo['name']) 
                         
        elif secim == '3': # Buraya tekrar bak hata !!
            name = input('repository name: ')
            result = github.createRepository(name)
            print(result)
        else:
            print('False choose !!')

# https://developer.github.com/changes/2020-02-10-deprecating-auth-through-query-param/