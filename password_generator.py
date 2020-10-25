import PySimpleGUI as sg
import string
import random

class GeneratorScreen:
    def __init__(self):
        layout = [
            [sg.Text('Python Password Generator', justification='center', font=(12))],
            [sg.Output(key='inputScreen', font=(12))],
            [sg.Button('Copy', font=(12), key='copy'), sg.Button('Generate', font=(12), key='generate', focus=True)],
            [sg.Text('github.com/filipespadetto', justification='center')]
        ]

        self.window = sg.Window('Password Generator', layout)
    
    def Initiate(self):
        while True:
            event, values = self.window.Read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'generate':
                new_password = self.generate_password(values)
                print(new_password)
    
    def generate_password(self, values, length=8):
        letters = string.ascii_letters
        numbers = string.digits
        punctuation = string.punctuation

        printable = f'{letters}{numbers}{punctuation}'
        printable = list(printable)
        random.shuffle(printable)

        random_password = random.choices(printable, k=length)
        random_password = ''.join(random_password)
        return random_password

screen = GeneratorScreen()
screen.Initiate()