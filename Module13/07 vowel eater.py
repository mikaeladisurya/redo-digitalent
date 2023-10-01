import time

novowel_word = ""
vowel = "AIUEO"

user_word = input("Your word: ").upper()

for char in user_word:
  if char in vowel:
    print("nom...")
    time.sleep(0.5)
  else:
    novowel_word += char

print("Remaining of your word:", novowel_word)
