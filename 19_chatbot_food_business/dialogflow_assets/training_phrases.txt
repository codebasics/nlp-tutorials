# Author: Dhaval Patel. Codebasics YouTube Channel

Default Welcome Intent
======================
Text response:  Hello, How can I help you? You can say "New Order" or "Track Order"
				Good day! What can I do for you today? You can say "New Order" or "Track Order"
				Greetings! How can I assist? You can say "New Order" or "Track Order"

				
Default Fallback Intent
========================
Text Response: I didn't understand. You can say 'New Order' or 'Track Order'. Also, in a new order, please mention only items from our available menu: Pav Bhaji, Chole Bhature, Pizza, Mango Lassi, Masala Dosa, Biryani, Vada Pav, Rava Dosa, and Samosa. Also specify a quantity for each item for example: "One pizza and 2 chole bhature"				


Intent= new.order
=================
new order
Place new order

	Text Response = 
		Ok, starting a new order. You can say things like "I want two pizzas and one mango lassi". Make sure to specify a quantity for every food item! Also, we have only the following items on our menu: Pav Bhaji, Chole Bhature, Pizza, Mango Lassi, Masala Dosa, Biryani, Vada Pav, Rava Dosa, and Samosa.

		Starting new order. Specify food items and quantities. For example, you can say, "I would like to order two pizzas and one mango lassi. Also, we have only the following items on our menu: Pav Bhaji, Chole Bhature, Pizza, Mango Lassi, Masala Dosa, Biryani, Vada Pav, Rava Dosa, and Samosa.

Intent= order.add - context: ongoing-order
==========================================
Give me 2 plates of chole bhature, one cheese pizza
I'd like to order two plates of chole bhature,  one cheese pizza, and 3 mango lassi, please.
Can you please get me two servings of chole bhature, one cheese pizza, and one mango lassi?
Please prepare 2 portions of chole bhature, along with one cheese pizza and 1 mango lassi for me
3 biryani, 2 lassi, 1 pav bhaji
Can I get 2 plates of chole bhature, along with one cheese pizza and 1 mango lassi?
I'll take 2 orders of chole bhature, one cheese pizza, and 1 mango lassi, if you don't mind
I want 1 lassi, 2 chhole bhature and one vada paav, do it fast plz
In addition, add 1 bhaji pav and 2 pizzas
Moreover, include 2 mango lassi
Also, please give me 2 mango lassi
Additionally, I'd like 2 mango lassi.
2 pizza and ok lets add one biryani too
3 biryani
Oh yes, add one pav bhaji as well

Intent= order.complete - context: ongoing-order
==========================================
Nope
That's all I needed
Done ordering it
Place an order
Done
That's it

Intent= order.remove - context: ongoing-order
==========================================
No pav bhaji and samosa in my order. please remove.
Kindly take pav bhaji and samosa off the order, please.
I'd like to exclude pav bhaji and samosa, please
I no longer want the rava dosa in my order, please remove it
Kindly exclude the rava dosa from my order
I would like to remove the pizza from my order
Please take the pizza off my order
delete chole from my order
hey, plz get rid of rava dosa and samosa
I don't want pav bhaji
remove pizza from my order
can you remove mango lassi?

Intent= track.order
===================

check the status of my order
track order
track existing order

Text response:
	Definitely. What is your order id?
	Sure. Please enter your order id.
	Definitely. What is your order id?


Intent= track.order - context: ongoing-tracking
==================================================
how about 32
how about 40?
here it is - 63321
here you go: 123
here is my order number 675
id is 453
here is my order id # 341
7890
123
345
