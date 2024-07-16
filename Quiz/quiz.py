class QuizBrain:

    '''Create a constructor with question_list and question_number attributes'''
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_num = 0
        self.score = 0

    '''Hold the current question which will form the question list'''
    def next_question(self):
        current_question = self.question_list[self.question_num]
        user_guess = input(f"Q{self.question_num + 1}: {current_question.text} (True/False) ? ")
        self.check_answers(user_guess, current_question.answer)
        self.question_num += 1

   
    def still_has_questions(self):
        return self.question_num < len(self.question_list)
    
    def check_answers(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"You got it right.")
        else:
            print(f"Wrong answer")

        print(f"The correct answer was: {correct_answer}\nYour current score is {self.score}/{self.question_num + 1}\n")
    

