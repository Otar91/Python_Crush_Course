#8.36 Cities Names
def cities_countries(city,country):
    print(city.title() + ', ' + country.title())

cities_countries('santiago','chile')

#8.7 Album
def make_album(artist_name,title_song):
    song={'artist':artist_name,'song':title_song}
    return song

songg= make_album('Linkin park','In the end')
print(songg)

def make_album(artist_name,title_song,year=''):
    if year:
        song={'artist':artist_name,'song':title_song,'year':year}
        return song
    else:
        song={'artist':artist_name,'song':title_song}
        return song

songg= make_album('Linkin park','In the end',1994)
print(songg)

songg= make_album('Last Resort','Papa roach')
print(songg)

#While loop with fucntions

