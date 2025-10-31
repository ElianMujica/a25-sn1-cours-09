virus_et_autres_info = [
    ["Virus-T", 0.9 ,"Transforme les humains en zombies et armes biologiques"],
    ["Virus-C", 0.0001 ,"Provoque des mutations extrêmes et régénère les tissus"],
    ["Virus-G", 0.85, "Cause des mutations incontrôlables avec régénération cellulaire rapide"],
    ["Uroboros", 0.005, "Consomme les organismes incompatibles et renforce les hôtes compatibles"]
]
virus=[]
taux_de_succes=[]
caracteristiques=[]
if len(virus_et_autres_info) == 0:

    print("Désolé aucun produit pharmaceutique mortel disponible")

else:
    print(f"Liste des {len(virus_et_autres_info)} virus ")

    for i in range(len(virus_et_autres_info)):
        virus.append (virus_et_autres_info[i][0])
        taux_de_succes.append ((virus_et_autres_info[i][1]*100) )
        caracteristiques.append (virus_et_autres_info[i][2])

    for j in range (len(virus)):
        print(f"{virus[j]} - {caracteristiques[j]} - (taux de mutation estimé : {taux_de_succes[j]}%)")







