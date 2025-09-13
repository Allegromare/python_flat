# Esempio 2: Aggiungere un pulsante e gestire i clic
import flet as ft

def main(page: ft.Page):
    page.title = "Button Example"
    
    # Step 1: Creare una variabile per il contatore
    page.counter = 0
    
    # Step 2: Creare un controllo Testo per visualizzare il contatore
    counter_text = ft.Text(f"Counter: {page.counter}", size=20)
    
    # Step 3: Definire la funzione di gestione eventi per il clic del pulsante
    def on_button_click(e):
        page.counter += 1 # Incrementa il contatore
        counter_text.value = f"Counter: {page.counter}" # Aggiorna il valore del controllo testo
        page.update() # Aggiorna la pagina per visualizzare le modifiche
    
    # Step 4: Creare il pulsante e associare il gestore all'evento on_click
    my_button = ft.ElevatedButton("Click me!", on_click=on_button_click)
    
    # Step 5: Aggiungere il testo e il pulsante alla pagina
    page.add(counter_text, my_button)
    page.update()
    
ft.app(target=main)

''' 
Spiegazione passo-passo:
page.counter = 0 # Aggiungiamo una proprietà contatore all'oggetto pagina per memorizzare lo stato del contatore.
                 # Questo è un modo comodo per gestire i dati dell'applicazione.
counter_text = ft.Text(...) # Crea un controllo testo che visualizzerà il valore corrente del contatore.
def on_button_click(e): # Definisce una funzione che sarà chiamata ogni volta che il pulsante viene cliccato.
                        # Flet passa un oggetto evento (e) a questa funzione.
page.counter += 1 # Incrementa o decrementa il valore del contatore.
current_value.value = str(count) # Aggiorna la proprietà value del widget di testo con il nuovo valore del contatore.
                                 # È importante convertire il numero di nuovo in una stringa, poiché ft.Text visualizza stringhe.
page.update() # Questo è un passaggio cruciale! Flet non aggiorna l'interfaccia utente automaticamente.
              # Dopo qualsiasi modifica di stato a un widget (ad esempio, current_value.value), è necessario chiamare page.update()
              # (o widget.update() se si aggiorna un widget specifico) affinché le modifiche si riflettano sullo schermo.
minus_button = ft.ElevatedButton(...) # Crea un pulsante con il testo "-" e
                                    # associa la funzione on_button_click per gestire i clic.
plus_button = ft.ElevatedButton(...) # Similmente per il pulsante "+".
ft.ElevatedButton # È un pulsante con un'ombra che si "eleva" quando viene premuto.
# Organizzazione degli elementi con ft.Row e ft.Column:
ft.Row([...], alignment=ft.MainAxisAlignment.CENTER, spacing=10)
# ft.Row è utilizzato per la disposizione orizzontale dei widget.
# Inseriamo minus_button, current_value e plus_button in questa riga.
# alignment=ft.MainAxisAlignment.CENTER: Centra gli elementi all'interno della riga orizzontalmente.
# spacing=10: Aggiunge 10 pixel di spazio tra ogni elemento nella riga.
ft.Column([...], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=30)
# ft.Column è utilizzato per la disposizione verticale dei widget.
# Aggiungiamo un titolo (ft.Text("Your Counter:")) e la nostra row_controls a questa colonna.
# horizontal_alignment=ft.CrossAxisAlignment.CENTER: Centra il contenuto all'interno della colonna orizzontalmente
# (ad esempio, i nostri row_controls saranno centrati).
# spacing=30: Aggiunge 30 pixel di spazio tra ogni elemento nella colonna.
# Aggiungere l'elemento principale alla pagina (page.add) e aggiornare l'interfaccia utente (page.update()):
page.add(column_layout) # Aggiunge il column_layout creato (che contiene tutti gli altri widget) alla pagina.
page.update() # Questa chiamata di update() è necessaria qui per visualizzare inizialmente tutti gli elementi
              # sulla pagina quando l'applicazione viene avviata per la prima volta.
# Esecuzione dell'applicazione Flet (ft.app(target=main, view=ft.WEB_BROWSER)):
ft.app(...) # Questa funzione esegue la tua applicazione Flet.
            # target=main: Specifica quale funzione è il punto di ingresso per la tua applicazione (in questo caso, la nostra funzione principale).
            # view=ft.WEB_BROWSER: Questo argomento dice a Flet di aprire l'applicazione nel tuo browser web.
            # Questo è comodo per lo sviluppo e il test rapidi, poiché il browser può essere aggiornato automaticamente quando il codice cambia.
            # Se vuoi eseguire l'applicazione come una normale applicazione desktop,
            # rimuovi semplicemente view=ft.WEB_BROWSER, lasciando ft.app(target=main).

'''