import PySimpleGUI as sg
def get_layout_home():
    return [
        [sg.Text("TODO APP", font=("Helvetica", 20), justification="center", size=(20, 1))],
        [sg.Column([[sg.Text("_" * 30, justification="center")]], justification="center")],
        [sg.Column(
            [
                [sg.Button("CREA", size=(15, 2), button_color=("white", "#007BFF"), font=("Helvetica", 12))],
                [sg.Button("MODIFICA", size=(15, 2), button_color=("white", "#28A745"), font=("Helvetica", 12))],
                [sg.Button("VISUALIZZA", size=(15, 2), button_color=("white", "#FFC107"), font=("Helvetica", 12))],
                [sg.Button("CANCELLA", size=(15, 2), button_color=("white", "#DC3545"), font=("Helvetica", 12))],
                [sg.Text("")],  # Spazio vuoto
                [sg.Button("Esci", size=(15, 2), button_color=("white", "#6C757D"), font=("Helvetica", 12))]
            ],
            justification="center",  # Centro dei bottoni
            element_justification="center",  # Centro degli elementi nella colonna
        )]
    ]

def get_layout_crea():
    return [
        [sg.Text("CREA")],
        [sg.Button("HOME")]
    ]

def get_layout_modifica():
    return [
        [sg.Text("MODIFICA")],
        [sg.Button("HOME")]
    ]

def get_layout_visualizza():
    return [
        [sg.Text("VISUALIZZA")],
        [sg.Button("HOME")]
    ]

def get_layout_cancella():
    return [
        [sg.Text("CANCELLA")],
        [sg.Button("HOME")]
    ]