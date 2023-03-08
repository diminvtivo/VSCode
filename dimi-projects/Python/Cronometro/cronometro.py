from time import monotonic
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Static
from textual.containers import Container
from textual.reactive import reactive

    #Widget de Cronômetro
class displayTempo(Static):
    iniciar_tempo = reactive(monotonic)
    tempo = reactive(0.0)
    total = reactive(0.0)

    def on_mount(self) -> None:
        self.set_interval(1 / 60, self.update_time)
        self.update_timer = self.set_interval(1 / 60, self.update_time, pause=True)

    def update_time(self) -> None:
        self.time = self.total + (monotonic() - self.iniciar_tempo)
    
    def watch_time(self, time: float) -> None:
        minutes, seconds = divmod(time, 60)
        hours, minutes = divmod(minutes, 60)
        self.update(f"{hours: 02,.0f}:{minutes:02.0f}:{seconds:05.2f}")

    def iniciar(self) -> None:
        self.iniciar_tempo = monotonic()
        self.update_timer.resume()
    
    def parar(self) -> None:
        self.update_timer.pause
        self.total += monotonic() - self.iniciar_tempo
        self.time = self.total
    
    def reiniciar(self) -> None:
        self.total = 0
        self.time = 0
        
class Cronometro(Static):
    def compose(self) -> ComposeResult:
        yield Button("Iniciar", id="iniciar")
        yield Button("Parar", id="parar")
        yield Button("Reiniciar", id="reiniciar")
        yield displayTempo("00:00:00.00")
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        botao_id = event.button.id
        display_tempo = self.query_one(displayTempo)
        if botao_id == "iniciar":
            display_tempo.iniciar()
            self.add_class("iniciado")
        elif botao_id == "parar":
            display_tempo.parar()
            self.remove_class("iniciado")
        elif botao_id == "reiniciar":
            display_tempo.reiniciar()

class CronometroApp(App):

    CSS_PATH = "cronometro_css.css"
    BINDINGS = [("q", "quit", "Sair")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Container(Cronometro(), Cronometro(), Cronometro())

if __name__ == "__main__":
    app = CronometroApp()
    app.run