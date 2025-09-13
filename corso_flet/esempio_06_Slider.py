# Esempio 6: Slider per input numerico
import flet as ft

def main(page: ft.Page):
    page.title = "Slider Example"
    
    # Step 1: Creare un controllo testo per visualizzare il valore dello slider
    slider_value_text = ft.Text("Value: 50", size=20)
    
    # Step 2: Definire la funzione di gestione eventi per il cambiamento del valore dello slider
    def on_slider_change(e):
        # e.control.value contiene il valore corrente dello slider
        slider_value_text.value = f"Value: {int(e.control.value)}"
        page.update() # Aggiorna la pagina
        
    # Step 3: Creare lo slider
    my_slider = ft.Slider(
        min=0, # Valore minimo
        max=100, # Valore massimo
        divisions=10, # Numero di divisioni (per lo "snap")
        value=50, # Valore iniziale
        label="{value}", # Visualizza il valore corrente come tooltip
        on_change=on_slider_change # Associa il gestore
    )
    
    # Step 4: Aggiungere gli elementi alla pagina
    page.add(
        slider_value_text,
        my_slider
    )
    page.update()
    
ft.app(target=main)

'''
# Spiegazione passo-passo:
slider_value_text = ft.Text(...) # Testo per visualizzare il valore selezionato.
def on_slider_change(e): # Gestore eventi per l'evento on_change dello slider.
e.control.value # contiene il valore numerico corrente dello slider. Lo convertiamo in int per la visualizzazione.
my_slider = ft.Slider(...) # Crea lo slider.
min, max # Definiscono l'intervallo di valori.
divisions # Divide l'intervallo in un numero specificato di passaggi (consente lo "snap" a questi valori).
value # Valore iniziale dello slider.
label="{value}" # Mostra un tooltip con il valore corrente quando viene trascinato.
on_change # Associa il gestore.
page.update() # Aggiorna l'interfaccia utente.
'''
