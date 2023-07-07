"""
Create  function to return a movie most similar to Planet Hulk for the list in movies.text
The function must return the movie name only
rexeg needs to be installed - pip install regex
"""

import spacy  # importing spacy
import regex as re # pip install regex
nlp = spacy.load('en_core_web_md')

def movie_description(input):

    description = nlp(input)
    df = open("movies.txt").read()
    movies = re.split(':|\n',df) # splitting in multiple locations
    titles = []
    blurb = []
    best_fit = []
    best_fit_location = 0

    for i in range(0,len(movies)): # Splitting titles and blurbs
        if i % 2:
            blurb.append(movies[i])
        else:
            titles.append(movies[i])
    #print(titles)

    #print(blurb)
    for i in blurb: # comparaing upcoming movies to current
        similarity = nlp(i).similarity(description)
        best_fit.append(similarity)

    for i in range(0,len(best_fit)): # Finding index locatoin
        if best_fit[i] > best_fit[best_fit_location]:
            best_fit_location = i
    # print(best_fit_location)
    return titles[best_fit_location] # Sends only the film name as requested, the other return sends a nicer user output to view
    # return (f'We are glad you enjoyed the film. A similar movie you may enjoy is {titles[best_fit_location]}.\n{blurb[best_fit_location]}')

# I was unsure as if you wanted an input or the input from planet hulk. so the second option to recieve an input is below.

current_movie = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
# current_movie = input("Enter movie description:\n")
print(movie_description(current_movie))
