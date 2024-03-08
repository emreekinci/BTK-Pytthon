html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web Scrapping</title>
</head>
<body>
<h1 id="header">Python Kurs İçeriği</h1>
    
    <div class="group-1">
        <h2>Programlama</h2>
        <ul>
            <li>Menü1</li>
            <li>Menü2</li>
            <li>Menü3</li>
            <li>Menü4</li>
            <li>Menü5</li>
        </ul>
    </div>

    <div class="group-2">
        <h2>Modüller</h2>
        <ul>
            <li>os</li>
            <li>request</li>
            <li>BeatifulSoap</li>
            <li>Json</li>
            <li>re</li>
            <li>datetime</li>
        </ul>
    </div>
    <div class="group-3">
        <h2>Django</h2>
        <ul>
            <li>security</li>
            <li>validation</li>
            <li>Admin Panel</li>
            <li>Template</li>
            <li>Design</li>
            <li>Verification</li>
        </ul>
    </div>  
    <a class= "sister1" href="http://example1.com/elsie" id="link1">Link1</a><br>
    <a class= "sister2" href="http://example2.com/elsie" id="link1">Link1</a><br>
    <a class= "sister3" href="http://example3.com/elsie" id="link1">Link1</a><br>
  
</body>
</html>
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen

soup = BeautifulSoup(html_doc, 'html.parser') #  parse the html document with parser

# res = soup.prettify()
# res2 = soup.title 
# res3 = soup.head
# res4  = soup.body
# res5 = soup.title.name
# res6 = soup.title.string

# print(f"\n***************\ntitle: {res2}\nhead: {res3}\nbody: {res4}\ntitle_name: {res5}\ntitle_str: {res6}")

# res_h1 = soup.h1 # get all h1 tags in the page
# res_h2 = soup.h2  # get all h2 tags in the page
# res_h2_name = soup.h2.name   # get name of h2 tag
# res_h1_str = soup.h1.string
# res_h2_str = soup.h2.string   # get string inside h2 tag (text between opening and closing tag)

# print("------------------------------")
# print(res_h1_str)

# res1 = soup.findAll('h2')# find all h2 tags that contain specific text
# res2 = soup.findAll('h2')[0]
# res3 = soup.findAll('h2')[1]
# print(res1)

# res = soup.div # first div
# res2 = soup.findAll('div')[0] 
# res3 = soup.find_all('div')[1] # second div
# res4 = soup.find_all('div')[1].ul  # ul within the second div
# res5 = soup.find_all('div')[1].ul.li  # li's within the ul within the second div
# res6 = soup.find_all('div')[1].ul.find_all('li') 
# print("\n\n------------------------------")
# print(res6)

res = soup.div.findChildren()
res = soup.div.findNextSibling().findNextSibling() # div1->div2->[div3]
res = soup.div.findNextSibling().findNextSibling().find_previous_sibling() # div1->div2->div3->[div2]

res = soup.find_all('a')
print(res)

for link in res:
    #print(link) 
    print(link.get('href'))




