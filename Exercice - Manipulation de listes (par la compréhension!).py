liste = [1, 2, 3, 4, 5]


multiple_5 = [element * 5 for element in liste]
print(multiple_5)

ajout_3 = [element + 3 for element in liste]
print(ajout_3)

carre = [element ** 2 for element in liste]
print(carre)

caractere = [str(element) for element in liste]
print(caractere)

double_pair = [element * 2 for element in liste if element % 2 == 0]
print(double_pair)

phrase_carre = [f"Le carré de { element } est { element **2 } " for element in liste]
print(phrase_carre)

filtrer_sup_a_2 = [ element * 10 for element in liste if element > 2 ]
print(filtrer_sup_a_2)

TF_sup_3= [element > 3 for element in liste ]
print(TF_sup_3)

impair = [ element if element % 2 == 0 else "impair"  for element in liste ]
print(impair)

phrase_pair_ou_impair = [ f"{element} est { "pair" if element % 2 == 0 else "impair" } " for element in liste ]
print(phrase_pair_ou_impair)