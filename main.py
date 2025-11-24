import random
#1-misol
print("21. 6 xonali tasodifiy parol (faqat raqam):")
parol = random.randint(100000, 999999)
print(parol)
print("-" * 40)

#2-misol
print("22. 1-10 oralig'ida son va uning faktoriyali:")
son = random.randint(1, 10)
fakt = 1
for i in range(1, son + 1):
    fakt *= i
print(f"Son: {son} → Faktoriyal: {fakt}")
print("-" * 40)

#3-misol
print("23. Satrdan tasodifiy harf tanlash:")
satr = input("Istalgan satr kiriting: ")
if satr:  # bo'sh emasligini tekshirish
    tasodifiy_harf = random.choice(satr)
    print(f"Tasodifiy tanlangan harf: {tasodifiy_harf}")
else:
    print("Satr bo'sh!")
print("-" * 40)

#4-misol
print("24. 0-50 oralig'ida son → 7 ga bo'linishini tekshirish:")
son = random.randint(0, 50)
print(f"Tasodifiy son: {son}")
if son % 7 == 0:
    print("7 ga bo'linadi!")
else:
    print("7 ga bo'linmaydi.")
print("-" * 40)

#5-misol
print("25. 1-4 oralig'ida son → turli xabarlar:")
son = random.randint(1, 4)
if son == 1:
    print("Birinchi variant tanlandi – Salom dunyo!")
elif son == 2:
    print("Ikkinchi variant – Bugun ajoyib kun!")
elif son == 3:
    print("Uchinchi variant – Dasturlash – bu san'at!")
else:  # son == 4
    print("To'rtinchi variant – Muvaffaqiyat sizniki!")
