import requests
from bs4 import BeautifulSoup
from time import localtime, strftime
import smtplib
import re


#HTML Architecture and list notes:
#scoreboard will hold a list of the scoreboards
#each scoreboard will have a list of their own with each piece of HTML content inside

url = 'http://www.cbssports.com/nba/standings/'

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

scoreboard1 = soup.find_all("tr", {"class": "row2"})


standingsInfo = {}
body = ""

for item in scoreboard1:
    try:
        x = item.findAll("td") 
        teamname = re.sub(r'\d+', '', x[0].text).strip()
        teamInfo = []
        teamInfo.append(teamname)
        teamInfo.append(x[1].text)
        teamInfo.append(x[2].text)
        teamInfo.append(x[3].text)
        teamInfo.append(x[4].text)
        teamInfo.append(x[5].text)
        teamInfo.append(x[6].text)
        teamInfo.append(x[7].text)
        teamInfo.append(x[8].text)
        teamInfo.append(x[9].text)
        teamInfo.append(x[10].text)

        
        print teamInfo[0]

        standingsInfo[teamname] = teamInfo

    
    except:

        body = "Sorry, no games tonight!!!"


print standingsInfo.values()



#Lets email myself the body
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('emad1997@gmail.com', 'emad1997')
    server.sendmail('emad1997@gmail.com', 'emad1997@gmail.com', body)
except:
    pass






 url = 'http://www.cbssports.com/nba/standings/'

    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    scoreboard1 = soup.find_all("tr", {"class": "row2"})

    scoreboard2 = soup.find_all("tr", {"class": "row1"})
    
    easternteams = OrderedDict()


    westernteams = OrderedDict()
    body = ""

    east = []

    east = ["Cleveland","Toronto","Boston","Charlotte","Milwaukee","New York","Chicago","Detroit","Indiana","Atlanta","Orlando","Washington","Miami","Brooklyn","Philadelphia"]

    west = []

    west = ["Golden St.","San Antonio","L.A. Clippers","Houston","Memphis","Oklahoma City","Utah","Portland","L.A. Lakers","Sacramento","Denver","New Orleans","Minnesota","Phoenix","Dallas"]

    for item in scoreboard1:
        try:
            x = item.findAll("td") 
            teamname = re.sub(r'\d+', '', x[0].text).strip()
            teamInfo = []
            teamInfo.append(teamname)
            teamInfo.append(x[1].text)
            teamInfo.append(x[2].text)
            teamInfo.append(x[3].text)
            teamInfo.append(x[4].text)
            teamInfo.append(x[5].text)
            teamInfo.append(x[6].text)
            teamInfo.append(x[7].text)
            teamInfo.append(x[8].text)
            teamInfo.append(x[9].text)
            teamInfo.append(x[10].text)

            if teamname in east:
                easternteams[teamname] = teamInfo
            if teamname in west:
                westernteams[teamname] = teamInfo


        
        except:

            body = "Sorry, no games tonight!!!"


    for item in scoreboard2:
        try:
            y = item.findAll("td") 
            teamname2 = re.sub(r'\d+', '', y[0].text).strip()
            teamInfo2 = []
            teamInfo2.append(teamname2)
            teamInfo2.append(y[1].text)
            teamInfo2.append(y[2].text)
            teamInfo2.append(y[3].text)
            teamInfo2.append(y[4].text)
            teamInfo2.append(y[5].text)
            teamInfo2.append(y[6].text)
            teamInfo2.append(y[7].text)
            teamInfo2.append(y[8].text)
            teamInfo2.append(y[9].text)
            teamInfo2.append(y[10].text)
            
            if teamname2 in east:
                easternteams[teamname2] = teamInfo2
            if teamname2 in west:
                westernteams[teamname2] = teamInfo2

        
        except:

            body = "Sorry, no games tonight!!!"

    #sort each conference by winning percentage

    sortedeasternteams = OrderedDict()
    sortedwesternteams = OrderedDict()

    eastpct = []

    #adding the win pct of each team to a list
    for name,info in easternteams.items():
        eastpct.append(info[3])

    #sorting the list of win percentages
    eastpct.sort(reverse=True)

    for name,info in easternteams.items():
        if eastpct[0] == info[3]:
            sortedeasternteams[info[0]] = info