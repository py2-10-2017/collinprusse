from datetime import datetime
class call(object):
    callnum = 0
    def __init__(self, name, number, reason):

        self.id = call.callnum
        self.name = name
        self.number = number
        self.time = datetime.now()
        self.reason = reason

        call.callnum += 1

    def displayCall(self):
        print "Caller ID: " + str(self.callnum)
        print "Name: " + self.name
        print "Number: " + str(self.number)
        print "Call Time: " + str(self.time)
        print "Reason: " + self.reason

class callcenter(object):
    def __init__(self):
        self.calls = []
        self.queue = self.get_queue_size()

    def add(self):
        self.calls.append(new_call)

    def remove(self, removecall):
        self.calls.remove(removecall)

    def info(self):
        for call in self.calls:
            call.display_info()

    def get_queue_size(self):
        return len(self.calls)

call1 = call("Steve", 3037925887, "Just bored")
call1.displayCall()
