import rdflib, csv

g = rdflib.Graph()

g.parse("issue23_test.ttl", format="n3")

g.serialize(destination='test.ttl', format='turtle')
