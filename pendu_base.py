import random
from words import words
from hangman_visual import lives_visual_dict
import string
question = "Welcome to the hangman game. \n please, select a gamemode :\n Easy : 1\n normal: 2\n hard : 3 \n oneshot : 4\n:"

def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman(lives = 7, lives_visual = lives_visual_dict):
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual[lives])
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')

def oneshot():
    
    nombre_lettres = 2

    def devine_mot(nombre_lettres, mots):
    
    
        """Fonction pour deviner un mot en une seule tentative
        avec des indices"""
    
    
    # Choix aléatoire d'un mot dans la liste 
        word = random.choice(words)
    
    # Liste de lettres uniques dans le mot choisi 
        lettres = list(set(word))
    
    
    # Lettres à afficher pour la devinette et ajout de tirets pour les autres lettres
        indices = lettres[:nombre_lettres]
        indices.extend(['-']*(len(word)-nombre_lettres))
        indices = ' '.join(indices)
    
    # Demande d'un mot de même longueur que le mot à deviner
        mot_a_deviner = input(f"Entrez un mot de {len(word)} lettres : ")
    
    # Vérification du mot
        if len(mot_a_deviner) != len(word):
            return f"Le mot à deviner a {len(word)} lettres. Veuillez entrer un mot de même longueur."

        elif mot_a_deviner == word:
            return "Bravo ! Vous avez deviné le mot."

        else:
        # Séparation des lettres correctes et incorrectes entre le mot saisi et le mot choisi
            lettres_correctes = set(mot_a_deviner).intersection(set(word))
            lettres_incorrectes = set(mot_a_deviner).difference(set(word))
        # Affichage des résultats
            return f"Le mot choisi était {word}. Vous avez trouvé {len(lettres_correctes)} lettres correctes ({', '.join(lettres_correctes)}) et {len(lettres_incorrectes)} lettres incorrectes ({', '.join(lettres_incorrectes)})."

# Appel de la fonction pour deviner un mot
    resultat = devine_mot(nombre_lettres, words)

# Affichage du résultat
    print(resultat)


def easymode():
    return hangman(lives = 10, lives_visual = lives_visual_dict3)
    filtered_words = [word for word in words if len(word) < 5]
#faire un dessin de pendu amélioré pour un jeu à 10 vies (+3 dessins)
#trier les mots pour exclure les mots > 5 lettres


def hardmode():
    return hangman(lives = 4, lives_visual = lives_visual_dict2)
    filtered_words = [word for word in words if len(word) > 5]
#faire un dessin de pendu réduit pour un jeu à 4 vies
#trier les mots pour exclure les mots < 5 lettres

    
if __name__ == '__main__':
    while True:
        try:
            reponse = int(input(question))
        except ValueError:
            print("Please, answer the question by choosing the number associated with the gamemode")
        if reponse == 1:
            easymode()
        elif reponse == 2:
            hangman()
        elif reponse == 3:
            hardmode()
        elif reponse == 4:
            oneshot()
            break
        else:
            print("Invalid gamemode number. Please try again.")
        