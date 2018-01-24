import random

possible_answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

user_question = input("Ask me a question (type 'quit' to exit): ")
while user_question != 'quit':
	if user_question[-1] == '?':
		print(random.choice(possible_answers))
	else:
		print("I'm sorry, please state that in the form of a question")
	user_question = input("Ask me a question (type 'quit' to exit): ")
