import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._Provider = None
        self._distanzaScelta = None

    def fillDD(self):
        provider = self._model.getAllProvider()
        for p in provider:
            self._view._ddProvid.options.append(ft.dropdown.Option(text=p, data=p, on_click=self.readDDProvider))
        self._view.update_page()

    def readDDProvider(self, e):
        if e.control.data is None:
            self._Provider = None
        else:
            self._Provider = e.control.data

    def hadleGrafo(self, e):
        if self._Provider is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Attenzione, nessun Provider selezionato"))
            self._view.update_page()
            return
        self._distanzaScelta = self._view._txtDistanza.value
        if self._distanzaScelta is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Attenzione, nessun hai scritto alcuna distanza"))
            self._view.update_page()
            return
        try:
            num = float(self._distanzaScelta)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Attenzione, inserisci un valore corretto per la distanza"))
            self._view.update_page()
            return

        self._model.buildGraph(self._Provider, num)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Il grafo è stato correttamente costruito"))
        e, n = self._model.getNumeri()
        self._view.txt_result.controls.append(ft.Text(f"Il grafo è costituito da {n} location e {e} connessioni tra di esse"))
        self._view.update_page()

    def hadleAnalisi(self, e):
        vicini = self._model.getVicini()
        usare = []
        for v in vicini:
            if v[1] == vicini[0][1]:
                usare.append(v)
        self._view.txt_result.controls.append(ft.Text("Vertici con più vicini"))
        for u in usare:
            self._view.txt_result.controls.append(
                ft.Text(f"{u[0].Location}, #vicini: {u[1]}"))
        self._view.update_page()


    def hadlePercorso(self, e):
        pass