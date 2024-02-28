# 1-Mislo
# yoqtirgan_taomlar = ['grechka', 'somsa', 'qogirma_lagmon']

# yoqtirgan_taomlar.append('shashlik')

# yoqtirgan_taomlar.insert(2, 'manty') 
# yoqtirgan_taomlar_tuple = tuple(yoqtirgan_taomlar)

# print(yoqtirgan_taomlar_tuple)

# ------------------------------------------------------------------
# 2-misol
# I = ["A", "a", "B", "b", "C", "c", "D", "d"]

# katta_harflar = [x for x in I if x.isupper()]

# kichik_harflar = [x for x in I if x.islower()]

# harflar_tuple = (katta_harflar, kichik_harflar)

# print(harflar_tuple)

# ------------------------------------------------------------------
# 3-misol
# royxat = ["Akmal", "abror", "toxir", "Sobir", "Bakir", "jalil"]

# katta_boshlangan = [soz for soz in royxat if soz[0].isupper()]

# kichik_boshlangan = [soz for soz in royxat if soz[0].islower()]

# natija_tuple = (katta_boshlangan, kichik_boshlangan)

# print(natija_tuple)

# ------------------------------------------------------------------
# 4-misol
# p_numbers = ["+998991234567", "+79454874459", "+14385001031"]

# def alohida_raqamlar(royxat):
#     uzbekiston_raqamlari = [nomer for nomer in royxat if nomer.startswith("+998")]
    
#     russia_raqamlari = [nomer for nomer in royxat if nomer.startswith("+7")]
    
#     amerika_raqamlari = [nomer for nomer in royxat if nomer.startswith("+1")]

#     return (uzbekiston_raqamlari, russia_raqamlari, amerika_raqamlari)

# natija_tuple = alohida_raqamlar(p_numbers)
# print(natija_tuple)
# ------------------------------------------------------------------
# 5-misol
# n = 7 
# toq_sonlar = [i for i in range(1, 2+n, 2)]
# print(toq_sonlar)

# -----------------------------------------------------------------------------
# 6-savol
# sumbers = [386, 462, 47, 418, 907,
# 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 
# 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 
# 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527
# ]

# even_numbers = []

# for num in sumbers:
#     if num % 2 == 0:
#         even_numbers.append(num)
#     if num == 815:
#         break

# even_numbers.sort()
# print(even_numbers)
# -----------------------------------------------------------------------------
# 7-Savol
# my_dict = { 'apple': 3, 'banana': 8, 'orange': 6, 'grape': 5 }

# key = input("Kalit so'zni kiriting: ")

# if key in my_dict:
#     if my_dict[key] % 2 == 0:
#         print("Bu kalit-qiymat juftligi mavjud.")
#     else:
#         print("Bu kalit-qiymat juftligi mavjud emas.")
# else:
#     print("Bunday kalit mavjud emas.")
# print(even_numbers)
# -----------------------------------------------------------------------------
# 8-savol
# d = {'a': 1, 'b': 2, 'c': 3}

# yigindi = sum(d.values())

# print("Lug'at qiymatlarining yig'indisi:", yigindi)

# -----------------------------------------------------------------------------
# 9-savol
# d = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}

# yigindi = sum(d.keys())

# print("Lug'at kalitlarining yig'indisi:", yigindi)

# -----------------------------------------------------------------------------
# 10-savol
# n = int(input("n raqamini kiriting: "))  

# lugat = {x: x*x for x in range(1, n+1)}

# print("Kutilayotgan natija:", lugat)


# -----------------------------------------------------------------------------
# 11-savol
# lugat = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# yigindi = sum(lugat.values())

# ortacha = yigindi / len(lugat)

# print("Barcha qiymatlar yig'indisi:", yigindi)
# print("Arifmetik o'rtacha:", ortacha)
# -----------------------------------------------------------------------------
# 12-savol
# royxat_1 = ['a', 'b', 'c']
# royxat_2 = [1, 2, 3]

# lugat = dict(zip(royxat_1, royxat_2))

# print("Kalit: qiymat lug'ati:", lugat)


# son=int(input('Sonni kiriting: '))
# sonn=[]
# son_n=[]

# if son%2==0:
#     for i in range(0, son,2):
#         sonn.append(i)
#     print(sonn[::-1][0])


# elif son%2==1:
#     for i in range(1, son+1,2):
#         natija=(i-1)
#         son_n.append(natija)
#     print(son_n[::-1])

# Shunday kod yozingki. dasturda for operatoridan foydalaning.
# Dasturda ism kiritishni so`rang va shu ismdagi birinchi 3ta undosh harfni print qiling
