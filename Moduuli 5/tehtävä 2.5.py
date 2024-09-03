# ohjelma kysyy lukuja siihen saakka, kunnes käyttäjä painaa enter
luvut = []
luku = input("anna jokin luku, painamalla enter lopetat toiminnon:")
while luku!="":
    luvut.append(int(luku))
    luku = input("anna jokin luku, painamalla enter lopetat toiminnon:")
luvut.sort(reverse=True)
print("viisi suurinta lukua olivat:")
for luku in luvut[:5]:
    print(luku)
