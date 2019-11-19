# from question import Question



# question_prompts = [
    
#     "Name the city in China that has the highest population?\n(a) Nanjing\n(b) Beijing\n(c) Shanghai\n(d) Shenzhen\n\n",
#     "Which among the following is river mentioned represents the colours Blue and white?\n (a) Ganges\n (b) Nile\n (c) Danube\n (d)Yangtze\n\n",
#     "Mojave Desert is located in which place?\n(a) Peru, Chile\n(b) China, Mongolia\n(c) S.W Africa\n(d) California, USA\n\n"
# ]

# questions = [
#     Question(question_prompts[0],"c"),
#     Question(question_prompts[1],"b"),
#     Question(question_prompts[2],"d")

# ]

# def run(questions):
#     score = 0
#     for question in questions:
#         answer = input(question.prompt)
#         if answer == question.answer:
#             score += 1
#     print(f"Your score is {score}/3 so far! ")
# run(questions)

# print("")
# print("")
# answer1 = str(input('''Question-1) The country which was earlier called as Siam?

# (a) Vietnam

# (b) Cambodia

# (c) Thailand

# (d) Laos

# '''))

# def multiple_choice(answer1):
#     if answer1 == "c":
#         print("Q1:Correct!")

#     else:
#         print("Q1:Not Correct! The answer is Thailand.")

# answer2 = int(input('''How many states are there in the United States? (Please enter an integer)
# '''))

# def numeric_response(answer2):
#     if answer2 == 50:
#         print("Q2:Correct!")
#     else:
#         print("Q2:Not Correct! The answer is 50")

# answer3 = int(input("""

# Alaska was the last state to enter the Union, 
# true or false? Please enter only digits.

# """))
# def true_false(answer3):
#     if answer3 > 0:
#         print("Q3:Correct!")
#     else:
#         print("Q3:False! Note: ")





# multiple_choice(answer1)
# numeric_response(answer2)
# true_false(answer3)







