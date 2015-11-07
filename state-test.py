import time, calendar

class Person(object):
    def __init__(self, name, qr_text):
        self.name = name
        self.qr_text = qr_text
        self._state = False #True = inside (clocking up time), False = outside (not clocking up time)
        #   Example structure for logs: [[["IN", 1446938256], ["OUT", 1446939200]], [["IN", 1447941200]]]
        self._logs = []

    def match_qr(self, qr_text):
        """ Method that you can call on this object to see if it's qr code string matches a specific one. If it does, returns True"""
        if self.qr_text == qr_text:
            self.log()
            return [True, self.name]
        return [False, self.name]

    def log(self):
        """ Called if the qr string scanned matches this person's one. If it does, then the log() method is called to log it"""
        if self._state == True:
            if len(self._logs[-1]) == 1 and self._logs[-1][0][0] == "IN":
                    # there is an open session at the end of the logs list that needs to be closed
                    self._logs[-1].append(["OUT", calendar.timegm(time.gmtime())])
                # Here I need to figure out what to do if there is there is a session that closes with no opening,
                # as well as what if there is a session that has "OUT" at the start
        else:
            # this person is currently logged out, therefore we want to add a new session on the end of the list
            self._logs.append([["IN", calendar.timegm(time.gmtime())]])
        self._state = not self._state

arthur = Person("Arthur Allshire", "shots fired")

print arthur.match_qr("example")
print arthur._logs

print arthur.match_qr("shots fired")
print arthur._logs

print arthur.match_qr("shots fired")
print arthur._logs

print arthur.match_qr("shots fired")
print arthur._logs


print arthur.match_qr("shots fired")
print arthur._logs
