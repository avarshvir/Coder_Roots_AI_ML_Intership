"""Create a “admin.py”, a CLI program that allows the user to add, list, search, view and delete
details of movies
You need to create data in this format -
[ { "name": "Forrest Gump", "year": 1994, "duration": 142, "genres": ["Drama", "Romance"] },
{ "name": "Avengers: Endgame", "year": 2019, "duration": 181, "genres": ["Action",
"Adventure", "Drama"] }, { "name": "Back to the Future", "year": 1985, "duration": 114,
"genres": ["Adventure", "Comedy", "Sci-Fi"] } ]
The “name” key contains a string of the movie’s name, the “year” key contains an integer of
the movie’s release year, and the “duration” key contains an integer of the movie’s running
time in minutes.
The program should then print a welcome message and enter an endless loop which starts
by printing a list of options: “Choose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.” and then
prompts the user to enter their choice.
Once a choice has been entered, use an “if/elif” statement to handle each of the different
choices (detailed in the following requirements).
▪ If the user enters “a” (add), prompt them to enter a movie name, its release year, duration
in minutes, and genres. Place the details into a new dictionary with the keys shown earlier,
and append the dictionary to the data list.
▪ Use your “input_something()” function when prompting the user for the movie name and
genres, to ensure that they are re-prompted until they enter something other than
whitespace.
▪ Use your “input_int()” when prompting the user for the release year and duration, to ensure
that they are re-prompted until they enter an integer.
▪ The program must ensure that the user enters at least one genre for the movie.
▪ If the user enters “l” (list), display the name and release year of all movies in the data list
preceded by their index number plus 1 (so that the list starts from 1 rather than 0).
▪ If the data list is empty, show a “No movies saved” message instead.
▪ Use a “for” loop to iterate through the items in the data list. Remember: Each item is a
dictionary.
▪ You can use the “enumerate()” function to ensure that you have access to variables
containing the index number and dictionary of each item as you loop through them
If the user enters “s” (search), prompt them for a search term and then display the name and
release year of all movies (in the same format as when listing all movies) which contain the
search term in the movie name. Include the index number plus 1 next to each result.
▪ If the data list is empty, show a “No movies saved” message instead of prompting for a
search term.
▪ Control the spacing of your output, e.g. print “1) Forrest Gump (1994)” not “1 ) Forrest
Gump ( 1994 )”.
▪ Use your “input_something()” when prompting the user for the search term, to ensure that
they are re-prompted until they enter something other than whitespace.
▪ Ensure that the searching is not case-sensitive, e.g. “avengers” should find “Avengers:
Endgame”.

If the user enters “v” (view), prompt them for an index number and then print details of the
corresponding movie. Include all details of the movie, including the duration and genre(s).
▪ If the data list is empty, show a “No movies saved” message instead of prompting for index
number.
▪ The list of genres should be shown as a comma-separated list,
. ▪ Use your “input_int()” when prompting the user for an index number, to ensure that they
are re-prompted until they enter an integer.
▪ Remember: Index numbers shown to/entered by users start from 1, but the data list starts
from 0.
▪ Print an “Invalid index number” message if the index number entered does not exist in the
data list.
If the user enters “d” (delete), prompt them for an index number and then delete the
corresponding movie’s dictionary from the data list, then print a confirmation message.
▪ If the data list is empty, show a “No movies saved” message instead of prompting for index
number.
▪ Use your “input_int()” ) when prompting the user for an index number, to ensure that they
are re-prompted until they enter an integer.
▪ Remember: Index numbers shown to/entered by users start from 1, but the data list starts
from 0.
▪ Print an “Invalid index number” message if the index number entered does not exist in the
data list.
If the user enters “q” (quit), print “Goodbye!” and break out of the loop to end the program.
If the user enters anything else, print an “Invalid choice” message (the user will then be
reprompted for a choice on the next iteration of the loop).

Functions in “admin.py”
The requirements above mentioned 3 functions - “input_int()”, “input_something()”, and
As part of “admin.py”, you must define and use these functions.
1. The “input_int()” function takes 1 parameter named prompt – a string containing the
message to display before waiting for input. The function should repeatedly re-prompt the
user (using the prompt parameter) for input until they enter an integer that is greater than or
equal to 1. It should then return the value as an integer. ▪
2. The “input_something()” function takes 1 parameter named prompt – a string containing
the message to display before waiting for input. The function should repeatedly re-prompt
the user (using the prompt parameter) for input until they enter a value which consists of at
least 1 non-whitespace character (i.e. the input cannot be nothing or consist entirely of
spaces, tabs, etc.). It should then return the value as a string.
▪ Use the “strip()” string method on a string to remove whitespace from the start and end. If
a string consists entirely of whitespace, it will have nothing left once you strip the whitespace
away."""


data = [{ "name": "Forrest Gump",
          "year": 1994,
          "duration": 142, 
          "genres": ["Drama", "Romance"] 
        },
        { "name": "Avengers: Endgame",
          "year": 2019,
          "duration": 181, 
          "genres": ["Action","Adventure", "Drama"] 
        }, 
        { "name": "Back to the Future",
          "year": 1985, "duration": 114,
          "genres": ["Adventure", "Comedy", "Sci-Fi"] 
        }]

"""for i in data:
    print(i)"""

print("Welcome")

def options():
    #[a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.
    print("[a]dd")
    print("[l]ist")
    print("[v]iew")
    print("[d]elete")
    print("[q]uit")

def input_something(a):
    user_string = input()
    return user_string



data_2 = []

def add_movie():
    input_something()
    data.append(data_2)

def add_movie():
    name = input_something("Enter movie name: ")
    year = input_int("Enter release year: ")
    duration = input_int("Enter duration in minutes: ")
    genres = input_something("Enter genres (comma-separated): ").split(',')

    movie = {
        "name": name,
        "year": year,
        "duration": duration,
        "genres": [genre.strip() for genre in genres]
    }

    data.append(movie)
    print(f'Movie "{name}" added successfully!')




while True:
    options()
    select_options = input()

    if select_options == 'a':
        add_movie()
    break

print(data)

