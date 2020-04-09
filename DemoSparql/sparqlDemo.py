from SPARQLWrapper import SPARQLWrapper, JSON
sparql = SPARQLWrapper("http://dbpedia.org/sparql")
while 1==1:
    cadena = input("Introduce tu búsqueda o escribe exit para salir:  ")
    if cadena == "exit":
        break
    sparql.setQuery("""

    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    PREFIX dbpedia0: <http://dbpedia.org/ontology/>
    SELECT DISTINCT * WHERE {
            ?s dbpedia0:abstract ?abstract.
            ?abstract bif:contains "'"""+cadena+"""'" .
            FILTER(LANGMATCHES(LANG(?abstract),"es")).
    }
    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query()
    results.print_results()
    print