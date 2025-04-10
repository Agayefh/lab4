import random

# Siyahının uzunluğunu müəyyən edin
n = 10  # Məsələn, siyahıda 10 ədəd olsun

# [-3, 14] intervalında təsadüfi həqiqi ədədlərdən ibarət siyahı
random_list = [random.uniform(-3, 14) for _ in range(n)]

# Siyahını çıxışa ver
print(random_list)
