import json

# dict
person_str = '{ "name":"Emre", "languages":["Python","Java"] }'
# str values must be convert dict value
# result = person["name"]
# result2 = person["languages"]
# result3 = person["languages"[0]]

# json string to dict for person
person_dict = json.loads(person_str)
# print(person_dict)
# print(type(person_dict))  # <class   'dict'>
p_name = person_dict[u'name']
print("Person name is : ", p_name)
# p_lan = person_dict[u'languages']
# print("Person languages are: ",p_lan)

# languages = person_dict['languages']
# print("\nLanguages are: ")
# for language in languages:
#     print(language)

# try:
#     notexistent_key = person_dict['notexist']
# except KeyError as e:
#     print("\nKey error occurred!")
#     print("The key does not exist.")    
#     print("Message: %s" % e)
    
# with open("person.json") as f:
#     data_json= json.load(f) 
#     print(data_json["name"])
#     print(data_json["languages"])

person_dict2 = {
    "name": "Hakan",
    "languages": ["Python", "C","C#",  "Javascript"],
    "age": 28,
}

# dict to json string
# result = json.dumps(person_dict2) #  return a string    
# print(f"Result: {result} and type : {type(result)}")   
# # print(result["name"]) non accesable

# write  the dictionary into a file
# with open("person.json","w") as f2:
#     json.dump(person_dict2,f2)

person_dict2 = json.loads(person_str)
result2 = json.dumps(person_dict2,  indent=4, sort_keys=True) # pretty printed
print(person_dict)
print(result2)


# json documents area:

# JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate. It is based on a subset of the JavaScript Programming Language, Standard ECMA-262 3rd Edition - December 1999.

# JSON is a text format that is completely language independent but uses conventions that are familiar to programmers of the C-family of languages, including C, C++, C#, Java, JavaScript, Perl, Python, and many others. These properties make JSON an ideal data-interchange language.

# JSON Syntax

# JSON data is written as key-value pairs, just like Python dictionaries.
# Key must be a string.
# Value can be a string, number, boolean expression, array, object, or null.
# Key and value are separated by a colon.
# Each key-value pair is separated by a comma.
# Curly braces hold objects, and square brackets hold arrays.
# Here's an example of JSON syntax:

# json
# Copy code
# {
#   "name": "John Doe",
#   "age": 30,
#   "city": "New York",
#   "skills": ["Python", "Java", "C#"],
#   "active": true,
#   "settings": null
# }
# JSON in Python

# Python has built-in support for JSON with the json module.

# json.dumps(): Convert a Python object (dict, list, string, int, float, bool, or None) to a JSON string.
# json.dump(): Write a Python object as a JSON formatted string to a file.
# json.loads(): Convert a JSON string to a Python object.
# json.load(): Read a JSON formatted string from a file and convert it to a Python object.
# For more information on JSON and the json module in Python, you can refer to the official documentation:

# JSON: https://www.json.org/json-en.html
# Python json module: https://docs.python.org/3/library/json.html