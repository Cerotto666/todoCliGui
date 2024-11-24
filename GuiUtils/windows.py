import PySimpleGUI as sg
from GuiUtils import utils as u
from Modules.Constants import windows_status as ws

def get_layout_home():
    return [
        [sg.Column([[sg.Text("TODO APP", font=("Helvetica", 20), justification="center", size=(20, 1))]],
                   justification="center")],
        [sg.Column([[sg.Text("_" * 80, justification="center")]], justification="center")],
        [sg.Column([[sg.Text(ws.BASE, font=("Helvetica", 20), key="action")]], justification="Left")],
        [sg.Column(
            [
                [sg.Listbox(values = [], key="todos", enable_events=True, size = (60,12), expand_x=True, expand_y=True,pad=(30,15), font=("Helvetica", 16))]
            ]),
        sg.Column(
            [
                [sg.Button("CREA", key="CREA", size=(17, 3), button_color=("white", "#28a745"), font=("Helvetica", 12))],
                [sg.Button("RINOMINA", key="RINOMINA", size=(17, 3), button_color=("white", "#6c757d"), font=("Helvetica", 12))],
                [sg.Button("MODIFICA", key="MODIFICA", size=(17, 3), button_color=("white", "#007bff"), font=("Helvetica", 12))],
                [sg.Button("VISUALIZZA", key = "VISUALIZZA", size=(17, 3), button_color=("white", "#17a2b8"), font=("Helvetica", 12))],
                [sg.Button("CANCELLA", key = "CANCELLA", size=(17, 3), button_color=("white", "#dc3545"), font=("Helvetica", 12))],
                [sg.Text("")],  # Spazio vuoto
                [sg.Button("Esci", key="Esci", size=(17, 3), button_color=("white", "#6C757D"), font=("Helvetica", 12))]
            ],
            justification="right",  # Centro dei bottoni
            element_justification="center",  # Centro degli elementi nella colonna,
            expand_x=True, expand_y=True,
            pad=(10, 15)
        )],
        [
            sg.Column(
                [
                    [sg.InputText(tooltip="Enter todo", key="todo", size = (60, 1), font=("Helvetica", 16), disabled=True)]
                ]
                , pad = (38,0)),
            sg.Column(
                [
                    [sg.Button("OK", size=(17, 3), button_color=("white", "green"), font=("Helvetica", 12),pad=(15,0))]
                ]
                ,element_justification="center",
                expand_x=True, expand_y=True,
                pad=(10,15))
        ]
    ]



def get_layout_modifica():
    return [
        [sg.Text("MODIFICA")],
        [sg.Button("HOME")]
    ]

def get_layout_visualizza():
    return [
        [
            sg.Column([
                [sg.Text("TODO", font=("Helvetica", 14), justification="center", size=(20, 1))],
                [sg.Listbox(values = [], key="visualizza_todos", enable_events=False, size = (40,10), expand_x=True, expand_y=True,pad=(30,15), font=("Helvetica", 14))],
                [sg.Text("DONE", font=("Helvetica", 14), justification="center", size=(20, 1))],
                [sg.Listbox(values=[], key="visualizza_done", enable_events=False, size=(40, 10), expand_x=True, expand_y=True, pad=(30, 15), font=("Helvetica", 14))]
            ],
                justification="left",  # Centro dei bottoni
                element_justification="center",  # Centro degli elementi nella colonna,
                expand_x=True, expand_y=True,
                pad=(10, 15)
            ),
            sg.Column([
                [sg.Text("LISTA FILE", font=("Helvetica", 14), justification="center", size=(20, 1))],
                [sg.Listbox(values = [], key="visualizza_file", enable_events=True, size=(40, 12), expand_x=True, expand_y=True,pad=(30, 15), font=("Helvetica", 16))]
            ],
                justification="right",  # Centro dei bottoni
                element_justification="center",  # Centro degli elementi nella colonna,
                expand_x=True, expand_y=True,
                pad=(10, 15)
            )
        ],
        [
            sg.Column([
                [sg.Button("INDIETRO", key = "INDIETRO", size=(15, 2), button_color=("white", "#dc3545"), font=("Helvetica", 12))]
            ],
                justification="center",  # Centro dei bottoni
                element_justification="center",  # Centro degli elementi nella colonna,
                expand_x=True, expand_y=True,
                pad=(10, 15)
            )
        ]
    ]

def get_layout_bye():

    image_path = "Images/bye.png"
    new_size = (200, 200)

    resized_img = u.resize_image(image_path, new_size)
    return [
        [sg.Image(data=resized_img)],  # Cambia "path/to/your/image.png" con il percorso dell'immagine
        [sg.Text("Grazie per aver usato la nostra applicazione!",
                 font=("Helvetica", 18), justification="center", size=(30, 2))],
        [sg.Text("Arrivederci e a presto! 😊",
                 font=("Helvetica", 14), justification="center", size=(30, 1))],
        [sg.Button("Chiudi", size=(10, 1), button_color=("white", "#007BFF"), font=("Helvetica", 12))]
    ]

