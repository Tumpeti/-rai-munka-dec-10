"""Adott az ABC: AÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVWXYZ  Kérj be a felhasználótól egy szöveget, majd írd ki a szöveget titkosítva oly módon,
hogy az erdeti ABC betűje helyett a 3-mal eltolt ABC-t használod helyette. XYZAÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVW

A rendelkezésre álló idő 20 perc.

A kódról és a program futásáról is képernyőképet kérek feltölteni.

1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25	26	27	28	29	30	31	32	33	34	35
A	Á	B	C	D	E	É	F	G	H	I	Í	J	K	L	M	N	O	Ó	Ö	Ő	P	Q	R	S	T	U	Ú	Ü	Ű	V	W	X	Y	Z
EREDETI	A	Á	B	C	D	E	É	F	G	H	I	Í	J	K	L	M	N	O	Ó	Ö	Ő	P	Q	R	S	T	U	Ú	Ü	Ű	V	W	X	Y	Z
ELTOLT	X	Y	Z	A	Á	B	C	D	E	É	F	G	H	I	Í	J	K	L	M	N	O	Ó	Ö	Ő	P	Q	R	S	T	U	Ú	Ü	Ű	V	W
K	U	T	Y	A
Titkosított szöveg: 	I	R	Q	V	X

2 lista																											"""

# abc = ['A', 'Á', 'B', 'C', 'D', 'E', 'É', 'F', 'G', 'H', 'I', 'Í', 'J', 'K', 'L', 'M', 'N', 'O', 'Ó', 'Ö', 'Ő', 'P', 'Q', 'R', 'S', 'T', 'U', 'Ú', 'Ü', 'Ű', 'V', 'W', 'X', 'Y', 'Z']
#
# uzenet = input("Kérem a kódolandó szöveget! ").upper()
# uzenet_nagy = [*uzenet]
# print(f"Üzenet: {uzenet_nagy}")
# print(f"ABC:{abc}")
#
# def beolvaso():
#     i = 0
#     l = 0
#     kodolt_uzenet = []
#     while i < len(uzenet_nagy):
#         while l < len(abc):
#             if abc[l] == uzenet_nagy[i]:
#                 titkositott_betu = abc[l-3]
#                 kodolt_uzenet.append(titkositott_betu)
#             l += 1
#         l = 0
#         i += 1
#     print(kodolt_uzenet)
#
#
# beolvaso()

# abc = "AÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVWXYZ "
# titkos = "XYZAÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVW "
# #
# def betukeres(betu):
#      i = 0
#      while i < len(abc) and abc[i] != betu:
#          i += 1
#      if i < len(abc):
#          return i
#      else:
#          return -1
#
# # keresendo_betu = input("Kérek egy betűt").upper()
# # print(betukeres(keresendo_betu))
#
# def titkosit():
#     szoveg = input("Adj meg egy szöveget! ").upper()
#     i = 0
#     titkos_szoveg = ""
#     while i < len(szoveg):
#         betu_hely = betukeres(szoveg[i])
#         titkos_szoveg += titkos[betu_hely]
#         i += 1
#
#     print(titkos_szoveg)

# titkosit()