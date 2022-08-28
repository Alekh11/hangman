word_list=["Panda","baboon","camel","cat","monkey","bear","octopus","fish","Racoon","panther","chimpanzee","lion","cow","tiger","dinosaur","vulture","zebra"]
import random
logo = '''
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/                       
'''
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

win= '''   _   _   _     _   _   _  
  / \ / \ / \   / \ / \ / \ 
 ( Y | o | u ) ( w | i | n )
  \_/ \_/ \_/   \_/ \_/ \_/ 
  '''
lose = '''
   _   _   _     _   _   _   _  
  / \ / \ / \   / \ / \ / \ / \ 
 ( Y | o | u ) ( l | o | s | e )
  \_/ \_/ \_/   \_/ \_/ \_/ \_/ '''
  
print (logo)

print("Your topic is animals.")

chosen_word = random.choice(word_list)

word_length=len(chosen_word)

livesgone=0


display = []
for _ in range(word_length):
    display+= "_"
print(display)

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter =chosen_word[position]
        if letter==guess:
            display[position]=letter
            
    if guess not in chosen_word:
        print(f"You guessed {guess} which isnt in the word. HAHA you lose a life!")
       
        livesgone += 1
        if livesgone == 6:
            end_of_game= True
            print (lose)
            print(f"The word was {chosen_word}")
        
    print(display)

    if "_" not in display:
        end_of_game = True
        print (win)
        
    print(stages[livesgone])