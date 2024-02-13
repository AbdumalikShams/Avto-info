def avto_info(make, modeli, rangi, yili,karobka, narxi = None):
    """Avto haqidagi malumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    avto = {
        'make':make,
        'model':modeli,
        'rang':rangi,
        'yil':yili,
        'karobka':karobka,
        'narx':narxi
        }
    return avto

def enter_avto():
    """Foydalanuvchidan avto ma'lumotlarini qabul qilib ro'yxat qaytaruvchi funksiya"""
    avtolar = []
    while True:
        print("Quyidagi ma'lumotlarni to'ldiring.")
        komp = input("Ishlab chiqaruvchi: ")
        model = input("Modeli: ")
        rang = input("Rangi: ")
        yil = int(input("Ishlab chiqarilgan yil: "))
        karobka = input("Karobkasi: ")
        narx = input("Narxi: ")
        avtolar.append(avto_info(komp, model, rang, yil, karobka,narx))
        javob = input("Davom ettiraszmi?(yes/no): ")
        if javob == 'no':
            break
    return avtolar
    
def info_print(avto_info):
    """Avtolar haqidagi malumotlar saqlangan lug'atni konsolga chiqaruvchi funksiya"""
    if avto_info['narx'] != '':
        print(f"{avto_info['rang'].title()} {avto_info['make'].upper()} {avto_info['model'].title()} "
              f"{avto_info['yil']} {avto_info['karobka'].title()} karobka. Narxi: {avto_info['narx']} $")
    else:
        print(f"{avto_info['rang'].title()} {avto_info['make'].upper()} {avto_info['model'].title()} "
              f"{avto_info['yil']} {avto_info['karobka'].title()} karobka. Narxi: Noma'lum.")

avtolar = enter_avto()
for avto in avtolar:
    info_print(avto)