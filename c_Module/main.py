import module_

#result = help(module_)
# result = help(module_.func)
# print(result)

result2 = module_.number
result3 = module_.numbers  

result4 = module_.person["name"]
result5 = module_.person["age"]
result6 = module_.func(10)

p = module_.Person()
p.walk()

print(result2)
print(result3)

print(result4)
print(result5)
print(result6)



    
    # Modül yerleri:
    # vscode -> terminal -> powershell:python->
    
    # >>> import sys
    # >>> sys.path
    # ['', 'C:\\Users\\asus\\AppData\\Local\\Programs\\Python\\Python312\\python312.zip',
    # 'C:\\Users\\asus\\AppData\\Local\\Programs\\Python\\Python312\\DLLs',
    # 'C:\\Users\\asus\\AppData\\Local\\Programs\\Python\\Python312\\Lib',
    # 'C:\\Users\\asus\\AppData\\Local\\Programs\\Python\\Python312',
    # 'C:\\Users\\asus\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages']

    # >>> sys.builtin_module_names
    # ('_abc', '_ast', '_bisect', '_blake2', '_codecs', '_codecs_cn', '_codecs_hk', '_codecs_iso2022', '_codecs_jp', '_codecs_kr', '_codecs_tw', '_collections', '_contextvars', '_csv', '_datetime', '_functools', '_heapq', '_imp', '_io', '_json', '_locale', '_lsprof', '_md5', '_multibytecodec', '_opcode', '_operator', '_pickle', '_random', '_sha1', '_sha2', '_sha3', '_signal', '_sre', '_stat', '_statistics', '_string', '_struct', '_symtable', '_thread', '_tokenize', '_tracemalloc', '_typing', '_warnings', '_weakref', '_winapi', '_xxinterpchannels', '_xxsubinterpreters', 'array', 'atexit', 'audioop', 'binascii', 'builtins', 'cmath', 'errno', 'faulthandler', 'gc', 'itertools', 'marshal', 'math', 'mmap', 'msvcrt', 'nt', 'sys', 'time', 'winreg', 'xxsubtype', 'zlib')
    
 