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
        [
            sg.Column([
                [sg.Text("TODOS", font=("Helvetica", 20), justification="center", size=(20, 1))],
                [sg.Listbox(values = [], key="visualizza_todos_modifica", enable_events=True, size = (40,20), expand_x=True, expand_y=True,pad=(30,15), font=("Helvetica", 14))],
                [sg.Button("MARK AS", key = "mark_as", size=(15, 2), button_color=("white", "#dc3545"), font=("Helvetica", 12), disabled=True)]
            ],
            element_justification="center"),
            sg.Column([
                [sg.Text("DONES", font=("Helvetica", 20), justification="center", size=(20, 1))],
                [sg.Listbox(values=[], key="visualizza_dones_modifica", enable_events=True, size=(40, 20),
                            expand_x=True, expand_y=True, pad=(30, 15), font=("Helvetica", 14))],
                [sg.Button("INDIETRO", key="indietro_modifica", size=(15, 2), button_color=("white", "#dc3545"),
                           font=("Helvetica", 12))]
            ],
            element_justification="center")
        ],
        [
            sg.Column([
                [
                    sg.InputText( key="todo_to_edit", size = (60, 1), font=("Helvetica", 16), disabled=True),
                    sg.Button("MODIFICA", key="modifica_modifica", size=(17, 3), button_color=("white", "#6c757d"), font=("Helvetica", 12), disabled=True),
                    sg.Button("CANCELLA", key="cancella_modifica", size=(17, 3), button_color=("white", "#dc3545"), font=("Helvetica", 12), disabled=True),
                    sg.Button("AGGIUNGI", key="aggiungi_modifica", size=(17, 3), button_color=("white", "#dc2266"),
                              font=("Helvetica", 12), disabled=False)
                ]
            ])
        ]
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

def get_layout_bye(base_path):


    new_size = (200, 200)

    resized_img = u.resize_image(new_size, base_path)
    return [
        [sg.Image(data=resized_img)],  # Cambia "path/to/your/image.png" con il percorso dell'immagine
        [sg.Text("Grazie per aver usato la nostra applicazione!",
                 font=("Helvetica", 18), justification="center", size=(30, 2))],
        [sg.Text("Arrivederci e a presto! 😊",
                 font=("Helvetica", 14), justification="center", size=(30, 1))],
        [sg.Button("Chiudi", size=(10, 1), button_color=("white", "#007BFF"), font=("Helvetica", 12))]
    ]

