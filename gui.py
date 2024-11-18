import FreeSimpleGUI as sg
import os
import sys

# Gestione del percorso in base all'ambiente (sviluppo o eseguibile)
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS  # Percorso temporaneo nell'eseguibile
else:
    base_path = os.path.dirname(__file__)

