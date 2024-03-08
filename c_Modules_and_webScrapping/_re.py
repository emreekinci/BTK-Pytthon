import re
# result = dir(re)

# re module

# re.findall()
str = "Python  is a great programming language | Python  40 50 400 hours"
# result = re.findall("Python", str)

# re.split()
# result = re.split(" ",str)

# re.sub()
# result = re.sub(r'\s', '', str) # remove all white spaces --> \s = " "
# result = re.sub(" ", "-", str) # replace space with -

# re.search
# result = re.search("Python", str)

# result1 = result.span()     #  return the position of match --> (start, end)
# result2 = result.start()    # start of matched string
# result3 = result.end()      #  end of matched string
# result4 = result.group()    #  matched string itself
# result5 = result.string     # The original string passed to search().
# print(result1, result2,  result3,  result4, result5)

result = re.findall("[abc]",str)
result = re.findall("[sat]", str)
result = re.findall("[a-e]",str)
result = re.findall("[a-z]", str)  
result = re.findall("[0-5]",str)
result = re.findall("[^0-9]",str)
result = re.findall("[^abc]",str) # negation [^abc] means not abc
result = re.findall("...",str) #   three dots represent any character
result = re.findall("Py...n",str) # Matches Py and followed by three characters n
result = re.findall("^P",str) #  Match only at the beginning of the line 
result = re.findall("s$",str) #  Match only at the End of the Line
result = re.findall("hours$",str) #  Match 'hours' at the end of the line
result = re.findall("hourss$",str) #  Match 'hours' at the end of the line
result = re.findall("hour*s",str) #  * matches zero or more occurrences of preceding RE
result = re.findall("program+ming",str) #  + matches one or more occurrences of preceding RE
result = re.findall("m{2}",str) # {n} -- matches exactly n occurrences of preceding RE
result = re.findall("[0-9]{2,3}",str) #   {n, m} -- matches between n and m occurrences of preceding RE   

result = re.findall("\APython", str) # Match only at the Start of the String
result = re.findall("hours\Z", str) #    Match only at the End of the String
print(result)

# Regular Expression

# RegEx veya Normal İfade, bir arama modeli oluşturan bir karakter dizisidir.

# RegEx, bir dizenin belirtilen arama modelini içerip içermediğini kontrol etmek için kullanılabilir.

# RegEx Modülü
# rePython'un Normal İfadelerle çalışmak için kullanılabilecek yerleşik bir paketi vardır .

# Modülü içe aktarın re:

# import re
# Python'da RegEx
# Modülü içe aktardığınızda re normal ifadeleri kullanmaya başlayabilirsiniz:

# Örnek
# "The" ile başlayıp "Spain" ile bitip bitmediğini görmek için dizeyi arayın:

# import re

# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# RegEx İşlevleri
# Modül re, bir dizede eşleşme aramamıza olanak tanıyan bir dizi işlev sunar:

# Function	Description
# findall	    Returns a list containing all matches
# search	    Returns a Match object if there is a match anywhere in the string
# split	    Returns a list where the string has been split at each match
# sub	        Replaces one or many matches with a string

# Meta karakterler
# Meta karakterler özel bir anlamı olan karakterlerdir:

# Character	Description                                                     	        Example	
# []	        A set of characters	"[a-m]"	
# \	        Signals a special sequence (can also be used to escape special characters)	"\d"	
# .	        Any character (except newline character)	                                "he..o"	
# ^	        Starts with	                                                                "^hello"	
# $	        Ends with	                                                                "planet$"	
# *	        Zero or more occurrences	                                                "he.*o"	
# +	        One or more occurrences	                                                    "he.+o"	
# ?	        Zero or one occurrences	                                                    "he.?o"	
# {}	        Exactly the specified number of occurrences	                                "he.{2}o"	
# |	        Either or	                                                                "falls|stays"	
# ()	        Capture and group	 
	 
# Özel Diziler
# Özel bir dizi, \ aşağıdaki listede yer alan karakterlerden birinin ardından gelir ve özel bir anlama sahiptir:

# Character	Description	                                                                                                Example	
# \A	        Returns a match if the specified characters are at the beginning of the string	                            "\AThe"	

# \b	        Returns a match where the specified characters are at the beginning or at the end of a word                 r"\bain"
#             (the "r" in the beginning is making sure that the string is being treated as a "raw string")	            r"ain\b"
                                                                                                                                                                                                       	
# \B	        Returns a match where the specified characters are present,but NOT at the beginning(or at the end) of a word r"\Bain"
#             (the "r" in the beginning is making sure that the string is being treated as a "raw string")	            r"ain\B" 
	

