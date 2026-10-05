# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)

Artist1Albums = ["Alb11", "Alb12", "Alb13"]
Artist2Albums = ["Alb21", "Alb22", "Alb23"]
Artist3Albums = ["Alb31", "Alb32", "Alb33"]
Artist4Albums = ["Alb41", "Alb42", "Alb43"]

musicDb = {
    "Artist1" : Artist1Albums,
    "Artist2" : Artist2Albums,
    "Artist3" : Artist3Albums,
    "Artist4" : Artist4Albums
}

# Pretty-print the data structure

pprint(musicDb)

# Display details of one album recorded by a specific artist

print(musicDb["Artist1"][0])
