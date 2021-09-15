from bs4 import BeautifulSoup
import requests
import re
import mysql.connector
import datetime

# create connection to MySQL DB
db = mysql.connector.connect(
    host=<host>,
    user=<user>,
    passwd=<password>,
    database=<database>,
    )

mycursor = db.cursor()

# drop previous MySQL table
mycursor.execute("DROP TABLE FilmShowings")

# create MySQL table
mycursor.execute("CREATE TABLE FilmShowings (title VARCHAR(50), showtime VARCHAR(20), date VARCHAR(20), location VARCHAR(25), buy_ticket_link VARCHAR(100), summary VARCHAR(500))")

# request data from Row House Cinema website
source = requests.get('https://rowhousecinema.com/').text
soup = BeautifulSoup(source, 'lxml')

# request from Hollywood Theater website
source2 = requests.get('https://www.hollywoodtheaterpgh.org/').text
soup2 = BeautifulSoup(source2, 'lxml')

# create datetime object for current day
x = datetime.datetime.now()

# scrape data from Row House Cinema website
for showing in soup.find_all('div', class_='show-details'):
    title = showing.h2.a.text
    info = showing.find('div', class_='show-description')
    summary = info.find('p', class_="").text
    showtime = showing.find(class_='showtime').text
    editted_showtime = re.sub('\n', '', showtime)
    more_editted_showtime = re.sub('\t', '', editted_showtime)
    date = x.strftime("%B") + " " + x.strftime("%d")
    location = "Row House Cinema"
    buy_ticket = showing.find(class_='showtime')
    buy_ticket_link = buy_ticket.get('href')

    # insert data from Row House into database
    mycursor.execute("INSERT INTO FilmShowings (title, showtime, date, location, buy_ticket_link, summary) VALUES (%s,%s,%s,%s,%s,%s)", (title, more_editted_showtime, date, location, buy_ticket_link, summary))
    db.commit()

# scrape from Hollywood Theater website
for showing in soup2.find_all(class_="showtimes-details"):
    title = showing.find('h1', class_='name').text
    time = showing.find('span', class_="number").text
    ampm = showing.find('span', class_="ampm").text
    showtime = time + " " + ampm
    raw_date = showing.find(class_='location_date')
    new_date = showing.parent.attrs['id']
    date = re.sub('2021-09-', 'Sep ', new_date)
    location = "Hollwood Theater"
    buy_ticket = showing.find(class_='showtime')
    buy_ticket_link = buy_ticket.get('href')
    summary = showing.find(class_='synopsis').text

    # insert data from Hollywood Theater into database
    mycursor.execute("INSERT INTO FilmShowings (title, showtime, date, location, buy_ticket_link, summary) VALUES (%s,%s,%s,%s,%s,%s)", (title, showtime, date, location, buy_ticket_link, summary))
    db.commit()
