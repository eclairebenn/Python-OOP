# pylint: disable=print-statement
class Call(object):
    def __init__(self, name, phonenum, time, reason):
        self.name = name
        self.phonenum = phonenum
        self.time = time
        self.reason = reason
        #self.id =      
    def display_caller(self):
        print "The caller name is {}, the phone number is {}, the time of call is {}, the reason for the call is {}.".format(self.name, self.phonenum, self.time, self.reason)
    
caller1 = Call('Megan', 573952, '3:15 PM', 'To complain')
caller2 = Call('Lar', 346456, '2:00 AM', 'for some late night company')
caller1.display_caller()
caller2.display_caller()

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue = 0             
    
    def add_new_caller(self, incomingCall):
        self.calls.append(incomingCall)
        self.queue += 1
        print "The caller {} was added to the queue".format(incomingCall.name)
        return self

    def remove_caller(self, phonenum):
        for callers in self.calls:
            if callers.phonenum == phonenum:
                self.calls.remove(callers)
                print "Caller {} was removed from the queue".format(callers.name)
        self.queue -= 1
        return self
        
    def info(self):
        for caller in self.calls:
            print "The current caller name and number is {} and {}.".format(caller.name, caller.phonenum)
        print "The current queue length is {}.".format(self.queue) 


my_call_center = CallCenter()
my_call_center.add_new_caller(caller1).add_new_caller(caller2).remove_caller(346456).info()