
# Printing functions


import reports


file_name = input("Please enter the file name: ")
print(reports.count_games(file_name))

year = input("Please enter the release date: ")
print(reports.decide(file_name, year))

print(str(reports.get_latest(file_name)))

genre = input("Please enter a genre: ")
print(reports.count_by_genre(file_name, genre))

title = input("Please enter the game title: ")
print(reports.get_line_number_by_title(file_name, title))
