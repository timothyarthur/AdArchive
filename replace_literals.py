import rdflib, csv

g = rdflib.Graph()

g.parse("issue23_test.ttl", format="n3")

subs = {}

for s, p , o in g:
    if o in subs.keys():
        g.add(s, p, subs[o])
        g.remove(s, p, o)
