class Painting:
    museum = "Louvre"

    def __init__(self, title, painter, year):
        self.title = title
        self.painter = painter
        self.year = year


the_title = input()
the_artist = input()
the_year = input()
my_painting = Painting(the_title, the_artist, the_year)

print('"{0}" by {1} ({2}) hangs in the {3}.'.format(my_painting.title, my_painting.painter, my_painting.year, my_painting.museum))
