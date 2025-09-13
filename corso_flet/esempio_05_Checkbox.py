# Esempio 5: Checkbox e gestione dello stato
import flet as ft

def main(page: ft.Page):
    page.title = "Checkbox Example"
    
    # Step 1: Creare un controllo testo che cambierà
    status_text = ft.Text("Checkbox is unchecked", size=20)
    
    # Step 2: Definire la funzione di gestione eventi per il cambiamento di stato del checkbox
    def on_checkbox_change(e):
        if e.control.value: # e.control si riferisce al controllo che ha attivato l'evento (Checkbox)
            status_text.value = "Checkbox is checked!"
        else:
            status_text.value = "Checkbox is unchecked"
        page.update() # Aggiorna la pagina
        
    # Step 3: Creare il checkbox
    my_checkbox = ft.Checkbox(
        label="Check me",
        value=False, # Stato iniziale (deselezionato)
        on_change=on_checkbox_change # Associa il gestore
    )
    
    # Step 4: Aggiungere gli elementi alla pagina
    page.add(
        my_checkbox,
        status_text
    )
    page.update()
    
ft.app(target=main)

'''
# Spiegazione passo-passo:
status_text = ft.Text(...) # Testo per visualizzare lo stato del checkbox.
def on_checkbox_change(e): # Gestore eventi per l'evento on_change del checkbox.
e.control.value # A differenza di un pulsante, per un Checkbox, il nuovo stato (selezionato/deselezionato) viene passato in e.control.value.
                # Se True, il checkbox è selezionato; se False, è deselezionato.
my_checkbox = ft.Checkbox(...) # Crea il checkbox.
label # Testo accanto al checkbox.
value # Stato iniziale del checkbox (True o False).
on_change # Associa il gestore all'evento di cambio di stato.
page.update() # Aggiorna l'interfaccia utente.
'''