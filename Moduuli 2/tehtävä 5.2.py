print("Ohjelma kysyy massasi keskiaikaisten mittojen mukaan")
leiviska_str = input("leiviskat ")
naulat_str = input("naulat ")
luodit_str = input("luodit ")
leiviska = float(leiviska_str) * 20 * 32 * 13.3
naulat = float(naulat_str) * 32 * 13.3
luodit = float(luodit_str) * 13.3
print("Tämä on grammoina")
print( leiviska + naulat + luodit)
print("ja kilogrammoina")
print( (leiviska + naulat + luodit)*0.001)

