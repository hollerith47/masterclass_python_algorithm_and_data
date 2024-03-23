# RAPPELS PYTHON : Dictionnaire

# clef -> valeur

'''p = { "nom": "Jean", "a": 20 }

age = p.get("age")
if age:
    print("Age de la personne : " + str(age))
else:
    print("L'age n'est pas spécifié")'''

repertoire = {
    "Jean Dupont": {"age": 20, "tel": "0610191818"},
    "Marie Dupont": {"age": 30, "tel": "066565656"},
    "Herman Makiese": {"age": 26, "tel": "0899615757"},
    "Eric Dupuis": {"age": 35, "tel": "0748484848"}
}

personne_recherchee = "Herman Makiese"
infos = repertoire[personne_recherchee]
print(infos)

"""
for clef in repertoire:
    print(clef)
    print(repertoire[clef])
"""

names = ["Herman", "Makiese", "Dituasilua", "Herman", "Jean"]
nom_sans_doublons = list(set(names))
print(names)
print(nom_sans_doublons)
