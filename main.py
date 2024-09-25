import requests
from bs4 import BeautifulSoup
import csv

# Send a request to the Stake.com website
url = "https://stake.com/casino/games/crash"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the game data from the HTML content
game_data = []
for game in soup.find_all('div', {'class': 'game'}):
    # Extract the necessary data from each game element
    crash_out_number = game.find('span', {'class': 'crash-out-number'}).text
    game_id = game.find('span', {'class': 'game-id'}).text
    game_data.append({'game_id': game_id, 'crash_out_number': crash_out_number})

# Save the game data to a CSV file
with open('game_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['game_id', 'crash_out_number'])
    writer.writerows(game_data)
