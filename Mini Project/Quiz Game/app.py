import tkinter as tk
import random as rand

root = tk.Tk()
root.geometry("720x400")
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
    "Which northern Nigerian soup relies on ground baobab leaf for its distinct texture?": {
        "choices": [
            ("A", "Miyan Kuka"),
            ("B", "Miyan Taushe"),
            ("C", "Ofe Nsala"),
            ("D", "Efo Elegusi")
        ],
        "correct": ("A", "Miyan Kuka")
    },
    "In northern Nigeria, what is Fura da Nono made from?": {
        "choices": [
            ("A", "Roasted corn dough mixed with palm nut cream"),
            ("B", "Spiced millet dough balls crumbled into fermented cow milk"),
            ("C", "Steamed bean pudding served with groundnut oil"),
            ("D", "Mashed sorghum swallow paired with dried okra soup")
        ],
        "correct": ("B", "Spiced millet dough balls crumbled into fermented cow milk")
    },
    "Which traditional Igbo dish consists of shredded dried cassava tossed with palm oil, ugba (fermented oil bean), and local seasonings?": {
        "choices": [
            ("A", "Tuwon Masara"),
            ("B", "Abacha"),
            ("C", "Kunun Zaki"),
            ("D", "Oha Soup")
        ],
        "correct": ("B", "Abacha")
    },
    "What separates Tuwon Masara from Tuwon Dawa in northern Nigerian cooking?": {
        "choices": [
            ("A", "Tuwon Masara is made from maize while Tuwon Dawa is made from sorghum"),
            ("B", "Tuwon Masara is deep-fried while Tuwon Dawa is steamed in leaves"),
            ("C", "Tuwon Masara is a cold beverage while Tuwon Dawa is a thick soup"),
            ("D", "Tuwon Masara uses yam flour while Tuwon Dawa uses cassava flakes")
        ],
        "correct": ("A", "Tuwon Masara is made from maize while Tuwon Dawa is made from sorghum")
    },
    "Which fermented condiment is traditionally wrapped in leaves and used to add deep savory flavor to soups like Ofe Onugbu, Ofe Oha, and Egusi?": {
        "choices": [
            ("A", "Yaji"),
            ("B", "Ogiri"),
            ("C", "Garri"),
            ("D", "Kuli-Kuli")
        ],
        "correct": ("B", "Ogiri")
    },
    "In eastern Nigerian delicacies, which dish features spicy palm-oil-dressed cow foot garnished with utazi leaves?": {
        "choices": [
            ("A", "Nkwobi"),
            ("B", "Isi Ewu"),
            ("C", "Dan Wake"),
            ("D", "Ofada Stew")
        ],
        "correct": ("A", "Nkwobi")
    },
    "Which eastern Nigerian delicacy is prepared using a seasoned goat head in a rich palm oil sauce?": {
        "choices": [
            ("A", "Isi Ewu"),
            ("B", "Pepper Soup"),
            ("C", "Miyan Kuka"),
            ("D", "Gbegiri")
        ],
        "correct": ("A", "Isi Ewu")
    },
    "What is the traditional base ingredient of Gbegiri soup in Yoruba cuisine?": {
        "choices": [
            ("A", "Peeled, boiled, and mashed/blended beans"),
            ("B", "Grated cocoyam paste"),
            ("C", "Crushed melon seeds"),
            ("D", "Chopped jute leaves")
        ],
        "correct": ("A", "Peeled, boiled, and mashed/blended beans")
    },
    "Which northern Nigerian street or household meal consists of firm bean flour dumplings served with oil, yaji, onions, and boiled eggs?": {
        "choices": [
            ("A", "Dan Wake"),
            ("B", "Ewa Agoyin"),
            ("C", "Asaro"),
            ("D", "Bole")
        ],
        "correct": ("A", "Dan Wake")
    },
    "Which Yoruba staple swallow is made from dried, peeled yam pieces milled into flour and stirred into boiling water?": {
        "choices": [
            ("A", "Amala"),
            ("B", "Fufu"),
            ("C", "Tuwo Shinkafa"),
            ("D", "Eba")
        ],
        "correct": ("A", "Amala")
    },
    "Which northern Nigerian drink is commonly made from fermented grain paste with warming spices like ginger and cloves?": {
        "choices": [
            ("A", "Kunun Zaki"),
            ("B", "Agbo"),
            ("C", "Palm Wine"),
            ("D", "Zobo")
        ],
        "correct": ("A", "Kunun Zaki")
    },
    "How is Tuwo Shinkafa prepared so it can be eaten as a swallow with soups?": {
        "choices": [
            ("A", "Soft rice is cooked until very tender and mashed into a smooth dough"),
            ("B", "Parboiled rice is sun-dried and pounded into dry flour"),
            ("C", "Raw rice is soaked and fried into crispy cakes"),
            ("D", "Rice grains are fermented in water for three days and baked")
        ],
        "correct": ("A", "Soft rice is cooked until very tender and mashed into a smooth dough")
    },
    "Which spice blend is famously rubbed onto skewered meat before roasting for Suya and Balangu?": {
        "choices": [
            ("A", "Yaji"),
            ("B", "Iru"),
            ("C", "Ugu"),
            ("D", "Efo")
        ],
        "correct": ("A", "Yaji")
    },
    "In which pairing is an aromatic leaf matched with a soup it is widely associated with in Nigerian cooking?": {
        "choices": [
            ("A", "Utazi with Nkwobi"),
            ("B", "Ewedu leaves with Banga soup"),
            ("C", "Moringa leaves with Gbegiri"),
            ("D", "Scent leaf with Tuwon Masara")
        ],
        "correct": ("A", "Utazi with Nkwobi")
    },
    "What is Ogi (also called Pap) traditionally made from in Nigerian kitchens?": {
        "choices": [
            ("A", "Fermented cereal porridge from maize, sorghum, or millet"),
            ("B", "Roasted yam slices simmered in palm oil"),
            ("C", "Steamed groundnut paste wrapped in banana leaves"),
            ("D", "Fried plantain cubes tossed with pepper sauce")
        ],
        "correct": ("A", "Fermented cereal porridge from maize, sorghum, or millet")
    },
    "Which northern Nigerian meat preparation involves roasting meat on sticks beside an open fire and seasoning with yaji?": {
        "choices": [
            ("A", "Balangu"),
            ("B", "Moi Moi"),
            ("C", "Efo Riro"),
            ("D", "Abacha")
        ],
        "correct": ("A", "Balangu")
    },
    "Which Nigerian dish is made by cooking yam chunks in a savory pepper-and-tomato palm oil sauce until soft and partly mashed?": {
        "choices": [
            ("A", "Asaro (yam pottage)"),
            ("B", "Kilishi"),
            ("C", "Fura da Nono"),
            ("D", "Ofe Nsala")
        ],
        "correct": ("A", "Asaro (yam pottage)")
    },
    "Which leafy green is paired with moringa-based cooking in northern Nigeria, known locally as zogale?": {
        "choices": [
            ("A", "Moringa leaves (zogale)"),
            ("B", "Jute leaves (ewedu)"),
            ("C", "Waterleaf"),
            ("D", "Bitter leaf")
        ],
        "correct": ("A", "Moringa leaves (zogale)")
    },
    "In southwestern Nigeria, what is Bole traditionally made from?": {
        "choices": [
            ("A", "Roasted plantains, often served with groundnuts or pepper sauce"),
            ("B", "Fermented cassava dough wrapped in leaves"),
            ("C", "Steamed cocoyam leaves with palm oil"),
            ("D", "Boiled beans mashed with palm oil")
        ],
        "correct": ("A", "Roasted plantains, often served with groundnuts or pepper sauce")
    },
    "Which fermented locust bean condiment is closely tied to Yoruba cooking and sauces such as Ofada stew?": {
        "choices": [
            ("A", "Iru"),
            ("B", "Nono"),
            ("C", "Fura"),
            ("D", "Masa")
        ],
        "correct": ("A", "Iru")
    },
    "Which traditional Igbo soup is thickened with grated cocoyam and pairs bitter leaf (onugbu) with palm oil and meat or fish?": {
        "choices": [
            ("A", "Ofe Onugbu"),
            ("B", "Miyan Kuka"),
            ("C", "Ewedu soup"),
            ("D", "Gbegiri")
        ],
        "correct": ("A", "Ofe Onugbu")
    },
    "Which northern Nigerian soup features pumpkin (squash) cooked down with tomatoes, spices, and palm oil or groundnut oil?": {
        "choices": [
            ("A", "Miyan Taushe"),
            ("B", "Ofe Nsala"),
            ("C", "Efo Riro"),
            ("D", "Afang soup")
        ],
        "correct": ("A", "Miyan Taushe")
    },
    "What makes Ofada rice and Ofada stew distinct from standard white rice and everyday tomato stew in southwestern Nigeria?": {
        "choices": [
            ("A", "Ofada rice is unpolished indigenous rice, and Ofada stew traditionally uses locust beans (iru), unbleached palm oil, and fiery green or red peppers"),
            ("B", "Ofada rice is made from millet flour, and Ofada stew is a sweet coconut milk sauce"),
            ("C", "Ofada rice is steamed inside banana leaves with beans, and Ofada stew has no peppers"),
            ("D", "Ofada rice is dried cassava flakes, and Ofada stew is thickened with baobab leaf")
        ],
        "correct": ("A", "Ofada rice is unpolished indigenous rice, and Ofada stew traditionally uses locust beans (iru), unbleached palm oil, and fiery green or red peppers")
    },
    "Which crisp northern Nigerian snack is made by pressing spiced groundnut paste cake after extracting oil and frying it?": {
        "choices": [
            ("A", "Kuli-Kuli"),
            ("B", "Puff-Puff"),
            ("C", "Akara"),
            ("D", "Chin Chin")
        ],
        "correct": ("A", "Kuli-Kuli")
    },
    "Which traditional Igbo soup is made with tender young oha leaves added right at the end with cocoyam thickener and palm oil?": {
        "choices": [
            ("A", "Oha Soup"),
            ("B", "Banga soup"),
            ("C", "Miyan Kuka"),
            ("D", "Ewedu soup")
        ],
        "correct": ("A", "Oha Soup")
    },
    "Which spicy, savory Nigerian bean dish is slow-cooked with palm oil and a rich pepper-and-onion sauce and commonly eaten with bread or garri?": {
        "choices": [
            ("A", "Ewa Agoyin"),
            ("B", "Fura da Nono"),
            ("C", "Ogi"),
            ("D", "Tuwo Shinkafa")
        ],
        "correct": ("A", "Ewa Agoyin")
    },
    "In Delta and Edo cooking, which spice is famously included in Banga soup to give it its distinct aromatic profile?": {
        "choices": [
            ("A", "Oburunbube (banga spice)"),
            ("B", "Kuka"),
            ("C", "Zobo petals"),
            ("D", "Nono")
        ],
        "correct": ("A", "Oburunbube (banga spice)")
    },
    "Which northern Nigerian pancake-like snack or breakfast food is made from fermented rice or millet batter cooked in a special pan with depressions?": {
        "choices": [
            ("A", "Masa"),
            ("B", "Nkwobi"),
            ("C", "Asaro"),
            ("D", "Abacha")
        ],
        "correct": ("A", "Masa")
    },
    "What is Ofe Nsala (White Soup) in Igbo cuisine known for?": {
        "choices": [
            ("A", "A light, peppery broth—often with catfish or chicken and yam as thickener—made without palm oil"),
            ("B", "A heavy palm-oil stew made with roasted groundnuts and dried fish"),
            ("C", "A cold fermented milk drink sweetened with dates"),
            ("D", "A dish of shredded cassava mixed with melon seeds")
        ],
        "correct": ("A", "A light, peppery broth—often with catfish or chicken and yam as thickener—made without palm oil")
    },
    "Which sweet Yoruba yam dish is made by pounding boiled yam until smooth and glossy—traditionally without cassava or flour?": {
        "choices": [
            ("A", "Iyan (Pounded Yam)"),
            ("B", "Eba"),
            ("C", "Amala"),
            ("D", "Tuwon Masara")
        ],
        "correct": ("A", "Iyan (Pounded Yam)")
    },
    "Which Nigerian beverage is brewed from dried hibiscus petals and often flavored with ginger, cloves, or pineapple?": {
        "choices": [
            ("A", "Zobo"),
            ("B", "Fura"),
            ("C", "Ogi"),
            ("D", "Iru")
        ],
        "correct": ("A", "Zobo")
    },
    "Which southern Nigerian soup is made with periwinkles, palm oil, and leafy greens such as fluted pumpkin leaves or bitter leaf?": {
        "choices": [
            ("A", "Editan soup"),
            ("B", "Miyan Kuka"),
            ("C", "Tuwon Dawa"),
            ("D", "Fura da Nono")
        ],
        "correct": ("A", "Editan soup")
    },
    "What is Ukwa in southeastern Nigerian cuisine?": {
        "choices": [
            ("A", "African breadfruit seeds cooked savory in palm oil or porridge"),
            ("B", "Fermented sorghum gruel served hot at breakfast"),
            ("C", "Sun-dried goat meat coated in groundnut paste"),
            ("D", "Steamed plantain pudding wrapped in foil")
        ],
        "correct": ("A", "African breadfruit seeds cooked savory in palm oil or porridge")
    },
    "Which aromatic herb—known as efirin in Yoruba and nchuanwu in Igbo—is prized in soups and pepper sauces for its strong herbal aroma?": {
        "choices": [
            ("A", "Scent leaf"),
            ("B", "Jute leaf"),
            ("C", "Baobab leaf"),
            ("D", "Pumpkin leaf")
        ],
        "correct": ("A", "Scent leaf")
    },
    "How is traditional Nigerian fufu (cassava fufu) prepared before serving with soup?": {
        "choices": [
            ("A", "Fermented cassava is soaked, mashed or sieved, cooked in water until firm, and pounded or stirred smooth"),
            ("B", "Fresh cassava is sliced thin and deep-fried like potato chips"),
            ("C", "Cassava flour is mixed with cold milk and baked into bread"),
            ("D", "Whole cassava tubers are roasted in ash and eaten with honey")
        ],
        "correct": ("A", "Fermented cassava is soaked, mashed or sieved, cooked in water until firm, and pounded or stirred smooth")
    },
}

