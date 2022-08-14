import PySimpleGUI as sg
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


sg.theme("LightBlue")
table_content = []
maket = [
    [sg.Table(
        headings=['Ось', 'Область'],
        values=table_content,
        expand_x=True,
        hide_vertical_scroll=True,
        key='-TABLE-')],
    [sg.Input(key='-INPUT-', expand_x=True), sg.Button('Принять')],
    [sg.Canvas(key='-CANVAS-')]
]

window = sg.Window('Quick Graph', maket)

# matplotlib
fig = matplotlib.figure.Figure(figsize=(5, 5))
fig.add_subplot(111).plot([], [])
figure_canvas_agg = FigureCanvasTkAgg(fig, window['-CANVAS-'].TKCanvas)
figure_canvas_agg.draw()
figure_canvas_agg.get_tk_widget().pack()


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()

