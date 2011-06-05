class Relay:

    def __init__(self, fingerprint, bandwidth):
        self.fingerprint = fingerprint
        self.bandwidth = bandwidth
        #username = models.CharField(max_length=255)
        #is_anonymous = models.BooleanField()

    def get_fingerprint(self):
        return self.fingerprint

class RelayDetails():
    def __init__(self):
        print "hello"
    #name = models.CharField(max_length=257) # TODO: figure out if this is a performance issue
    #bandwidth = models.CharField(max_length=257)
    #status = models.IntegerField()
