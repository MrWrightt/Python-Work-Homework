# Name: Javar Wright
# Student: 1096440
# Section: 07
# Module 5 Assignment 3



triviabank_dict = {}

print("Welcome to the trivia builder 3000")

while True:
   question_str = input("Enter the next question: ")

   if question_str == "":
       print("You did not enter a question, let's try again.")
       continue

   if question_str == "Done":
       print("We will stop entering questions now")
       break

   answer_srt = input("Enter the correct answer: ")
   triviabank_dict[question_str] = answer_srt

print("Here is the final trivia dictionary:")
for question_str, answer_srt in triviabank_dict.items():
    print(f"The question is: {question_str}")
    print(f"And the answer is: {answer_srt}")