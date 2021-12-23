sort = str.lower(input("Введіть речення: "))
print("Виберіть дію: \n 1:сортувати речення \n 2:показати кількість букв")
choose = str(input("   "))
sortlist = sort.split()
setl = set(sortlist)
a = ""
b = {}
for i in sorted(setl):
    if len(i) > 3:
      a += "" + i
    else:
        continue
if choose == "1":
    print(a)
elif choose == "2":
    for f in set(a):
        if f != " ":
            b[f] = a.count(f)
        else:
            continue
    print(b)
else:
    print('Некоректне значення')