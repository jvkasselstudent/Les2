age = input("Geef je leeftijd: ")
passport = input("Nederlands paspoort: ")
if int(age) >= 18 and passport.lower() == "ja":
    print("Gefeliciteerd, je mag stemmen!")