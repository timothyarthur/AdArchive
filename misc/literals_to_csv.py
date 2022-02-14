import rdflib, csv

g = rdflib.Graph()

g.parse("issue23_test.ttl", format="n3")

with open('literals.csv', 'w') as csvfile:
    for s,p,o in g:
        if isinstance(o, rdflib.term.Literal):
            literal_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            literal_writer.writerow([o])
