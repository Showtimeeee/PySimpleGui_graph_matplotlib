import PySimpleGUI as sg
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



def update_par(data):
    axes = fig.axes
    x = [i[0] for i in data]
    y = [int(i[1]) for i in data]
    axes[0].plot(x, y, 'b-')
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack()




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

# gui + graph
window = sg.Window('Quick Graph', maket, finalize=True)

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

    if event == 'Принять':
        new_value = values['-INPUT-']
        if new_value.isnumeric():
            table_content.append([len(table_content) + 1, float(new_value)])
            window['-TABLE-'].update(table_content)
            window['-INPUT-'].update('')
            update_par(table_content)

window.close()

