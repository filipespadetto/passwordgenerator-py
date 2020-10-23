import PySimpleGUI as sg

sg.theme('Reddit')

layout = [
    [sg.Text("Python Password Generator", justification='center', font=(12))],
    [sg.Input(key="generator", font=(12), disabled=True)],
    [sg.Button("Copy", font=(12)), sg.Button("Generate", font=(12), focus=True)],
    [sg.Text("github.com/filipespadetto", justification='center')]
]

window = sg.Window("Password Generator", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
window.close()