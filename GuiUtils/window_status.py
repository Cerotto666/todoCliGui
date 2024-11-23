from Modules.Constants import windows_status as ws
from Modules import Funcions as f
def init_crea(window):
    window['action'].update(value=ws.BASE + ws.CREA)
    window['todo'].update(disabled=False)
    window['CREA'].update(disabled=True)
    window['RINOMINA'].update(disabled=True)
    window['MODIFICA'].update(disabled=True)
    window['VISUALIZZA'].update(disabled=True)
    window['CANCELLA'].update(text="INDIETRO")

def exit_crea(window):
    window['action'].update(value=ws.BASE)
    window['todo'].update(disabled=True, value="")
    window['CREA'].update(disabled=False)
    window['RINOMINA'].update(disabled=False)
    window['MODIFICA'].update(disabled=False)
    window['VISUALIZZA'].update(disabled=False)
    window['CANCELLA'].update(text="CANCELLA")
    file_list = f.listFile(True)
    window['todos'].update(values=file_list)

def init_rinomina(window):
    window['action'].update(value=ws.BASE + ws.RINOMINA)
    window['CREA'].update(disabled=True)
    window['RINOMINA'].update(disabled=True)
    window['MODIFICA'].update(disabled=True)
    window['VISUALIZZA'].update(disabled=True)
    window['CANCELLA'].update(text="INDIETRO")
    window['OK'].update(disabled=True)

def exit_rinomina(window):
    window['action'].update(value=ws.BASE)
    window['CREA'].update(disabled=False)
    window['RINOMINA'].update(disabled=False)
    window['MODIFICA'].update(disabled=False)
    window['VISUALIZZA'].update(disabled=False)
    window['CANCELLA'].update(text="CANCELLA")
    window['OK'].update(disabled=False)
    file_list = f.listFile(True)
    window['todos'].update(values=file_list)
