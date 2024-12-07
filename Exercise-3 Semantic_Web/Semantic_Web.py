import rdflib
from rdflib import URIRef, Literal, RDF

# Create a graph
g = rdflib.Graph()

# Namespaces
MOVIE_NS = URIRef("http://example.org/movie/")
ACTOR_NS = URIRef("http://example.org/actor/")
GENRE_NS = URIRef("http://example.org/genre/")

# Add the movies, actors, and genres to the graph
movie_1 = URIRef(MOVIE_NS + "American_Psycho")
movie_2 = URIRef(MOVIE_NS + "The_Dark_Knight_Rises")
movie_3 = URIRef(MOVIE_NS + "Django_Unchained")

actor_1 = URIRef(ACTOR_NS + "Christian_Bale")
actor_2 = URIRef(ACTOR_NS + "Tom_Hardy")
actor_3 = URIRef(ACTOR_NS + "Jamiee_Fox")

genre_1 = URIRef(GENRE_NS + "Mystery")
genre_2 = URIRef(GENRE_NS + "Action")
genre_3 = URIRef(GENRE_NS + "Thriller")

# Add data properties and object properties

# Movie 1: American Psycho
g.add((movie_1, RDF.type, URIRef(MOVIE_NS + "Movie")))
g.add((movie_1, URIRef(MOVIE_NS + "hasTitle"), Literal("American Psycho")))
g.add((movie_1, URIRef(MOVIE_NS + "hasActor"), actor_1))
g.add((movie_1, URIRef(MOVIE_NS + "hasGenre"), genre_1))
g.add((movie_1, URIRef(MOVIE_NS + "hasGenre"), genre_3))

# Movie 2: The Dark Knight Rises
g.add((movie_2, RDF.type, URIRef(MOVIE_NS + "Movie")))
g.add((movie_2, URIRef(MOVIE_NS + "hasTitle"), Literal("The Dark Knight Rises")))
g.add((movie_2, URIRef(MOVIE_NS + "hasActor"), actor_1))
g.add((movie_2, URIRef(MOVIE_NS + "hasActor"), actor_2))
g.add((movie_2, URIRef(MOVIE_NS + "hasGenre"), genre_2))

# Movie 3: Django Unchained
g.add((movie_3, RDF.type, URIRef(MOVIE_NS + "Movie")))
g.add((movie_3, URIRef(MOVIE_NS + "hasTitle"), Literal("Django Unchained")))
g.add((movie_3, URIRef(MOVIE_NS + "hasActor"), actor_3))
g.add((movie_3, URIRef(MOVIE_NS + "hasGenre"), genre_3))
g.add((movie_3, URIRef(MOVIE_NS + "hasReleaseYear"), Literal(2012)))

# Add actors and genres data properties
g.add((actor_1, RDF.type, URIRef(ACTOR_NS + "Actor")))
g.add((actor_1, URIRef(ACTOR_NS + "hasName"), Literal("Christian Bale")))

g.add((actor_2, RDF.type, URIRef(ACTOR_NS + "Actor")))
g.add((actor_2, URIRef(ACTOR_NS + "hasName"), Literal("Tom Hardy")))

g.add((actor_3, RDF.type, URIRef(ACTOR_NS + "Actor")))
g.add((actor_3, URIRef(ACTOR_NS + "hasName"), Literal("Jamiee Fox")))

g.add((genre_1, RDF.type, URIRef(GENRE_NS + "Genre")))
g.add((genre_1, URIRef(GENRE_NS + "hasName"), Literal("Mystery")))

g.add((genre_2, RDF.type, URIRef(GENRE_NS + "Genre")))
g.add((genre_2, URIRef(GENRE_NS + "hasName"), Literal("Action")))

g.add((genre_3, RDF.type, URIRef(GENRE_NS + "Genre")))
g.add((genre_3, URIRef(GENRE_NS + "hasName"), Literal("Thriller")))

# Print the graph in Turtle format
print(g.serialize(format='turtle'))
