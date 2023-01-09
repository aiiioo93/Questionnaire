questions = ["Quel est votre prénom?", "Quel est votre âge?", "Quel est votre ville de résidence?"]
réponses = []

# Boucle qui parcourt les questions
for question in questions:
  # Affichage de la question
  print(question)
  # Enregistrement de la réponse de l'utilisateur
  réponse = input()
  réponses.append(réponse)

# Affichage des réponses
print("Voici vos réponses:")
for i, réponse in enumerate(réponses):
  print(f"Réponse à la question {i+1}: {réponse}")