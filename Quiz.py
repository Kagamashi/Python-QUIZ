print("Witaj w quizie o Minecrafcie!")

playing = input("Czy masz ochotę zagrać? ")

if playing != "Tak":
  quit()
  
print("Super! Zagrajmy :)")

answer = input("Na jakim poziomie można znaleźć diamenty?")
if answer == "11":
  print("Prawiłowa odpowiedź!")

answer = input("Ile najwięcej szmaragdów można spotkać obok siebie?")
if answer == "2":
  print("Prawidłowa odpowiedź!")
