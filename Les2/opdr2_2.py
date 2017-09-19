cijferICOR = 7
cijferPROG = 9
cijferCSN = 8

totaal = (cijferICOR + cijferPROG + cijferCSN)

gemiddelde = totaal / 3
beloning = totaal * 30
overzicht = "Mijn cijfers (gemiddeld een {0}) leveren een beloning op van €{1} op!".format(gemiddelde, beloning)

print(overzicht)