from question import Question



question_prompts = [
    
    "Name the city in China that has the highest population?\n(a) Nanjing\n(b) Beijing\n(c) Shanghai\n(d) Shenzhen\n\n",
    "Which among the following is river mentioned represents the colours Blue and white?\n (a) Ganges\n (b) Nile\n (c) Danube\n (d)Yangtze\n\n",
    "Mojave Desert is located in which place?\n(a) Peru, Chile\n(b) China, Mongolia\n(c) S.W Africa\n(d) California, USA\n\n"
]

questions = [
    Question(question_prompts[0],"c"),
    Question(question_prompts[1],"b"),
    Question(question_prompts[2],"d")

]

def run(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(f"Your score is {score}/3 so far! ")
run(questions)

print("")
print("")

answer1 = str(input('''Question-4) The country which was earlier called as Siam?

(a) Vietnam

(b) Cambodia

(c) Thailand

(d) Laos

'''))


def multiple_choice(answer1):
    if answer1 == "c":
        print("Q4:Correct!")

    else:
        print("Q4:Not Correct! The answer is Thailand.")
print("")
print("")
answer2 = (input('''
Question-5) How Many Planets Are in Our Solar System? ? (Please enter an integer)
'''))

def numeric_response(answer2):
    if answer2 == 8:
        print("Q5:Correct!")
    else:
        print("Q5:Not Correct! The answer is 8 Planets.")
print("")
print("")
answer3 = (input("""

Question-6) Did Cristiano Ronaldo won 5 GOLDEN BALL?
True (1) or False (0)? Please enter only digits.

"""))
def true_false(answer3):
    if answer3 == 1:
        print("Q6:Correct!")
     
    else:
        print("""Q6:False! Note: Portuguese footballer Cristiano Ronaldo, has received five Ballon d'Or awards, 
        the most for a European player and is tied for most all-time. ... 
        Moreover, he is also the first player in history to win four European Golden Shoes. 
        
        """)

multiple_choice(answer1)
numeric_response(answer2)
true_false(answer3)






