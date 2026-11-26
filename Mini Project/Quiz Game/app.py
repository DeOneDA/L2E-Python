import tkinter as tk
import random as rand

root = tk.Tk()
root.geometry("500x400")
root.title("Quiz Game")

bank = {
    "Which leafy vegetable is the main ingredient used to make Yoruba Efo Riro?": {
        "choices": [
            ("A", "Bitter leaf"),
            ("B", "African spinach"),
            ("C", "Waterleaf"),
            ("D", "Scent leaf")
        ],
        "correct": ("B", "African spinach")
    },
    "Which of these soups is traditionally made from roasted or boiled and pounded palm fruits?": {
        "choices": [
            ("A", "Banga soup"),
            ("B", "Ogbono soup"),
            ("C", "Edikang Ikong"),
            ("D", "Ewedu soup")
        ],
        "correct": ("A", "Banga soup")
    },
    "What is Kilishi primarily made from?": {
        "choices": [
            ("A", "Fried plantain strips"),
            ("B", "Spiced, sun-dried beef"),
            ("C", "Fermented cassava flakes"),
            ("D", "Ground tiger nuts")
        ],
        "correct": ("B", "Spiced, sun-dried beef")
    },
    "Which classic Nigerian street food is a steamed pudding made from blended peeled beans, peppers, and onions?": {
        "choices": [
            ("A", "Akara"),
            ("B", "Masa"),
            ("C", "Moi Moi"),
            ("D", "Puff-Puff")
        ],
        "correct": ("C", "Moi Moi")
    },
    "Which Nigerian soup gets its signature slippery, draw texture from ground wild mango seeds?": {
        "choices": [
            ("A", "Egusi soup"),
            ("B", "Afang soup"),
            ("C", "Miyan Kuka"),
            ("D", "Ogbono soup")
        ],
        "correct": ("D", "Ogbono soup")
    },
    "In Abula, which combination pairs directly with Amala to give the dish its signature texture and flavor?": {
        "choices": [
            ("A", "Ewedu (jute leaf soup) and Ogbono soup"),
            ("B", "Ewedu (jute leaf soup) and Gbegiri (bean soup)"),
            ("C", "Gbegiri (bean soup) and Efo Riro"),
            ("D", "Efo Riro and Ewedu (jute leaf soup)")
        ],
        "correct": ("B", "Ewedu (jute leaf soup) and Gbegiri (bean soup)")
    },
    "Both Moi Moi and Akara start from a similar blended bean base, so what actually separates them in preparation?": {
        "choices": [
            ("A", "Moi Moi uses fermented bean paste while Akara uses freshly peeled whole beans"),
            ("B", "Moi Moi is steamed in leaves, foil, or containers while Akara is deep-fried in oil"),
            ("C", "Moi Moi always includes palm oil in the batter while Akara is fried without oil"),
            ("D", "Moi Moi is made from black-eyed peas while Akara is made from honey beans")
        ],
        "correct": ("B", "Moi Moi is steamed in leaves, foil, or containers while Akara is deep-fried in oil")
    },
    "If someone orders Eba vs. Garri at a Nigerian eatery, what distinction are they making?": {
        "choices": [
            ("A", "Garri is dried cassava flakes, while Eba is the dough made by stirring garri into hot water"),
            ("B", "Eba is made from white garri, while Garri itself always refers to yellow palm-oil garri"),
            ("C", "Garri is fermented cassava paste, while Eba is roasted cassava granules"),
            ("D", "Eba is pounded from boiled cassava, while Garri is grated and sun-dried without fermentation")
        ],
        "correct": ("A", "Garri is dried cassava flakes, while Eba is the dough made by stirring garri into hot water")
    },
    "Which detail best distinguishes traditional Suya from Kilishi?": {
        "choices": [
            ("A", "Suya uses beef while Kilishi is only made with goat or ram meat"),
            ("B", "Suya is grilled fresh over open flame with peanut spice, while Kilishi is thinly sliced, sun-dried, coated in spiced groundnut paste, and finished by roasting/drying"),
            ("C", "Kilishi is boiled in broth before spicing, while Suya is marinated in vinegar and fried"),
            ("D", "Suya has no groundnut spice, while Kilishi is coated only in chili and ginger")
        ],
        "correct": ("B", "Suya is grilled fresh over open flame with peanut spice, while Kilishi is thinly sliced, sun-dried, coated in spiced groundnut paste, and finished by roasting/drying")
    },
    "Between Edikang Ikong and Afang soup, which pairing of key ingredients is most accurate?": {
        "choices": [
            ("A", "Edikang Ikong relies heavily on ugu (pumpkin leaves) and waterleaf, while Afang pairs shredded afang (okazi) leaves with waterleaf"),
            ("B", "Edikang Ikong pairs afang (okazi) leaves with bitter leaf, while Afang soup uses ugu and scent leaf"),
            ("C", "Edikang Ikong is thickened with melon seeds, while Afang soup is thickened with ground baobab leaf"),
            ("D", "Edikang Ikong contains no palm oil, while Afang soup is cooked strictly with groundnut oil")
        ],
        "correct": ("A", "Edikang Ikong relies heavily on ugu (pumpkin leaves) and waterleaf, while Afang pairs shredded afang (okazi) leaves with waterleaf")
    },
}

total = 0
user= 0

def check_answer(question, choice):
    return True if choice == bank[question]["correct"][0] else False

def get_feedback(score, total):
    middle = total // 2
    return f"Wow, you got {score}/{total}. Impressive!" if score == total else f"Nice, you got {score}/{total}. You did very well." if score >= middle else f"So you got {score}/{total}, so sad."

def operator():
   global total, user, question, radiobuttons
   if question not in used_questions: used_questions.append(question)
   user_choice = option.get()
   if not user_choice: return
   total += 1
   if check_answer(question, user_choice): user += 1
   if total == 5:
      question_label.config(text=get_feedback(user, total))
      for radiobutton in radiobuttons: radiobutton.pack_forget()
      submit_button.config(state="disabled")
      return
   question = rand.choice(list(text for text in bank.keys() if text not in used_questions))
   question_label.config(text=question)
   option.set("")
   for radiobutton, new_option in zip(radiobuttons, bank[question]["choices"]):
       radiobutton.config(text=f"{new_option[0]}. {new_option[1]}", value=new_option[0])
       
      
title_label = tk.Label(root, text="Nigerian Food Trivia.", font=("Arial", 15))
title_label.pack(pady=5)

question = rand.choice(list(bank.keys()))
question_label = tk.Label(root, text=question, font=("Arial", 10), wraplength=440)
question_label.pack(pady=5)

used_questions = [question]
option = tk.StringVar()

radiobuttons = [tk.Radiobutton(root, text=f"{options[0]}. {options[1]}", variable=option, value=options[0], wraplength=440) for options in bank[question]["choices"]]
for radiobutton in radiobuttons: radiobutton.pack(anchor="center", padx=20)

submit_button = tk.Button(root, text="Submit", command=operator)
submit_button.pack()

tk.Label(root, text="Built by ~De One~", font =("Arial", 14)).pack(pady = 20)

root.mainloop()