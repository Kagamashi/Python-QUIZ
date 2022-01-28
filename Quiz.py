print("Witaj w quizie o Minecrafcie!")

playing = input("Czy masz ochotę zagrać? ")

if playing != "Tak":
  quit()
  
print("Super! Zagrajmy :)")

answer = input("Na jakim poziomie można znaleźć diamenty?")
if answer == "11":
  print("Prawiłowa odpowiedź!")
