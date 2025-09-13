# Esempio 4: Input utente (TextField)
import flet as ft

def main(page: ft.Page):
    page.title = "Text Input"
    
    # Step 1: Creare un campo di testo per l'input
    input_field = ft.TextField(
        label="Enter your name", # Suggerimento per l'utente
        hint_text="John Doe", # Testo di esempio
        width=300, # Larghezza del campo
        border_radius=10 # Angoli arrotondati
    )
    
    # Step 2: Creare un controllo testo per visualizzare l'output
    output_text = ft.Text("")
    
    # Step 3: Definire la funzione di gestione eventi del pulsante
    def greet_user(e):
        if input_field.value: # Controlla se il campo non è vuoto
            output_text.value = f"Hello, {input_field.value}!"
        else:
            output_text.value = "Please enter your name."
        page.update() # Aggiorna la pagina
        
    # Step 4: Creare il pulsante
    greet_button = ft.ElevatedButton("Say Hello", on_click=greet_user)
    
    # Step 5: Aggiungere gli elementi alla pagina
    page.add(
        input_field,
        greet_button,
        output_text
    )
    page.update()
    
ft.app(target=main)

'''
# Spiegazione passo-passo:
input_field = ft.TextField(...) # Crea un campo di testo.
label # Testo visualizzato sopra il campo di input.
hint_text # Testo di esempio all'interno del campo che scompare durante la digitazione.
width, border_radius # Proprietà di stile.
output_text = ft.Text("") # Crea un controllo testo vuoto che verrà aggiornato.
def greet_user(e): # Gestore eventi per il pulsante.
if input_field.value: # Ottiene il valore corrente dal campo di testo tramite la sua proprietà .value.
output_text.value = ... # Aggiorna il testo in output_text.
page.update() # Aggiorna l'interfaccia utente.
'''