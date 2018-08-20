
# Export functions


import reports
import sys


file_name = input("Please enter the file name: ")
year = input("Please enter the release date: ")
genre = input("Please enter a genre: ")
title = input("Please enter the game title: ")

sys.stdout = open('export.txt', 'w')
print(reports.count_games(file_name))
print(reports.decide(file_name, year))
print(str(reports.get_latest(file_name)))
print(reports.count_by_genre(file_name, genre))
print(reports.get_line_number_by_title(file_name, title))
sys.stdout.close()
