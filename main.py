import csv
import math
    
class Netflix:
    def __init__(self, showid, title, director, cast, country, dateadded, releaseyear, rating, duration, listedin, description, thetype):
        self._showid = showid
        self._title = title
        self._director = director 
        self._cast = cast
        self._country = country
        self._dateadded = dateadded
        self._releaseyear = releaseyear
        self._rating = rating
        self._duration = duration
        self._listedin = listedin
        self._description = description
        self._type = thetype
        self._numberOfCastMembers = Netflix._calculateNumberOfCastMembers(self._cast)

    @classmethod
    def _calculateNumberOfCastMembers(cls, cast):
        if len(cast) == 0:
            return "There are no cast numbers"
        else:
            return len(cast)
    
    def __str__ (self):
        return (f'Show ID: {self._showid} Title: {self._title} Director: {self.director()}, Duration: {self.duration()} Type: {self.type()} {self.numOfCast()} ')
    def __len__ (self):
        return "Depending on the type, length is different"

    def __repr__(self):
        return (f'Netflix(Show ID: {self._showid} Title: {self._title} Director: {self.director()}, Duration: {self.duration()} Type: {self.type()} {self.numOfCast()} )')
    
    def showid (self):
        return self._showid
    def title (self):
        return self._title
    def director (self):
        return 'Depending on the type, might not have a director'
    def cast (self):
        return self._cast
    def country (self):
        return self._country
    def dateadded (self):
        return self._dateadded
    def releaseyear (self):
        return self._releaseyear
    def rating (self):
        return self._rating
    def duration (self):
        return 'Depending on the type, it vareiy in duration'
    def listedin (self):
        return self._listedin
    def description (self):
        return self._description
    def type (self):
        return 'It can be a Movie or Tv Show'
    def numOfCast(self):
        return f'Num of Cast Members:{self._numberOfCastMembers}'
    

class TVShow(Netflix):
    def __init__(self, showid, title, director, cast, country, dateadded, releaseyear, rating, duration, listedin, description, thetype):
        self._showid = showid
        self._title = title
        self._director = director 
        self._cast = cast
        self._country = country
        self._dateadded = dateadded
        self._releaseyear = releaseyear
        self._rating = rating
        self._duration = duration
        self._listedin = listedin
        self._description = description
        self._type = thetype
        self._numberOfCastMembers = Netflix._calculateNumberOfCastMembers(self._cast)

    
    def type(self):
        return 'TV Show'

    def duration(self):
        return self._duration
        
    def __str__ (self):
        return f'Show ID: {self._showid}  Title: {self._title}  Director: {self.director()},   Cast: {self._cast},   Country: {self._country},   Date Added: {self._dateadded}  Release Year: {self._releaseyear}  Rating: {self._rating}  Duration: {self.duration()}  Listed In: {self._listedin}  Description: {self._description}  Type: {self.type()} {self.numOfCast()}'
    def __repr__(self):
        return (f'TV Show(Show ID: {self._showid} Title: {self._title}  Director: {self.director()},   Cast: {self._cast},   Country: {self._country},   Date Added: {self._dateadded}  Release Year: {self._releaseyear}  Rating: {self._rating}  Duration: {self.duration()}  Listed In: {self._listedin}  Description: {self._description}  Type: {self.type()} {self.numOfCast()}')
    def director(self):
        return "TV Shows do not have a director"

    def __len__(self):
        return self._duration
    
class Movie(Netflix):
    def __init__(self, showid, title, director, cast, country, dateadded, releaseyear, rating, duration, listedin, description, thetype):
        self._showid = showid
        self._title = title
        self._director = director 
        self._cast = cast
        self._country = country
        self._dateadded = dateadded
        self._releaseyear = releaseyear
        self._rating = rating
        self._duration = Movie.calculateDuration(duration)
        self._listedin = listedin
        self._description = description
        self._type = thetype
        self._numberOfCastMembers = Netflix._calculateNumberOfCastMembers(self._cast)

    
    def type(self):
        return "Movie"

    def type(self):
        return self._type

    @classmethod
    def calculateDuration(cls,duration):
        minutes = duration%60
        hours = duration//60
        return f'{hours} hours and {minutes} minutes'

    def duration(self):
        return self._duration

    def __str__(self):
        return f'Show ID: {self._showid}  Title: {self._title}  Director: {self.director()},   Cast: {self._cast},   Country: {self._country},   Date Added: {self._dateadded}  Release Year: {self._releaseyear}  Rating: {self._rating}  Duration: {self.duration()}  Listed In: {self._listedin}  Description: {self._description}  Type: {self.type()} {self.numOfCast()}'

    def __repr__(self):
        return f'Movie(Show ID: {self._showid} Title: {self._title}  Director: {self.director()},   Cast: {self._cast},   Country: {self._country},   Date Added: {self._dateadded}  Release Year: {self._releaseyear}  Rating: {self._rating}  Duration: {self.duration()}  Listed In: {self._listedin}  Description: {self._description}  Type: {self.type()} {self.numOfCast()})'

    def director(self):
        return self._director
    
    def __len__(self):
        minutes = self._duration%60
        hours = self._duration//60
        
        return f'{hours} hours and {minutes} minutes'
        

    

tvshowList = []
movieList = []
with open ("netflix_titles_nov_2019.csv", encoding = "utf-8", errors = "replace") as fileIn:

    reader = csv.DictReader(fileIn)
    for line in reader:
        if line["type"] == "TV Show":
            tvshowList.append(TVShow(int(line["show_id"]),
                                line["title"],
                                line["director"].split(","),
                                line["cast"].split(","),
                                line["country"],
                                line["date_added"],
                                line["release_year"],
                                line["rating"],
                                line["duration"],
                                line["listed_in"].split(","),
                                line["description"],
                                line["type"]))
        else:
            duration = int(line["duration"].split(" ")[0])
            movieList.append(Movie(int(line["show_id"]),
                                line["title"],
                                line["director"].split(","),
                                line["cast"].split(","),
                                line["country"],
                                line["date_added"],
                                line["release_year"],
                                line["rating"],
                                duration,
                                line["listed_in"].split(","),
                                line["description"],
                                line["type"]))

class Rating:
    def __init__ (self, tvshowList, movieList):
        self._list = tvshowList + movieList
        self._ratingDict = Rating.makeRatingDict(self._list)

    @classmethod
    def makeRatingDict(cls, biglist):
        ratingDict = {}
        for item in biglist:
            if item.rating() not in ratingDict.keys():
                ratingDict[item.rating()] = [item]
            else:
                ratingDict[item.rating()].append(item)
        return ratingDict


    def __str__(self):
        return f'{self._ratingDict}'
    
    def searchRating(self, rating):
        return self._ratingDict[rating]
    
    
r = Rating(tvshowList,movieList)
print(r)

    

