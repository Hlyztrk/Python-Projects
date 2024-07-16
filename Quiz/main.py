from question import Question
from data import question_data
from quiz import QuizBrain


# Create a list of question objects / which consist of question objects
question_list = []
for i in question_data:
     text = i['text']
     answer = i['answer']
     question = Question(text, answer)
     question_list.append(question)


quiz = QuizBrain(question_list)

while quiz.still_has_questions():
    quiz.next_question()
    