total = 0
user= 0
wrong_choices = {}

def check_answer(question, choice):
    return True if choice == bank[question]["correct"][0] else False

def get_feedback(score, total):
    middle = total // 2
    return f"Wow, you got {score}/{total}. Impressive!" if score == total else f"Nice, you got {score}/{total}. You did very well." if score >= middle else f"So you got {score}/{total}, so sad."

def operator():
   global total, user, question, radiobuttons, banks
   if question not in used_questions: used_questions.append(question)
   user_choice = option.get()
   if not user_choice: return
   total += 1
   if check_answer(question, user_choice): user += 1
   else:
      for letter, text in bank[question]["choices"]:
        if letter == user_choice:
           wrong_choices[question] = ((letter,text), bank[question]["correct"])
   if total == 10:
    if wrong_choices:
        root.geometry("720x650")
        question_label.config(text=f"{get_feedback(user, total)}")
        counter = 1
        tk.Label(root, text="Here are the questions you missed:").pack(pady=10)
        for q, (u, c) in wrong_choices.items():
           wrong_question = tk.Label(root, text=f"{counter}. {q}", wraplength=440)
           invalid = tk.Label(root, text=f"Your Choice was: {u}", fg="red", wraplength=440)
           valid = tk.Label(root, text=f"The Answer: {c}\n", fg="green", wraplength=440)
           wrong_question.pack()
           invalid.pack()
           valid.pack()
           counter += 1
        tk.Label(root, text="Built by ~De One~", font =("Arial", 14)).pack(pady = 20)
    else:
        question_label.config(text={get_feedback(user, total)})
        tk.Label(root, text="Built by ~De One~", font =("Arial", 14)).pack(pady = 20)
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

root.mainloop()