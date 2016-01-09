from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import random
import math


class FlashCard(BoxLayout):

    # Override the initialization
    def __init__(self, **kwargs):
        
        # Call the super constructor and then set the orientation
        super(FlashCard, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Load in the list of questions
        self.question_list = []
        with open("Questions.txt", "r") as ins:
            for line in ins:
                self.question_list.append(line)
    
        # Pick a random question
        self.question_number = int(math.ceil(random.uniform(0,len(self.question_list)/2)))
        
        # Add the first question
        self.question = Label(text=self.question_list[2*(self.question_number-1)])
        self.add_widget(self.question)
        
        # Add a status bar
        self.correct_answer = Label(text='Correct Answer:')
        self.add_widget(self.correct_answer)
        
        # Add the answer box
        self.answer = TextInput(multiline=False)
        self.add_widget(self.answer)
        
        # Add the submit button
        self.submit = Button(text='Submit')
        self.submit.bind(on_press=self.check_answer)
        self.add_widget(self.submit)
                
        # Add the next question button
        self.next = Button(text='Next Question')
        self.next.bind(on_press=self.next_question)
        self.add_widget(self.next)

    # Function for displaying the answer
    def check_answer(self, instance):

        # Update the correct answer
        self.correct_answer.text = 'Correct Answer: ' + self.question_list[2*(self.question_number-1)+1]

    # Function for displaying the answer
    def next_question(self, instance):
        
        # Pick a random question
        self.question_number = int(math.ceil(random.uniform(0,len(self.question_list)/2)))

        # Set the next question
        self.question.text = self.question_list[2*(self.question_number-1)]

        # Clear the correct answer
        self.correct_answer.text = 'Correct Answer:'

        # Clear the text box
        self.answer.text = ''

class RunQuiz(App):

    def build(self):
        return FlashCard()


if __name__ == '__main__':
    RunQuiz().run()



