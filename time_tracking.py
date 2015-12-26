import urllib, json, time

GRAPH_MINUTES = 15

class TimeTracker(object):
    def __init__(self, server_url):
        self.server_url = server_url
        self.data = {}
        self.graph_data = []
        #hardcoded the response string to this line as arthur cannot GET the dropbot outside the acfr
        self.update(response_string='{ \
                                       "clocked_in": ["james"], \
                                       "leaderboard": {"james":906.419,"arthur":381.759}, \
                                       "real_names": {"james":"James Ward","arthur":"Arthur Allshire"} \
                                     }')

    def update(self, response_string=None):
        if not response_string:
            response = urllib.urlopen(self.server_url+"/leaderboard")
            response_string = response.read()
        self.data = json.loads(response_string)
        self.graph_data.append([int(time.time()), sum(self.data["leaderboard"].values())])
        #for point in list(self.graph_data):
        #    if int(time.time()) - point[0] > (GRAPH_MINUTES*60) and int(time.time()) - point[0] > (GRAPH_MINUTES*60):
        #        self.graph_data.remove(point)

    def toggle_status(self, person):
        response = urllib.urlopen(self.server_url+"/qr/"+person)
        #self.update(response=response.read())
        self.update(response_string='{ \
                                       "clocked_in": ["james"], \
                                       "leaderboard": {"james":906.419,"arthur":381.759}, \
                                       "real_names": {"james":"James Ward","arthur":"Arthur Allshire"} \
                                     }')

    def get_leaderboard(self):
        leaderboard = self.data["leaderboard"]
        leaderboard_formatted = []
        for key,value in leaderboard.iteritems():
            person = []
            person.append(self.data["real_names"][key])
            person.append(value)
            if key in self.data["clocked_in"]:
                person.append(True)
            else:
                person.append(False)
            leaderboard_formatted.append(person)
        return leaderboard_formatted

    def get_total_time_and_history(self):
        """Function to get the cumulative time as well as the history of cumulative time over the last 15 minutes"""
        return self.graph_data, len(self.data["clocked_in"])
