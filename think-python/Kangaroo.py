class Kangaroo(object):

    def __init__(self):
        self.pouch_contents = []

    def __str__(self):
        return "In its pouch %s has: %s" % (object.__str__(self), str(self.pouch_contents))

    def put_in_pouch(self, other):
        self.pouch_contents.append(other)

kanga = Kangaroo()

roo = Kangaroo()

kanga.put_in_pouch(roo)

kanga.put_in_pouch(1)

kanga.put_in_pouch('hello world')

print kanga.pouch_contents
print kanga