from warnings import warn
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, DataTable
from textual_plotext import PlotextPlot

class State:
    def __init__(self, namespace, state, x, y, z, vx, vy, vz):
        self.data = (namespace, state, x, y, z, vx, vy, vz)
    def __call__(self):
        return self.data

class Interface(App):
    BINDINGS = [('q', 'quit', 'Quit'),
                ('d', 'dark_mode', 'Toggle dark mode'),
                ('ctrl+z', 'suspend_process', 'Suspend process'),
                ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.theme = 'solarized-light'

        self.states = [('Namespace', 'State', 'x', 'y', 'z', 'vx', 'vy', 'vz'),
                       ('r1', 'PREFLT', 0, 0, 0, 0, 0, 0),
                       ('r2', 'PREFLT', 0, 0, 0, 0, 0, 0)
                      ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield DataTable()
        yield PlotextPlot()
        yield Footer()

    def action_quit(self):
        exit(0)

    def action_dark_mode(self):
        self.theme = 'tokyo-night' if self.theme == 'solarized-light' else 'solarized-light'

    def on_mount(self):
        table = self.query_one(DataTable)
        table.add_columns(*self.states[0])
        table.add_rows(self.states[1:])

        plt = self.query_one(PlotextPlot).plt
        y = plt.sin() # sinusoidal test signal
        plt.scatter(y)
        plt.title("Scatter Plot") # to apply a title

    def update(self, states: list[State]):
        self.states = states
       
