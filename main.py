# compter les caractères


noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]

"""s = 0
for nom in noms:
    s += len(nom)


print(f"Nombre total de caractères: {s}")"""
"""s = [len(nom) for nom in noms]
print(s)
print(f"Nombre total de caractères: {sum(s)}")"""

print(len("".join(noms)))
