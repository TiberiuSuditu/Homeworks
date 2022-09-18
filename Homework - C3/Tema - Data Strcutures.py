print('''Declară o listă care conține elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine)
----->''')
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print('Lista mea este:', my_list)

print('''Afișează lista inițială ordonată ascendent (lista inițială trebuie păstrată în aceeași formă)
----->''')
print(sorted(my_list))
print(my_list) #lista nu s-a modificat

print('''Afișează lista inițială ordonată descendent (lista inițială trebuie păstrată în aceeași formă)
----->''')
print(sorted(my_list, reverse = True))
print(my_list) #lista nu s-a modificat

print('''Afișează o listă ce conține numerele pare din lista ordonată (folosind slice)
----->''')
my_list1 = sorted(my_list)
print(my_list1[1:len(my_list1):2])
print(my_list) #lista nu s-a modificat

print('''Afișează o listă ce conține numerele impare din lista ordonată (folosind slice)
----->''')
print(my_list1[0:len(my_list)-1:2])
print(my_list) #lista nu s-a modificat

print('''Afisează o listă ce conține numerele ce sunt multipli ai numărului 3 (folosind slice)
----->''')
print(my_list1[2:len(my_list1)-1:3])
print(my_list) #lista nu s-a modificat









