# Programme qui compte le nombre de mots dans un texte.
# Rédigé par Jia Lin Wan gr. 403


def word_count():
    num_words = len(text.split())
    print(num_words)


while True:
    text = input("Insérer le texte ici : \n")
    word_count()
