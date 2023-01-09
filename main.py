# Initialisation de la liste des questions
questions = []

# Boucle qui demande à l'utilisateur de saisir les questions
while True:
  question = input("Saisissez une question (ou tapez 'q' pour quitter): ")
  if question.lower() == 'q':
    break
  questions.append(question)

# Initialisation de la liste des réponses
réponses = {}

# Boucle qui parcourt les questions et enregistre les réponses de l'utilisateur
for question in questions:
  print(question)
  réponse = input()
  réponses[question] = réponse

# Affichage des réponses
print("Voici vos réponses:")
for question, réponse in réponses.items():
  print(f"Réponse à la question '{question}': {réponse}")
