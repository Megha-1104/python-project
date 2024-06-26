# Python project for creating a Quiz Game 

class Question:

# Creating a funtion to fetch the data from question_data
    def __init__(self, prompt, options, correct_answer):
        self.prompt = prompt
        self.options = options
        self.correct_answer = correct_answer 

# Creating a function to display questions 
    def display_question(self):
        print(self.prompt)
        for idx, option in enumerate(self.options):
            print(f"{idx + 1}. {option}")

# creating a function to validate the answer
    def check_answer(self, user_answer):
        return user_answer == self.correct_answer


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
    
    def run_quiz(self):
        print("Welcome to Quiz Game")

        print("LET'S PLAY ........")
        for question in self.questions:
            question.display_question()
            user_answer = self.get_user_input()
            if question.check_answer(user_answer):
                print("Correct!\n")
                self.score += 1
                print (" Your score is :" ,self.score)
            else:
                print(f"Sorry, incorrect. The correct answer was: {question.options[question.correct_answer - 1]}\n")
        
        print(f"Quiz completed! Your final score is: {self.score}/{len(self.questions)}")
    
    def get_user_input(self):
        while True:
            try:
                user_input = int(input("Enter your answer (1, 2, 3, or 4): "))
                if 1 <= user_input <= len(self.questions[0].options):
                    return user_input
                else:
                    print("Please enter a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")

# Example usage:
def main():
    # Define questions
    question_data = [
        "\n Q1.What is the capital of France?\n",
        "\n Q2.Who wrote 'Hamlet'?\n",
        "\n Q3.Which planet is known as the Red Planet?\n",
        "\n Q4.Which animal lays the largest egg?\n",
        "\n Q5.How many bones do human body have?\n"
    ]
    questions = [
        Question(question_data[0], ["Paris", "Madrid", "Rome", "Berlin"], 1),
        Question(question_data[1], ["William Shakespeare", "Charles Dickens", "Jane Austen", "Fyodor Dostoevsky"], 1),
        Question(question_data[2], ["Jupiter", "Mars", "Venus", "Saturn"], 2),
        Question(question_data[3], ["Elephant", "Whale", "Ostrich", "Eagle"], 3),
        Question(question_data[2], ["205", "206", "207", "208"], 2)
    ]

    # Create quiz
    quiz = Quiz(questions)
    quiz.run_quiz()

if __name__ == "__main__":
    main()