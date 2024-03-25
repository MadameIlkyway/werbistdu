print()
print("----------------------")
print("Hallo.")
print("Ich bin Maike und ich stehe zwischen dir und deinem Geschenk.")
print("Ich stelle sicher, dass auch wirklich die richtige Person die notwendigen Informationen bekommt.")
print("Ich werde dir ein paar Fragen stellen, um herauszufinden, ob du berechtigt bist.")
print()

name = input("Wie heißt du? ")
true_name = ["Robert", "robert"]
foo = "foobert"
if name in true_name:
    print("Das kann ja jeder sagen.") 
    nickname = input("Wie ist dein Internet-Nickname? ")
    if nickname == "foobert" :
        print("Yay, sehr gut.")
    else: 
        print("Okay, du bist nicht der Richtige. Bye")
        quit()
elif name == foo:
    print("Sehr gut. Das erspart mir direkt die zweite Frage.")        
else:        
    print("Okay. Du bist nicht der richtige. Bye.")
    quit()
    
print()
print("Runde 1 ist geschafft.")

tier = int(input("Wie viele Haustiere hast du? "))
if tier == 2:
    print("Das war einfach." )
else: 
    print("Falsch. Bye.")
    quit()


                     