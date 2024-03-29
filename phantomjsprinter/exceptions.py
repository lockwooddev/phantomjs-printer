
class PDFCreationException(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __str__(self):
        return "%s: %s" % self.code, self.message

    def __unicode__(self):
        return u"%s: %s" % self.code, self.message