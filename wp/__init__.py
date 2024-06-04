from textual.app import App, ComposeResult
from textual.widgets import Header, Footer

class WordProcessorApp(App):
    """
    A simple word processor for Textual.
    """

    BINDINGS = [("q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        """
        Create the application
        """
        yield Header()
        yield Footer()

def main():
    app = WordProcessorApp()
    app.run()
    
