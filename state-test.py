import time, calendar

class Person(object):
    def __init__(self, name, qr_text):
        self.name = name
        self.qr_text = qr_text
        self._state = False #True = inside (clocking up time), False = outside (not clocking up time)
        self._logs = []

    def match_qr(self, qr_text):
        """ Method that you can call on this object to see if it's qr code string matches a specific one. If it does, returns True"""
        if self.qr_text == qr_text:
            self.log()
            return [True, self.name]
        return [False, self.name]

    def log(self):
        """ Called if the qr string scanned matches this person's one. If it does, then the log() method is called to log it"""
        if self._state == False:
            self._logs.append(["IN", calendar.timegm(time.gmtime())])
        else:
            self._logs.append(["OUT", calendar.timegm(time.gmtime())])
        self._state = not self._state

arthur = Person("Arthur Allshire", "shots fired")

print arthur.match_qr("example")
print arthur._logs

print arthur.match_qr("shots fired")
print arthur._logs

print arthur.match_qr("shots fired")
print arthur._logs
