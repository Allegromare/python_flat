# Esempio 1: Hello World (Testo di base)
import flet as ft

# Step 1: Definire la funzione principale per creare la pagina
def main(page: ft.Page):
    # Step 2: Impostare il titolo per la finestra/scheda dell'applicazione
    page.title = "Hello, Flet!"
    
    # Step 3: Creare un controllo Testo
    hello_text = ft.Text("Hello, world!", size=30, weight=ft.FontWeight.BOLD)
    
    # Step 4: Aggiungere il controllo Testo alla pagina
    page.add(hello_text)
    
    # Step 5: Aggiornare la pagina per visualizzare le modifiche
    page.update()

# Step 6: Eseguire l'applicazione, passando la funzione principale
ft.app(target=main)

''' 
Spiegazione passo-passo:

import flet as ft # Importa la libreria Flet e le assegna l'alias ft per comodità.

def main(page: ft.Page): Definisce la funzione principale, che è il punto di ingresso della nostra applicazione.
Flet passa automaticamente un oggetto Pagina (la pagina dell'applicazione) ad essa.

page.title = "Hello, Flet!" # Imposta il titolo della finestra dell'applicazione o della scheda del browser.
hello_text = ft.Text("Hello, world!", ...) Crea un'istanza del controllo Testo.
Gli passiamo il testo "Hello, world!" e impostiamo la sua dimensione e il suo peso.

page.add(hello_text) Aggiunge il controllo testo creato alla pagina.

page.update() Questo è un passaggio cruciale! Dice a Flet che la pagina è stata modificata
e l'interfaccia utente deve essere ridisegnata per riflettere queste modifiche.
Senza update(), non vedrai il tuo testo.

ft.app(target=main) Esegue l'applicazione Flet.
target=main specifica quale funzione è il punto di ingresso per la tua applicazione (in questo caso, la nostra funzione principale).
view=ft.WEB_BROWSER: Questo argomento dice a Flet di aprire l'applicazione nel tuo browser web.
Questo è comodo per lo sviluppo e il test rapidi, poiché il browser può essere aggiornato automaticamente quando il codice cambia.
Se vuoi eseguire l'applicazione come una normale applicazione desktop,
rimuovi semplicemente view=ft.WEB_BROWSER, lasciando ft.app(target=main).
'''