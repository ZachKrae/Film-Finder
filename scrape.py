from bs4 import BeautifulSoup
import requests
import csv
import re

# scrape data from Row House Cinema website
# source = requests.get('https://rowhousecinema.com/').text
# soup = BeautifulSoup(source, 'lxml')

# scrape data from local copy of Row House Cinema website
with open('Row House Cinema.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

film_data = open('film-data.csv', 'w', newline='')
    
csv_writer = csv.writer(film_data)
csv_writer.writerow(['title', 'showtime', 'location', 'buy_ticket_link'])

for showing in soup.find_all('div', class_='show-details'):
    title = showing.h2.text
    print(title)
    info = showing.find('div', class_='show-description')
    summary = info.find('p', class_="").text
    print(summary)
    showtime = showing.find('div', class_='showtimes-container').text
    print(showtime)
    date = showing.find('div', class_='selected-date').text
    print(date)
    location = "Row House Cinema"
    print(location)
    buy_ticket = showing.find('div', 
        class_='showtimes-container').find('a', 
        attrs={'href': re.compile("^https://")})
    buy_ticket_link = buy_ticket.get('href')
    print(buy_ticket_link)
    print()

    csv_writer.writerow([title, showtime, location, buy_ticket_link])

film_data.close()