my_string = 'heLl0 wORLD go go go'
# method radace registra stroki
print(my_string.capitalize()) #perevod pervoi bukvi v verhni registr, ostalnie v nijni
print(my_string.lower()) #perevod vseh bukvennih simvolov v nijni registr
print(my_string.upper()) # perevod vseh bukvennih simvolov v verhni registr
print(my_string.title()) # perevod vseh pervih bukv slov v verhni registr, ostalnie v nijni
print(my_string.swapcase()) #zamena registra vseh bukvennih simvolov na protivopolojni

# method poisca podstroki v stroke
print(my_string.count('go', 1)) #podschet kolichestva fragmenta v stroke
print(my_string.find('go')) #poisk podstroki v stroke, ne nashel = -1
print(my_string.index('go')) #poisk podstroki v stroke, ne nashel = -vizov isclucheniya
print(my_string.rfind('go')) #poisk s prava na levo
print(my_string.rindex('go')) #poisk sprava na levo

#method proverki strok
new_string = 'Hello World'
print(new_string.isalnum()) #bukvi i chisla
print(new_string.isalpha()) #bukvennie simvoli
print(new_string.isdigit()) #chislovie simvoli
print(new_string.islower()) #vse bukvennie simvoli v nijnem registre
print(new_string.isupper()) #vse bukvennie simvoli v verhnem registre
print(new_string.isspace()) #stroka sostoit tolko iz probelnih simvolov
print(new_string.istitle()) #vse slova stroki nachinautsa s verhnego registra, ostalnie v nijnem