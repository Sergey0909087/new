# 1 zadanie
str_2 = str(input("Введи строку: "))
print(str_2[::-1])

# 2 zadanie
vvedi_stroku = str(input("Введи строку: "))
print(vvedi_stroku.isalpha()) #bukvennie simvoli
print(vvedi_stroku.isdigit()) #chislovie simvoli
for char in vvedi_stroku:
    if char.isalpha():
        pass