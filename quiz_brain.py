class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number+=1
        user = input(f"Q.{self.question_number}:{current_question.text} (True or False):")
        self.check_answer(user,current_question.answer)
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            False
    def check_answer(self,user_answer,correct_answer):
        if user_answer == correct_answer:
            print("Correct")
        else:
            print("Wrong Answer")