# \d	        Returns a match where the string contains digits (numbers from 0-9)                                          "\d"	
# \D	        Returns a match where the string DOES NOT contain digits	                                                 "\D"	
# \s	        Returns a match where the string contains a white space character	                                         "\s"	
# \S	        Returns a match where the string DOES NOT contain a white space character	                                 "\S"	
# \w	        Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character) 	"\w"	
# \W	        Returns a match where the string DOES NOT contain any word characters	                                    "\W"	
# \Z	        Returns a match if the specified characters are at the end of the string	                                "Spain\Z"	

# Setler
# []Küme, bir çift köşeli parantez içindeki özel bir anlamı olan bir karakter kümesidir :

# Set	    Description	
# [arn]	Returns a match where one of the specified characters (a, r, or n) is present	
# [a-n]	Returns a match for any lower case character, alphabetically between a and n	
# [^arn]	Returns a match for any character EXCEPT a, r, and n	
# [0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
# [0-9]	Returns a match for any digit between 0 and 9	
# [0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
# [a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
# [+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string	
 
# findall() İşlevi
# İşlev findall(), tüm eşleşmeleri içeren bir liste döndürür.

# Örnek
# Tüm eşleşmelerin listesini yazdırın:

# import re

# txt = "The rain in Spain"
# x = re.findall("ai", txt)
# print(x)
# Liste, eşleşmeleri bulunma sırasına göre içerir.

# Hiçbir eşleşme bulunamazsa boş bir liste döndürülür:

# Örnek
# Eşleşme bulunmazsa boş bir liste döndürün:

# import re

# txt = "The rain in Spain"
# x = re.findall("Portugal", txt)
# print(x)
 
# search() İşlevi
# İşlev search(), dizede bir eşleşme arar ve bir eşleşme varsa bir Match nesnesi döndürür.

# Birden fazla eşleşme varsa eşleşmenin yalnızca ilk oluşumu döndürülür:

# Örnek
# Dizedeki ilk boşluk karakterini arayın:

# import re

# txt = "The rain in Spain"
# x = re.search("\s", txt)

# print("The first white-space character is located in position:", x.start())
# Hiçbir eşleşme bulunamazsa değer None döndürülür:

# Örnek
# Hiçbir eşleşme sağlamayan bir arama yapın:

# import re

# txt = "The rain in Spain"
# x = re.search("Portugal", txt)
# print(x)
 
# split() İşlevi
# İşlev, split() dizenin her eşleşmede bölündüğü bir liste döndürür:

# Örnek
# Her boşluk karakterine bölün:

# import re

# txt = "The rain in Spain"
# x = re.split("\s", txt)
# print(x)
# Parametreyi belirterek oluşum sayısını kontrol edebilirsiniz maxsplit :

# Örnek
# Dizeyi yalnızca ilk geçtiği yerde bölün:

# import re

# txt = "The rain in Spain"
# x = re.split("\s", txt, 1)
# print(x)
 
# sub() İşlevi
# İşlev sub(), eşleşmeleri seçtiğiniz metinle değiştirir:

# Örnek
# Her boşluk karakterini 9 rakamıyla değiştirin:

# import re

# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt)
# print(x)
# Parametreyi belirterek değiştirme sayısını kontrol edebilirsiniz count :

# Örnek
# İlk 2 tekrarı değiştirin:

# import re

# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt, 2)
# print(x)
 
# Nesneyi Eşleştir
# Eşleşme Nesnesi, arama ve sonuç hakkında bilgi içeren bir nesnedir.

# Not: Eşleşme yoksa NoneEşleştirme Nesnesi yerine değer döndürülür.

# Örnek
# Eşleşme Nesnesini döndürecek bir arama yapın:

# import re

# txt = "The rain in Spain"
# x = re.search("ai", txt)
# print(x) #this will print an object
# Match nesnesi, arama ve sonuç hakkında bilgi almak için kullanılan özelliklere ve yöntemlere sahiptir:

# .span()  eşleşmenin başlangıc ve bitis konumlarını içeren bir tanımlama grubu döndürür.
# .string  işleve iletilen dizeyi döndürür,
# .group() dizenin eşleşme olan kısmını döndürür
# Örnek
# İlk eşleşme oluşumunun konumunu (başlangıç ve bitiş konumu) yazdırın.

# Normal ifade, büyük harf "S" ile başlayan sözcükleri arar:

# import re

# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.span())

# Örnek
# İşleve iletilen dizeyi yazdırın:

# import re

# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.string)

# Örnek
# Dizenin eşleşme olan kısmını yazdırın.

# Normal ifade, büyük harf "S" ile başlayan sözcükleri arar:

# import re

# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.group())
# Not: Eşleşme yoksa NoneEşleştirme Nesnesi yerine değer döndürülür.

