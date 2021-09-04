from bs4 import BeautifulSoup
import requests
import json
import csv
import re

# scrape data from Row House Cinema website
# source = requests.get('https://rowhousecinema.com/').text
# soup = BeautifulSoup(source, 'lxml')

# scrap from Hollywood Theater website
source2 = requests.get('https://www.hollywoodtheaterpgh.org/').text
soup2 = BeautifulSoup(source2, 'lxml')

# scrape data from local copy of Row House Cinema website
with open('Row House Cinema.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

film_data = open('film-data.csv', 'w', newline='')
    
csv_writer = csv.writer(film_data)
csv_writer.writerow(['title', 'showtime', 'date', 'location', 'buy_ticket_link', 'summary'])

for showing in soup.find_all('div', class_='show-details'):
    title = showing.h2.text
    # print(title)
    info = showing.find('div', class_='show-description')
    summary = info.find('p', class_="").text
    # print(summary)
    # showtime = showing.find(class_='showtimes-container').text
    showtime = showing.find(class_='showtime').text
    # print(showtime)
    date = showing.find('div', class_='selected-date').text
    date2 = re.sub('.*,  ', "", date)
    editted_date = re.sub('\n', "", date2)
    # print(editted_date)
    location = "Row House Cinema"
    # print(location)
    buy_ticket = showing.find(class_='showtime')
        # attrs={'href': re.compile("^https://")})
    buy_ticket_link = buy_ticket.get('href')
    # print(buy_ticket_link)

    csv_writer.writerow([title, showtime, editted_date, location, buy_ticket_link, summary])

for showing in soup2.find_all(class_="showtimes-details"):
    title = showing.find('h1', class_='name').text
    time = showing.find('span', class_="number").text
    ampm = showing.find('span', class_="ampm").text
    showtime = time + " " + ampm
    raw_date = showing.find(class_='location_date')
    new_date = showing.parent.attrs['id']
    date = re.sub('2021-09-', 'Sep ', new_date)
    # date = raw_date.attrs['id']
    location = "Hollwood Theater"
    buy_ticket = showing.find(class_='showtime')
    buy_ticket_link = buy_ticket.get('href')
    summary = showing.find(class_='synopsis').text

    csv_writer.writerow([title, showtime, date, location, buy_ticket_link, summary])

film_data.close()

with open("film-data.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    data = {"films": []}
    for row in reader:
        data["films"].append({"title": row[0], "showtime": row[1], "date": row[2], "location": row[3], "buy_ticket_link": row[4], "summary": row[5]})

with open("../filmscrapenative/film-data.json", "w") as f:
    json.dump(data, f, indent=4)