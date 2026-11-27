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
    "In Edo and Delta cooking, what is Owo soup traditionally made with?": {
        "choices": [
            ("A", "A rich palm-oil and spiced stock with traditional aromatics like banga spice and negro pepper, often with meat or fish"),
            ("B", "Roasted cornmeal stirred into cold coconut water"),
            ("C", "Sun-dried goat meat tossed in groundnut flour and honey"),
            ("D", "Steamed millet balls served in sweet milk")
        ],
        "correct": ("A", "A rich palm-oil and spiced stock with traditional aromatics like banga spice and negro pepper, often with meat or fish")
    },
    "Which northern Nigerian dish consists of steamed or boiled cowpea/bean flour cakes or dumplings eaten with spiced groundnut oil or stew?": {
        "choices": [
            ("A", "Dan Wake"),
            ("B", "Efo Elegusi"),
            ("C", "Bole"),
            ("D", "Gbegiri")
        ],
        "correct": ("A", "Dan Wake")
    },
    "What distinguishes Efo Elegusi from plain Efo Riro in Yoruba cuisine?": {
        "choices": [
            ("A", "Efo Elegusi incorporates ground melon seeds (egusi) into the leafy vegetable and pepper stew"),
            ("B", "Efo Elegusi is made with fermented locust beans only and contains no leafy greens"),
            ("C", "Efo Elegusi is a sweet dessert made from ripe plantains and coconut"),
            ("D", "Efo Elegusi is a clear broth thickened with yam flour")
        ],
        "correct": ("A", "Efo Elegusi incorporates ground melon seeds (egusi) into the leafy vegetable and pepper stew")
    },
    "Which northern Nigerian street food is made from fermented cassava or sorghum/millet gruel sweetened with sugar or milk and often topped with groundnuts?": {
        "choices": [
            ("A", "Kunu Gyada"),
            ("B", "Nkwobi"),
            ("C", "Ofe Owerri"),
            ("D", "Isi Ewu")
        ],
        "correct": ("A", "Kunu Gyada")
    },
    "What is Kunu Gyada in northern Nigerian cooking?": {
        "choices": [
            ("A", "A thick rice or cereal gruel/pap enriched with groundnut paste and served warm"),
            ("B", "Spiced dried beef strips fried in groundnut oil"),
            ("C", "Fermented palm sap tapped from raffia trees"),
            ("D", "Steamed bean pudding cooked in banana leaves")
        ],
        "correct": ("A", "A thick rice or cereal gruel/pap enriched with groundnut paste and served warm")
    },
    "Which traditional Igbo festival and everyday soup is celebrated for its generous mix of leafy greens, cocoyam paste, palm oil, and multiple meats or fish?": {
        "choices": [
            ("A", "Ofe Owerri"),
            ("B", "Miyan Kuka"),
            ("C", "Tuwon Masara"),
            ("D", "Kunun Zaki")
        ],
        "correct": ("A", "Ofe Owerri")
    },
    "Which Yoruba dish pairs roasted or boiled unripe or ripe plantains with palm-oil bean stew or fried fish and pepper sauce?": {
        "choices": [
            ("A", "Bole"),
            ("B", "Dan Wake"),
            ("C", "Miyan Taushe"),
            ("D", "Tuwo Shinkafa")
        ],
        "correct": ("A", "Bole")
    },
    "Which northern Nigerian snack or side is made from pounded or ground roasted groundnuts shaped into sticks or balls?": {
        "choices": [
            ("A", "Kuli-Kuli"),
            ("B", "Moi Moi"),
            ("C", "Akara"),
            ("D", "Asaro")
        ],
        "correct": ("A", "Kuli-Kuli")
    },
    "In Nigerian cooking, what is Ugba (also called Ukpaka) derived from?": {
        "choices": [
            ("A", "Fermented African oil bean seeds"),
            ("B", "Dried hibiscus flower calyces"),
            ("C", "Roasted tiger nut tubers"),
            ("D", "Pounded white yam flour")
        ],
        "correct": ("A", "Fermented African oil bean seeds")
    },
    "Which Nigerian soup is made using ground melon seeds cooked with leafy greens, palm oil, stock, and meats or fish?": {
        "choices": [
            ("A", "Egusi soup"),
            ("B", "Fura da Nono"),
            ("C", "Kunu Zaki"),
            ("D", "Masa")
        ],
        "correct": ("A", "Egusi soup")
    },
    "What is Tsire in Hausa meat preparation?": {
        "choices": [
            ("A", "Thinly sliced skewered meat coated in spiced peanut seasoning and roasted over charcoal or flame"),
            ("B", "Boiled cow tripe in a sour tamarind broth"),
            ("C", "Steamed millet dumplings in sweetened milk"),
            ("D", "Fermented cassava granules soaked in cold water")
        ],
        "correct": ("A", "Thinly sliced skewered meat coated in spiced peanut seasoning and roasted over charcoal or flame")
    },
    "Which traditional northern Nigerian drink is made from tiger nuts, often blended with dates and coconut?": {
        "choices": [
            ("A", "Kunun Aya"),
            ("B", "Zobo"),
            ("C", "Ogi"),
            ("D", "Ofada Stew")
        ],
        "correct": ("A", "Kunun Aya")
    },
    "What is Kunun Aya in northern Nigeria?": {
        "choices": [
            ("A", "A creamy drink made from tiger nuts, commonly blended with dates and coconut"),
            ("B", "A savory soup thickened with dried okra"),
            ("C", "A spicy beef jerky coated in groundnut paste"),
            ("D", "A yam pottage cooked with unbleached palm oil")
        ],
        "correct": ("A", "A creamy drink made from tiger nuts, commonly blended with dates and coconut")
    },
    "Which Yoruba bean dish is famous for its dark, rich palm-oil bean texture paired with a fiery, savory pepper stew and often eaten with agege bread or fried plantain?": {
        "choices": [
            ("A", "Ewa Agoyin"),
            ("B", "Miyan Kuka"),
            ("C", "Tuwon Dawa"),
            ("D", "Ofe Nsala")
        ],
        "correct": ("A", "Ewa Agoyin")
    },
    "Which traditional soup in southern Nigeria uses waterleaf and leafy greens with palm oil, periwinkles, and assorted proteins?": {
        "choices": [
            ("A", "Edikang Ikong"),
            ("B", "Fura da Nono"),
            ("C", "Kunun Zaki"),
            ("D", "Dan Wake")
        ],
        "correct": ("A", "Edikang Ikong")
    },
    "What is a common role of yam in Ofe Nsala (Igbo white soup)?": {
        "choices": [
            ("A", "Pieces of yam are cooked in the broth and mashed or blended to naturally thicken the soup without palm oil"),
            ("B", "Yam is sliced raw and served as a crunchy salad topping"),
            ("C", "Yam is fermented for a week to make the soup sour"),
            ("D", "Yam is deep-fried and used to replace all meat or fish")
        ],
        "correct": ("A", "Pieces of yam are cooked in the broth and mashed or blended to naturally thicken the soup without palm oil")
    },
    "Which northern Nigerian staple swallow is traditionally made from guinea corn (sorghum)?": {
        "choices": [
            ("A", "Tuwon Dawa"),
            ("B", "Amala"),
            ("C", "Eba"),
            ("D", "Iyan")
        ],
        "correct": ("A", "Tuwon Dawa")
    },
    "Which northern Nigerian staple swallow is traditionally made from maize (corn)?": {
        "choices": [
            ("A", "Tuwon Masara"),
            ("B", "Amala"),
            ("C", "Iyan"),
            ("D", "Eba")
        ],
        "correct": ("A", "Tuwon Masara")
    },
    "How is traditional Nigerian Pounded Yam (Iyan) prepared?": {
        "choices": [
            ("A", "Boiled yam chunks are pounded in a mortar with a pestle (or mashed/blended) until smooth and stretchy"),
            ("B", "Dried yam flour is whisked into cold water and baked"),
            ("C", "Grated raw yam is steamed in banana leaves like moi moi"),
            ("D", "Yam slices are sun-dried and fried in groundnut oil")
        ],
        "correct": ("A", "Boiled yam chunks are pounded in a mortar with a pestle (or mashed/blended) until smooth and stretchy")
    },
    "Which Nigerian snack is made from leavened wheat dough deep-fried into golden, airy balls?": {
        "choices": [
            ("A", "Puff-Puff"),
            ("B", "Akara"),
            ("C", "Kilishi"),
            ("D", "Kuli-Kuli")
        ],
        "correct": ("A", "Puff-Puff")
    },
    "What is Chin Chin in Nigerian snacking?": {
        "choices": [
            ("A", "Cut dough pieces—often flavored with nutmeg, milk, or sugar—deep-fried until crisp or crunchy"),
            ("B", "Steamed bean pudding wrapped in leaves"),
            ("C", "Fermented millet dough balls in sour milk"),
            ("D", "Roasted plantain slices with groundnut sauce")
        ],
        "correct": ("A", "Cut dough pieces—often flavored with nutmeg, milk, or sugar—deep-fried until crisp or crunchy")
    },
    "Which Nigerian pepper soup spice or seasoning profile is known for warming, aromatic spices such as calabash nutmeg (ehuru/uda) and scent leaf?": {
        "choices": [
            ("A", "Traditional Nigerian pepper soup"),
            ("B", "Ewedu soup"),
            ("C", "Gbegiri soup"),
            ("D", "Fura da Nono")
        ],
        "correct": ("A", "Traditional Nigerian pepper soup")
    },
    "What is Akara made from in Nigerian street food?": {
        "choices": [
            ("A", "Blended peeled beans seasoned with onions and peppers and deep-fried in oil"),
            ("B", "Fermented cassava flakes stirred into boiling water"),
            ("C", "Roasted groundnut cake pressed into sticks"),
            ("D", "Spiced dried beef strips")
        ],
        "correct": ("A", "Blended peeled beans seasoned with onions and peppers and deep-fried in oil")
    },
    "What is Moi Moi made from in Nigerian cuisine?": {
        "choices": [
            ("A", "Blended peeled beans with peppers, onions, and seasonings—often with oil, eggs, or fish—steamed until set"),
            ("B", "Sun-dried beef coated in groundnut paste"),
            ("C", "Fermented grain porridge served warm"),
            ("D", "Roasted unripe plantains with palm oil")
        ],
        "correct": ("A", "Blended peeled beans with peppers, onions, and seasonings—often with oil, eggs, or fish—steamed until set")
    },
    "Which traditional Nigerian soup is known for its draw texture from jute leaves?": {
        "choices": [
            ("A", "Ewedu soup"),
            ("B", "Ofada stew"),
            ("C", "Isi Ewu"),
            ("D", "Nkwobi")
        ],
        "correct": ("A", "Ewedu soup")
    },
    "Which southern Nigerian dish features shredded dried cassava mixed with palm oil, ugba, garden egg or leaves, fish, and pepper seasoning?": {
        "choices": [
            ("A", "Abacha (African salad)"),
            ("B", "Tuwo Shinkafa"),
            ("C", "Miyan Kuka"),
            ("D", "Kunun Zaki")
        ],
        "correct": ("A", "Abacha (African salad)")
    },
    "What is Zobo typically served as in Nigeria?": {
        "choices": [
            ("A", "A chilled or room-temperature spiced hibiscus drink"),
            ("B", "A hot bean swallow eaten with ewedu"),
            ("C", "A roasted meat skewer with yaji"),
            ("D", "A thick melon-seed soup")
        ],
        "correct": ("A", "A chilled or room-temperature spiced hibiscus drink")
    },
    "Which northern Nigerian drink is made from fermented sorghum, millet, or maize with spices like ginger and cloves?": {
        "choices": [
            ("A", "Kunun Zaki"),
            ("B", "Ofe Owerri"),
            ("C", "Efo Elegusi"),
            ("D", "Bole")
        ],
        "correct": ("A", "Kunun Zaki")
    },
    "In northern Nigeria, what is Fura?": {
        "choices": [
            ("A", "Cooked and spiced millet or sorghum dough shaped into balls"),
            ("B", "Palm oil stew made with locust beans"),
            ("C", "Steamed rice cakes cooked in a special pan"),
            ("D", "Fried plantain cubes with pepper")
        ],
        "correct": ("A", "Cooked and spiced millet or sorghum dough shaped into balls")
    },
    "In northern Nigeria, what is Nono in Fura da Nono?": {
        "choices": [
            ("A", "Fermented cow milk"),
            ("B", "Roasted groundnut oil"),
            ("C", "Dried baobab leaf powder"),
            ("D", "Fermented cassava flour")
        ],
        "correct": ("A", "Fermented cow milk")
    },
    "Which Nigerian condiment is made by fermenting locust beans and is widely used in soups and stews for umami?": {
        "choices": [
            ("A", "Iru (locust beans)"),
            ("B", "Garri"),
            ("C", "Ogi"),
            ("D", "Puff-Puff")
        ],
        "correct": ("A", "Iru (locust beans)")
    },
    "Which dish is traditionally associated with unbleached palm oil, locust beans, and fiery pepper stew alongside indigenous rice in southwestern Nigeria?": {
        "choices": [
            ("A", "Ofada rice and Ofada stew"),
            ("B", "Fura da Nono"),
            ("C", "Kunun Aya"),
            ("D", "Tuwon Masara")
        ],
        "correct": ("A", "Ofada rice and Ofada stew")
    },
    "Which traditional Igbo soup is made with bitter leaf that has been washed to temper its bitterness, paired with palm oil and cocoyam or egusi?": {
        "choices": [
            ("A", "Ofe Onugbu (Bitterleaf soup)"),
            ("B", "Kunun Zaki"),
            ("C", "Dan Wake"),
            ("D", "Masa")
        ],
        "correct": ("A", "Ofe Onugbu (Bitterleaf soup)")
    },
    "Which traditional Igbo soup features tender oha leaves torn by hand rather than cut with a knife to preserve texture?": {
        "choices": [
            ("A", "Oha Soup"),
            ("B", "Miyan Kuka"),
            ("C", "Gbegiri"),
            ("D", "Ewedu soup")
        ],
        "correct": ("A", "Oha Soup")
    },
    "Which Nigerian soup is made from palm fruit extract and seasoned with traditional spices and herbs?": {
        "choices": [
            ("A", "Banga soup"),
            ("B", "Kunun Aya"),
            ("C", "Fura da Nono"),
            ("D", "Ewa Agoyin")
        ],
        "correct": ("A", "Banga soup")
    },
    "What is Ogbono soup known for in Nigerian cuisine?": {
        "choices": [
            ("A", "Its thick, drawing texture from ground wild mango seeds"),
            ("B", "Being a cold fermented milk drink"),
            ("C", "Being made exclusively from roasted plantains"),
            ("D", "Being a sweet flour snack")
        ],
        "correct": ("A", "Its thick, drawing texture from ground wild mango seeds")
    },
    "Which Nigerian street food pairs roasted plantains with roasted groundnuts or spicy pepper sauce?": {
        "choices": [
            ("A", "Bole"),
            ("B", "Miyan Kuka"),
            ("C", "Tuwon Dawa"),
            ("D", "Ofe Nsala")
        ],
        "correct": ("A", "Bole")
    },
    "Which northern Nigerian meat dish is thinly sliced, dried, coated in a spiced groundnut paste mixture, and dried/roasted for long shelf life?": {
        "choices": [
            ("A", "Kilishi"),
            ("B", "Moi Moi"),
            ("C", "Puff-Puff"),
            ("D", "Ewedu soup")
        ],
        "correct": ("A", "Kilishi")
    },
    "Which northern Nigerian street food is skewered, seasoned with peanut spice mix (yaji), and grilled over open fire?": {
        "choices": [
            ("A", "Suya"),
            ("B", "Ogi"),
            ("C", "Asaro"),
            ("D", "Gbegiri")
        ],
        "correct": ("A", "Suya")
    },
    "Which Nigerian swallow is made by stirring garri (cassava flakes) into hot water until a smooth dough forms?": {
        "choices": [
            ("A", "Eba"),
            ("B", "Tuwo Shinkafa"),
            ("C", "Fura da Nono"),
            ("D", "Kunun Gyada")
        ],
        "correct": ("A", "Eba")
    },
    "Which Yoruba dish is made from peeled, boiled, and mashed/blended beans into a smooth yellow or pale brown soup often paired with ewedu and amala?": {
        "choices": [
            ("A", "Gbegiri"),
            ("B", "Kilishi"),
            ("C", "Bole"),
            ("D", "Zobo")
        ],
        "correct": ("A", "Gbegiri")
    },
    "Which Nigerian yam pottage is cooked with palm oil, peppers, onions, and seasoning until rich and partly mashed?": {
        "choices": [
            ("A", "Asaro"),
            ("B", "Fura da Nono"),
            ("C", "Kunun Zaki"),
            ("D", "Masa")
        ],
        "correct": ("A", "Asaro")
    },
    "Which northern Nigerian soup combines pumpkin/squash with savory spices, tomatoes, and oil?": {
        "choices": [
            ("A", "Miyan Taushe"),
            ("B", "Ofe Nsala"),
            ("C", "Efo Riro"),
            ("D", "Nkwobi")
        ],
        "correct": ("A", "Miyan Taushe")
    },
    "Which northern Nigerian soup uses ground baobab leaf powder for its signature texture?": {
        "choices": [
            ("A", "Miyan Kuka"),
            ("B", "Isi Ewu"),
            ("C", "Bole"),
            ("D", "Abacha")
        ],
        "correct": ("A", "Miyan Kuka")
    },
    "Which eastern Nigerian delicacy features spiced cow foot in a rich palm-oil sauce garnished with sliced onions and utazi leaves?": {
        "choices": [
            ("A", "Nkwobi"),
            ("B", "Tuwon Masara"),
            ("C", "Kunun Aya"),
            ("D", "Ogi")
        ],
        "correct": ("A", "Nkwobi")
    },
    "Which eastern Nigerian delicacy centers on a well-seasoned goat head in a savory palm-oil sauce?": {
        "choices": [
            ("A", "Isi Ewu"),
            ("B", "Ewa Agoyin"),
            ("C", "Miyan Taushe"),
            ("D", "Fura da Nono")
        ],
        "correct": ("A", "Isi Ewu")
    },
    "Which northern Nigerian street or home dumpling is made from bean flour and served with oil, yaji, onions, and sometimes boiled egg?": {
        "choices": [
            ("A", "Dan Wake"),
            ("B", "Efo Riro"),
            ("C", "Ofe Owerri"),
            ("D", "Banga soup")
        ],
        "correct": ("A", "Dan Wake")
    },
    "Which Nigerian breakfast/snack porridge is made from fermented maize, millet, or sorghum paste?": {
        "choices": [
            ("A", "Ogi (Pap)"),
            ("B", "Kilishi"),
            ("C", "Nkwobi"),
            ("D", "Isi Ewu")
        ],
        "correct": ("A", "Ogi (Pap)")
    },
    "Which Nigerian dish pairs mashed or blended melon seeds with leafy greens, palm oil, and assorted meats or fish?": {
        "choices": [
            ("A", "Egusi soup"),
            ("B", "Kunun Zaki"),
            ("C", "Fura da Nono"),
            ("D", "Masa")
        ],
        "correct": ("A", "Egusi soup")
    },
    "Which southern Nigerian soup combines leafy greens, waterleaf, palm oil, and proteins such as beef, stockfish, periwinkles, or dried fish?": {
        "choices": [
            ("A", "Edikang Ikong"),
            ("B", "Tuwon Dawa"),
            ("C", "Kunun Gyada"),
            ("D", "Ogi")
        ],
        "correct": ("A", "Edikang Ikong")
    },
    "Which Nigerian snack is made by pressing spiced groundnut cake after oil extraction and frying it crisp?": {
        "choices": [
            ("A", "Kuli-Kuli"),
            ("B", "Amala"),
            ("C", "Eba"),
            ("D", "Iyan")
        ],
        "correct": ("A", "Kuli-Kuli")
    },
    "Which northern Nigerian rice swallow is cooked soft and mashed into a smooth dough to pair with soups?": {
        "choices": [
            ("A", "Tuwo Shinkafa"),
            ("B", "Efo Riro"),
            ("C", "Gbegiri"),
            ("D", "Ewedu soup")
        ],
        "correct": ("A", "Tuwo Shinkafa")
    },
    "Which Yoruba swallow is made from yam flour (elubo) stirred into boiling water?": {
        "choices": [
            ("A", "Amala"),
            ("B", "Fura da Nono"),
            ("C", "Kunun Aya"),
            ("D", "Bole")
        ],
        "correct": ("A", "Amala")
    },
    "Which Nigerian spice blend containing ground roasted peanuts, chili, ginger, and seasonings is used on grilled meats like suya?": {
        "choices": [
            ("A", "Yaji"),
            ("B", "Ogi"),
            ("C", "Zobo"),
            ("D", "Masa")
        ],
        "correct": ("A", "Yaji")
    },
    "Which fermented condiment is used in many Nigerian soups and sauces to add deep savory flavor?": {
        "choices": [
            ("A", "Iru / Ogiri"),
            ("B", "Puff-Puff"),
            ("C", "Chin Chin"),
            ("D", "Akara")
        ],
        "correct": ("A", "Iru / Ogiri")
    },
    "Which southeastern Nigerian dish uses African breadfruit seeds cooked savory with palm oil or in porridge?": {
        "choices": [
            ("A", "Ukwa"),
            ("B", "Miyan Kuka"),
            ("C", "Tuwon Masara"),
            ("D", "Fura da Nono")
        ],
        "correct": ("A", "Ukwa")
    },
    "Which traditional Nigerian soup is made without palm oil, using peppery broth, protein, and yam as a natural thickener?": {
        "choices": [
            ("A", "Ofe Nsala (White Soup)"),
            ("B", "Efo Elegusi"),
            ("C", "Banga soup"),
            ("D", "Ofada stew")
        ],
        "correct": ("A", "Ofe Nsala (White Soup)")
    },
    "Which northern Nigerian pancake-like cake is made from fermented rice or millet batter in a special pan?": {
        "choices": [
            ("A", "Masa"),
            ("B", "Nkwobi"),
            ("C", "Isi Ewu"),
            ("D", "Abacha")
        ],
        "correct": ("A", "Masa")
    },
    "Which leafy vegetable is commonly known as zogale in northern Nigeria and used in soups and side dishes?": {
        "choices": [
            ("A", "Moringa leaves"),
            ("B", "Jute leaves"),
            ("C", "Waterleaf"),
            ("D", "Bitter leaf")
        ],
        "correct": ("A", "Moringa leaves")
    },
    "Which Nigerian meat preparation roasts seasoned meat on sticks near an open fire and is served with yaji?": {
        "choices": [
            ("A", "Balangu"),
            ("B", "Moi Moi"),
            ("C", "Efo Riro"),
            ("D", "Gbegiri")
        ],
        "correct": ("A", "Balangu")
    },
    "Which Nigerian drink is made from tiger nuts, dates, and coconut?": {
        "choices": [
            ("A", "Kunun Aya"),
            ("B", "Ewedu soup"),
            ("C", "Asaro"),
            ("D", "Kilishi")
        ],
        "correct": ("A", "Kunun Aya")
    },
    "Which Nigerian bean dish is slow-cooked with palm oil and a rich pepper-onion sauce, often paired with bread or fried plantain?": {
        "choices": [
            ("A", "Ewa Agoyin"),
            ("B", "Miyan Taushe"),
            ("C", "Tuwon Dawa"),
            ("D", "Ofe Nsala")
        ],
        "correct": ("A", "Ewa Agoyin")
    },
    "Which traditional Nigerian soup relies on ground melon seeds, palm oil, leafy greens, and savory seasonings?": {
        "choices": [
            ("A", "Egusi soup"),
            ("B", "Fura da Nono"),
            ("C", "Kunun Zaki"),
            ("D", "Bole")
        ],
        "correct": ("A", "Egusi soup")
    },
    "Which Nigerian snack consists of deep-fried dough pieces flavored with spices or milk?": {
        "choices": [
            ("A", "Chin Chin"),
            ("B", "Ofe Owerri"),
            ("C", "Isi Ewu"),
            ("D", "Nkwobi")
        ],
        "correct": ("A", "Chin Chin")
    },
    "Which traditional Nigerian swallow is made by mashing or pounding boiled yam until smooth?": {
        "choices": [
            ("A", "Iyan"),
            ("B", "Zobo"),
            ("C", "Kuli-Kuli"),
            ("D", "Yaji")
        ],
        "correct": ("A", "Iyan")
    },
    "Which Nigerian drink is brewed from dried hibiscus petals and spiced with ginger, cloves, or fruit?": {
        "choices": [
            ("A", "Zobo"),
            ("B", "Eba"),
            ("C", "Amala"),
            ("D", "Tuwo Shinkafa")
        ],
        "correct": ("A", "Zobo")
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
       
      
title_label = tk.Label(root, text="Nigerian Food Trivia.", font=("Arial", 25))
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