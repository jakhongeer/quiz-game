from question_model import Question
from quiz_brain import QuizBrain

question_bank = []


for i in question_data:
    question_text = i['question']
    question_answer = i['correct_answer']
    new_question = Question(text=question_text, answer=question_answer)

    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Congratulations! You've completed the quiz.")
print(f"Your final score was {quiz.score} out of {len(quiz.question_list)}")