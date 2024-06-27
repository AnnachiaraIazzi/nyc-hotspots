import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("NYC-Hotspots", color="blue", size=24)
        self._page.controls.append(self._title)

        self._ddProvid = ft.Dropdown(label="Provider (p)")
        self._btnCreaGrafo = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.hadleGrafo)
        row1 = ft.Row([ft.Container(self._ddProvid, width=200), ft.Container(self._btnCreaGrafo, width=200)],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        self._controller.fillDD()

        self._txtDistanza = ft.TextField(label="Distanza (x)")
        self._btnAnalisiGrafo = ft.ElevatedButton(text="Analisi Grafo", on_click=self._controller.hadleAnalisi)
        row2 = ft.Row([ft.Container(self._txtDistanza, width=200), ft.Container(self._btnAnalisiGrafo, width=200)],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        self._txtString = ft.TextField(label="Stringa (s)")
        self._ddTarget = ft.Dropdown(label="Target (t)")
        self._btnPercorso = ft.ElevatedButton(text="Calcola Percorso", on_click=self._controller.hadlePercorso)
        row3 = ft.Row([ft.Container(self._txtString, width=200), ft.Container(self._ddTarget, width=200), ft.Container(self._btnPercorso, width=200)],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
