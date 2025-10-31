# Liste des espèces marines observées dans la zone Atlantique
zone_atlantique = ["morue", "homard", "maquereau", "phoque"]

# Liste des espèces marines observées dans la zone Pacifique
zone_pacifique = ["saumon", "morue", "otarie", "maquereau"]

inventaire_global = set( zone_atlantique + zone_pacifique )
liste= list(inventaire_global)

print(f"Espèces recensées : {liste}")