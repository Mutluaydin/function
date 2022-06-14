# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.
def yazdir(kelime , sayi):
    print(kelime * sayi)
yazdir("Hallo\n" , 5)

# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazınız.
def listeCevir(*params):
    liste = []

    for i in params:
        liste.append(i)
    return liste

result = listeCevir("hallo" , 15, "Ali", 25)
print(result)


# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.
def asalSayi(num1, num2):
    for i in range(num1, num2+1):
        if i > 1:
            for j in range(2, i):
                if (i % j == 0):
                    break
            else:
                print(i)

num1 = int(input("Ilk sayiyi gir: "))
num2 = int(input("Son sayiyi gir: "))

asalSayi(num1, num2)

# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürünüz.
def tamBolenleriBul(say):
    tamBolenler = []

    for i in range(2, say):
        if (say % i == 0):
            tamBolenler.append(i)

    return tamBolenler

say = int(input("Sayiyi gir: "))
print(tamBolenleriBul(say))