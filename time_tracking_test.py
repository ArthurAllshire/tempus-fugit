import time_tracking

tt=time_tracking.TimeTracker("http://loki.acfr.usyd.edu.au:4774/dropbot/tempus-fugit")
print "Leaderboard before toggle: " + str(tt.get_leaderboard())
tt.toggle_status("arthur")
tt.toggle_status("james")
print "Leaderboard after toggle: " + str(tt.get_leaderboard())
time.sleep(10)
tt.toggle_status("arthur")
print "Leaderboard after second toggle: " + str(tt.get_leaderboard())
print "Last 15 mins: " + str(tt.graph_data)
