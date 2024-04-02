print()
print()
print()
print("Hallo.")
print("Ich bin Maike. Ich stehe zwischen dir und deinem Geschenk.")
print("Ich stelle sicher, dass auch wirklich die richtige Person die notwendigen Informationen bekommt.")
print("Ich werde dir ein paar Fragen stellen, um herauszufinden, ob du berechtigt bist.")
print()

name = input("Wie heißt du? ")
true_name = ["Robert", "robert"]
foo = ["foobert", "Foobert"]
if name in true_name:
    print()
    print("Das kann ja jeder sagen.") 
    nickname = input("Wie ist dein Internet-Nickname? ")
    if nickname in foo:
        print()
        print("Yay, sehr gut.")
    else: 
        print()
        print("Okay, du bist nicht der Richtige. Bye")
        quit()
elif name in foo:
    print()
    print("Sehr gut. Das erspart mir direkt die zweite Frage.")        
else:      
    print()  
    print("Okay. Du bist nicht der richtige. Bye.")
    quit()

print()    
print("Runde 1 ist geschafft.")
love = ["Ilke", "ilke", "Ilkyway", "Madame Ilkyway"]
freundin = input("Wie heißt die Frau, die du liebst? ")
if freundin in love:
    print()
    print("Sehr gut. <3 ")
else :
    print()
    print("WAAAASSSSS??? ")
    freundin = input("Du hast noch eine Chance, ansonsten explodiert dein System! ")
    if freundin in love:
        print()
        print("Nochmal Glück gehabt, Freundchen.")
    else: 
        print()
        print("Critical Damage in 3...2...1..." )
        print("BOOOOOMMMMMM")
        quit()    

print()
print("Eine Frage hab ich noch.")

bausteine = int(input("Wie viele Klemmbausteine besitzt du? "))
if bausteine >= 50000 :
    print()
    print("Jaaaaaa, das stiiiiimmmmmt." )
    print("Eigentlich lasse ich jede Zahl über 50.000 gelten. :D ")
    print("Hey, ich will auch meinen Spaß haben.")
else: 
    print()
    print("Falsch. Enttäuschend. Bye.")
    quit()                     

print()
print("Du bist der Richtige. Ich wusste es.")
print("Und jetzt machst du den Opa Hoppenstedt und denkst: Ich will jetzt mein Geschenk haben!!")  

hoppenstedt = input("Stimmts? ")
if hoppenstedt == "ja":
     print("Hihi. Kein Problem.") 
else: 
    print("Hmmm, okay, schade. Ich sags dir trotzdem.")     

print()
print("Gehe nun zu dem wundersamen Ort, an dem die Drahtesel pausieren.")
print("Koordinaten: N 51° 18.955 E012 22.175")
print("Kein X marktiert die Stelle. Dafür ein Stein. Nimm was zum buddeln mit.")
print("Viel Spaß, bye bye und ciao Kakao. :D ")    