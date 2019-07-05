# Code
The main scraper file is 'get_data.py' and its support file 'api_scrape_util.py'. 'api_scrape_util.py' will need to be edited occassionally to pick up tournaments. The rules for this can be edited in the Skip_event function. Furthermore, to run these to files make sure to create the appropriate file directories to store data.

Both of these files are modified versions of files I found from bwaggone's project (https://github.com/bwaggone/smash-stats). All credit goes to them for creating the scrapper files and logic.

The Ultimate Elo file was created by me and is pretty straightforward. However, make sure to manually adjust the tournament data before using this. All csvs should be sorted (with GFs last) by round_division (largest to smallest or Z-A) and Round (Z-A, make sure GF reset comes after GF). Also, make sure that tournament.csv has been properly updated.
