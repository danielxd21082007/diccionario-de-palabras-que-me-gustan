word_dict = {"HIPOPOTOMOSTROSESQUIPEDALIOFOBIA": "es el miedo a las palabras largas", "AIBOFOBIA": "es el miedo a las palabras que se escriben igual al derecho y al revés", "CROTOLAMO": "esta"
             
                        }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ¿Qué es")

if word in word_dict.keys():
    print (word_dict [word])

else:
    print ("esa palabra no está en mis conocimientos")
