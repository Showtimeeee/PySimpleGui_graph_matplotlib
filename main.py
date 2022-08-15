import PySimpleGUI as sg
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# func graph
def update_par(data):
    # оси
    axes = fig.axes
    # x = first el
    x = [i[0] for i in data]
    # int for graph accuracy
    y = [int(i[1]) for i in data]
    # points connected by green lines
    axes[0].plot(x, y, 'g-')
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack()


# beautiful theme
sg.theme("DarkTeal2")

# counter
table_content = []

# create layout and add 2 header arguments, resize window, scroll, table
maket = [
    [sg.Table(
        headings=['Ось', 'Область'],
        values=table_content,
        expand_x=True,
        hide_vertical_scroll=True,
        key='-TABLE-')],
    [sg.Input(key='-INPUT-', expand_x=True), sg.Button('Принять')],
    [sg.Canvas(expand_x=True), sg.Button('Удалить')],
    [sg.Canvas(key='-CANVAS-')]
]

# gui + graph, finalize to edit
window = sg.Window('Quick Graph', maket, finalize=True)

# matplotlib
fig = matplotlib.figure.Figure(figsize=(5, 5))
# draw plot in CANVAS, 111 = 1×1 grid
fig.add_subplot(1, 1, 1).plot([], [])
figure_canvas_agg = FigureCanvasTkAgg(fig, window['-CANVAS-'].TKCanvas)
figure_canvas_agg.draw()
figure_canvas_agg.get_tk_widget().pack()


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    # counter
    if event == 'Принять':
        new_value = values['-INPUT-']
        # check if the type is numeric, append [] + 1
        if new_value.isnumeric():
            table_content.append([len(table_content) + 1, float(new_value)])
            window['-TABLE-'].update(table_content)
            # func
            update_par(table_content)
            # clear input
            window['-INPUT-'].update('')

    # clear table
    if event == 'Удалить':
        window['-TABLE-'].update([])
        window['-INPUT-'].update('')


window.close()

