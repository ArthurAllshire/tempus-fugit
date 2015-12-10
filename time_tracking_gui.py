from kivy.app import App

from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.garden.graph import Graph, LinePlot
from kivy.clock import Clock

import time

from time_tracking import TimeTracker

BACKEND_URL = "http://loki.acfr.usyd.edu.au:4774/dropbot/tempus-fugit" # please do not leave the backslack at the end of the url, the code will break if you do that ;)

class TimeTrackingScreen(GridLayout):
    def __init__(self, **kwargs):
        super(TimeTrackingScreen, self).__init__(**kwargs)
        #self.rows = 2
        self.cols = 1
        self.tt = TimeTracker(BACKEND_URL)
        #self.qr = QRScanner()
        self.graph = TotalTimeGraph(self.tt)
        #self.leaderboard = Leaderboard()
        #self.bottom = BottomTimeTrackingScreen(self.qr, self.leaderboard)

        # add all of these widgets to the screen
        self.add_widget(self.graph)
        #self.add_widget(self.bottom)

    def update(self, dt):
        self.tt.update(dt) #this will send a request to the server and see what has changed. also update the variables that the graph etc. uess
        #self.qr.update(dt)
        self.graph.update(dt)
        #elf.leaderboard.update(dt)

class QRScanner():
    def __init__(self):
        pass

    def update(self, dt):
        pass # in this function my intention is to scan for qr codes in the image the toggle the status of the person if they havent scanned for a few seconds

class TotalTimeGraph(Graph):
    def __init__(self, timetracker, **kwargs):
        super(TotalTimeGraph, self).__init__(**kwargs)
        self.tt = timetracker

        #initalize the graph object
        self.xlabel="Time"
        self.ylabel="Cumulative Seconds Clocked Up"
        self.x_ticks_major = 1
        self.y_ticks_major = 1000
        self.x_grid_label = True
        self.y_grid_label = True
        self.PADDING = 5
        self.x_grid = True
        self.y_grid = True
        self.x_min = -15
        self.x_max = 0

        self.plot = LinePlot(color=[1, 0, 0, 1])
        self.update(0.0)

        pass

    def update(self, dt):
        history, gradient = self.tt.get_total_time_and_history()
        self.plot.points([history[:]+[[int(time.time()), (int(time.time()-history[-1][1])*gradient)]]])
        TotalTimeGraph.add_plot(self.plot)
        super(TotalTimeGraph, self)._redraw_all()

class Leaderboard():
    def __init__(self, dt):
        pass

    def update(self, dt):
        pass

class BottomTimeTrackingScreen(GridLayout):
    def __init__(self, leaderboard, qr, **kwargs):
        super(BottomTimeTrackingScreen, self).__init__(**kwargs)
        self.cols=2
        self.leaderboard = leaderboard
        self.qr = qr

        # add the leaderboard and the qr to the gridlayout
        self.add_widget(self.leaderboard)
        self.add_widget(self.qr)

class TimeTrackingApp(App):
    def build(self):
        tts = TimeTrackingScreen()
        Clock.schedule_interval(tts.update, 0.1)
        return TimeTrackingScreen()

if __name__ == "__main__":
    TimeTrackingApp().run()
