# Encapsulation is usually done to hide the state and representation of an object from the outside. 
# When encapsulating classes, a good convention is to declare all variables of a class private. 
# This will restrict direct access by the code outside that class.

class Movie:
	def __init__(self, title = '', year = -1, genre = ''):
		self.__title = title
		self.__year = year
		self.__genre = genre

	def get_title(self):
		return self.__title

	def set_title(self, new_title):
		self.__title = new_title

	def get_year(self):
		return self.__year

	def set_year(self, new_year):
		self.__year = new_year

	def get_genre(self):
		return self.__genre

	def set_genre(self, new_genre):
		self.__genre = new_genre

	def print_details(self):
	    print("Title: ", self.__title)
	    print("Year: ", self.__year)
	    print("Genre: ", self.__genre)
	    print("######################")

def main():
	movie = Movie("The Avengers", 2020, "Sci-Fi")
	movie.print_details()
	movie.set_title("Thor")
	movie.print_details()
	movie._Movie__title = "Mangled Title" # This is called Name Mangling. Data restriction does not actually work in Python. 
	movie.print_details()

if __name__ == "__main__":
    main()