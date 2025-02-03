def test(mess):
    ans = ""
    for i in mess:
        if i != " " :
            ans += i 
    return ans.lower()

def count_occurence(text):
    liste = {}
    for i in text: 

        liste[i] = text.count(i)
    return liste

def replace(text):
    liste = ""
    for i in text: 
        if i == "Q" :
            liste += "T" 
        else :
            liste += i

    return liste

mes = "CRYPTOGRAPHICSYSTEMSAREEXTREMELYDIFFICULTTOBUILDNEVERTHELESSFORSOMEREASONMANYNONEXPERTSINSISTONDESIGNINGNEWENCRYPTIONSCHEMESTHATSEEMTOTHEMTOBEMORESECURETHANANYOTHERSCHEMEONEARTHTHEUNFORTUNATETRUTHHOWEVERISTHATSUCHSCHEMESAREUSUALLYTRIVIALTOBREAK"
print(count_occurence(mes))

# liste = [(ord(char) + 2) for char in mes ]
# listes = ''.join([(chr(char)) for char in liste ])
# print(listes)