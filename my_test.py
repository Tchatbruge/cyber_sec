def test(mess):
    ans = ""
    for i in mess:
        if i != " " :
            ans += i 
    return ans.lower()

mes = "abCDefgh"
print(test(mes))

liste = [(ord(char) + 2) for char in mes ]
listes = ''.join([(chr(char)) for char in liste ])
print(listes)