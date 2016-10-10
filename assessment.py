"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   The three main design advantages provided by object orientation are 
   abstraction, encapsulation, and polymorphism.  

   Abstraction consists of creating methods that the user can use without 
   needing to know how the methods are working in the background.

   Encapsulation consists of keeping the attributes of something together
   with the functions that are going to be using that data.  

   Polymorphism consists of including common methods between subclasses in
   the superclass, eliminating the need for if-else statements for each
   subclass.

2. What is a class?

    A class is a type of thing, such as a string, file, or something 
    user-defined, which can define attributes and methods.

3. What is an instance attribute?
    
    An instance attribute is an attribute of each individual instance of
    a class.

4. What is a method?

    A method is a function defined on a class (inside a class definition).

5. What is an instance in object orientation?

    An instance is an object of the type Class.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   Every instance of a class will have the class attributes defined by the 
   class.  For example, if we had a Ball class, we could define a class 
   attribute ball_shape = 'round', because all balls are round.  An instance
   attribute is specific to each instance.  We could define an instance 
   attribute ball_color, which would change from ball to ball (brown for 
    basketball, yellow for tennis ball, etc.)


"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
    """A class for any student"""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.score = ""


class Question(object):
    """A class for any question"""

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """Ask the user for an answer and return True if it is correct"""
        print self.question
        user_answer = raw_input("What's your answer? > ")
        return user_answer == self.correct_answer

class Exam(object):
    """A class for any exam"""

    def __init__(self, name):
        self.name = name
        self.questions = []
        self.answers = []
        self.score = int()

    def add_question(self, question, correct_answer):
        """Add question and answer to the questions and answers attribute lists"""
        self.questions.append(question)
        self.answers.append(correct_answer)

    def administer(self):
        """Administer test and return score"""
        score = 0
        # For question in self.questions:
        for i in range(len(self.questions)):
            current_question = Question(self.questions[i], self.answers[i])
            if current_question.ask_and_evaluate():
                score += 1
        
        # Return score as a percent, between 0 and 100.
        return float(score) / len(self.questions) * 100


class Quiz(Exam):
    """A class for quizzes"""
    def __init__(self):
        super(Quiz, self).__init__("Quiz")

    def administer(self):
        score = super(Quiz, self).administer()
        return score >= 50

def take_test(exam, student):
    """Takes an exam and a student as parameters, administers the exam,
        and assigns the score to the student instance as a new attribute 
        called score."""
    # Administer the exam and assign the score to the student.
    student.score = exam.administer()


def example():
    """Creates an exam with questions and a student.  Administers exam
        to the student."""
    # Create an exam.
    final = Exam("Final exam")

    # Add questions to the exam.
    final.add_question("Who was the first president of the US?", "George Washington")
    final.add_question("What color is a sunflower?", "yellow")
    final.add_question("What day of the week is Thanksgiving?", "Thursday")

    # Create a student.
    alex = Student("Alex", "McLean", "Walnut Creek")

    # Administer the test to the student.
    final.administer()
