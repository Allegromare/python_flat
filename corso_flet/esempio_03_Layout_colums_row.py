# Esempio 3: Utilizzo di Column e Row per il layout
import flet as ft

def main(page: ft.Page):
    page.title = "Layout Example"
    
    # Step 1: Creare controlli
    text1 = ft.Text("Item 1")
    text2 = ft.Text("Item 2")
    button1 = ft.ElevatedButton("Button A")
    button2 = ft.ElevatedButton("Button B")
    
    # Step 2: Utilizzare Column per la disposizione verticale
    vertical_layout = ft.Column(
        [
            text1,
            text2,
            ft.Text("This is a vertical column")
        ],
        alignment=ft.MainAxisAlignment.CENTER, # Allinea al centro lungo l'asse principale (verticale)
        spacing=10 # Spaziatura tra gli elementi
    )
    
    # Step 3: Utilizzare Row per la disposizione orizzontale
    horizontal_layout = ft.Row(
        [
            button1,
            button2,
            ft.Text("This is a horizontal row")
        ],
        alignment=ft.MainAxisAlignment.SPACE_AROUND, # Distribuisce gli elementi in modo uniforme con spazio attorno ad essi
        spacing=20 # Spaziatura tra gli elementi
    )
    
    # Step 4: Aggiungere entrambi i layout alla pagina
    page.add(vertical_layout, horizontal_layout)
    page.update()

ft.app(target=main)

'''
# Spiegazione dettagliata di ogni fase:
# Importazione dei moduli necessari (import flet as ft e import os):
import flet as ft # Questa è la linea standard per importare il framework Flet. Usiamo as ft per comodità,
                  # in modo da poter scrivere ft.Page invece di flet.Page.
import os # Questo modulo è per interagire con il sistema operativo, ad esempio,
          # per verificare l'esistenza di un file (os.path.exists).
          # Non è utilizzato in questo specifico esempio di contatore, ma era necessario per l'esempio dell'immagine che abbiamo discusso in precedenza.
# Definizione della funzione principale main(page: ft.Page):
# Tutte le applicazioni Flet iniziano con una funzione principale che accetta un argomento:
# un oggetto Pagina di tipo ft.Page. Questo oggetto pagina
# rappresenta la finestra o la scheda dell'applicazione e consente di aggiungere controlli ad essa.
# Configurazione della pagina (page.title, page.vertical_alignment):
page.title = "Simple Flet Counter" # Imposta il testo che apparirà nella
                                  # barra del titolo della finestra dell'applicazione o nella scheda del browser.
page.vertical_alignment = ft.MainAxisAlignment.CENTER # Questa proprietà
                                                    # determina come il contenuto della pagina sarà allineato verticalmente.
                                                    # ft.MainAxisAlignment.CENTER centra tutto il contenuto verticalmente.
# Creazione di una variabile di stato (current_value):
current_value = ft.Text("0", size=30) # Creiamo un oggetto ft.Text.
                                      # Questo è un widget che visualizza testo. Inizialmente, mostra "0".
                                      # size=30: Imposta la dimensione del carattere del testo.
                                      # Importante: In Flet, se vuoi che un controllo cambi, devi memorizzarlo come un oggetto
                                      # (come current_value qui) e quindi aggiornare le sue proprietà (ad esempio, current_value.value).
# Creazione di una funzione di gestione eventi on_button_click(e):
# Questa funzione "ascolterà" i clic dei pulsanti. e (abbreviazione di "evento") è un
# oggetto evento che Flet passa quando viene attivato on_click.
count = int(current_value.value) # Ottiene il testo corrente da current_value
                                 # e lo converte in un intero in modo che possano essere eseguite operazioni matematiche.
if e.control.text == "+": # Usiamo e.control.text per
                          # determinare quale pulsante è stato premuto. e.control si riferisce al widget (pulsante) stesso che ha attivato l'evento.
count += 1 or count -= 1 # Incrementa o decrementa il valore del contatore.
current_value.value = str(count) # Aggiorna la proprietà value del widget di testo con il nuovo valore del contatore.
                                 # È importante convertire il numero di nuovo in una stringa, poiché ft.Text visualizza stringhe.
page.update() # Questo è un passaggio cruciale! Flet non aggiorna l'interfaccia utente automaticamente.
              # Dopo qualsiasi modifica di stato a un widget (ad esempio, current_value.value), è necessario chiamare page.update()
              # (o widget.update() se si aggiorna un widget specifico) affinché le modifiche si riflettano sullo schermo.
# Creazione dei pulsanti (ft.ElevatedButton):
minus_button = ft.ElevatedButton(text="-", on_click=on_button_click) # Crea un pulsante con il testo "-" e associa la funzione on_button_click per gestire i clic.
plus_button = ft.ElevatedButton(text="+", on_click=on_button_click) # Similmente per il pulsante "+".
ft.ElevatedButton # è un pulsante con un'ombra che si "eleva" quando viene premuto.
# Organizzazione degli elementi con ft.Row e ft.Column:
ft.Row([...], alignment=ft.MainAxisAlignment.CENTER, spacing=10)
# ft.Row è utilizzato per la disposizione orizzontale dei widget.
# Inseriamo minus_button, current_value e plus_button in questa riga.
# alignment=ft.MainAxisAlignment.CENTER: Centra gli elementi all'interno della riga orizzontalmente.
# spacing=10: Aggiunge 10 pixel di spazio tra ogni elemento nella riga.
ft.Column([...], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=30)
# ft.Column è utilizzato per la disposizione verticale dei widget.
# Aggiungiamo un titolo (ft.Text("Your Counter:")) e i nostri row_controls a questa colonna.
# horizontal_alignment=ft.CrossAxisAlignment.CENTER: Centra il contenuto all'interno della colonna orizzontalmente
# (ad esempio, i nostri row_controls saranno centrati).
# spacing=30: Aggiunge 30 pixel di spazio tra ogni elemento nella colonna.
# Row e Column sono potenti contenitori per la creazione di layout complessi.
# Aggiungere l'elemento principale alla pagina (page.add) e aggiornare l'interfaccia utente (page.update()):
page.add(column_layout) # Aggiunge il column_layout creato (che contiene tutti gli altri widget) alla pagina.
page.update() # Questa chiamata di update() è necessaria qui per visualizzare inizialmente tutti gli elementi
              # sulla pagina quando l'applicazione viene avviata per la prima volta.
# Esecuzione dell'applicazione Flet (ft.app(target=main, view=ft.WEB_BROWSER)):
ft.app(...) # Questa funzione esegue la tua applicazione Flet.
            # target=main: Specifica quale funzione è il punto di ingresso per la tua applicazione (in questo caso, la nostra funzione principale).
            # view=ft.WEB_BROWSER: Questo argomento dice a Flet di aprire l'applicazione nel tuo browser web.
            # Questo è conveniente per lo sviluppo e il test rapidi, poiché il browser può essere aggiornato automaticamente quando il codice cambia.
            # Se vuoi eseguire l'applicazione come una normale applicazione desktop,
            # rimuovi semplicemente view=ft.WEB_BROWSER, lasciando ft.app(target=main).
'''