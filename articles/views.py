from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.db.utils import ProgrammingError
import logging
from collections import OrderedDict



from .models import Content,Metadata,LongArticle

import requests
from bs4 import BeautifulSoup
from time import localtime, strftime
import smtplib
import re



def index(request):
    print "got to views"
 
    print "got to try block"
    latest_post_list = Content.objects.order_by('-article_date')[:5]
    carousel = Content.objects.order_by('-article_date')[:3]
    older_post_list = Content.objects.order_by('-article_date')[:10]
    
    nbapreviewlist = Content.objects.filter(tags__contains='nbapreview')
    toptenlist = Content.objects.filter(tags__contains='topten')
    teambreakdown = Content.objects.filter(tags__contains='teambreakdown')

    playerankings = Content.objects.filter(tags__contains='playerankings')
    machinelearning = Content.objects.filter(tags__contains='machinelearning')
    marqueegame = Content.objects.filter(tags__contains='marqueegame')


    

    ### SCRAPING NBA STATS

    url = 'http://www.basketball-reference.com/leagues/NBA_2017_leaders.html'

    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    usagerate = soup.find_all("div", {"id": "leaders_usg_pct"})

    usagerateleader = []

    for item in usagerate:
        x = item.findAll("tr")
        y = item.findAll("td")
        z = item.findAll("a")
        usagerateleader.append(z[0].text)
        usagerateleader.append(y[2].text)

    twopointfgs = soup.find_all("div", {"id": "leaders_fg2"})

    twopointfgleader = []

    for item in twopointfgs:
        x = item.findAll("tr")
        y = item.findAll("td")
        z = item.findAll("a")
        twopointfgleader.append(z[0].text)
        twopointfgleader.append(y[2].text)

    mpg = soup.find_all("div", {"id": "leaders_mp"})

    mpgleader = []

    for item in mpg:
        x = item.findAll("tr")
        y = item.findAll("td")
        z = item.findAll("a")
        mpgleader.append(z[0].text)
        mpgleader.append(y[2].text)



    url = 'http://www.rotoworld.com/headlines/nba/0/basketball-headlines'

    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    news = soup.find_all("div", {"class": "pb"})

    i = 0

    newsdict = OrderedDict()

    for item in news:
        if i>2:
            break
        headline = item.findAll("a")
        report = item.findAll("p")
        print headline[0].text
        print report[0].text

        newsdict[headline[0].text] = report[0].text

        i = i + 1
    

    context = {'latest_post_list': latest_post_list, 'carousel':carousel, 'older_post_list':older_post_list, 
    'usagerateleader':usagerateleader, 'twopointfgleader':twopointfgleader,'mpgleader':mpgleader, 'newsdict':newsdict,
    'nbapreviewlist': nbapreviewlist, 'toptenlist':toptenlist, 'teambreakdown':teambreakdown,
    'playerankings':playerankings, 'machinelearning':machinelearning, 'marqueegame':marqueegame}

    
    return render(request, 'articles/new/index03.html',context)


def article(request, article_name_slug):

    context_dict = {}
    latest_post_list = Content.objects.order_by('-article_date')[:5]
    older_post_list = Content.objects.order_by('-article_date')[:4:9]
    nbapreviewlist = Content.objects.filter(tags__contains='nbapreview')
    toptenlist = Content.objects.filter(tags__contains='topten')
    teambreakdown = Content.objects.filter(tags__contains='teambreakdown')



    article = Content.objects.get(slug=article_name_slug)
    context_dict = {'article': article, 'latest_post_list': latest_post_list, 'nbapreviewlist': nbapreviewlist, 'toptenlist':toptenlist, 'teambreakdown':teambreakdown}

  
    return render(request, 'articles/new/blog-post.html', context_dict)

def standings(request):

    url = 'http://www.espn.com/nba/standings'

    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    scoreboard1 = soup.find_all("tr", {"class": "standings-row"})

    easternteams = OrderedDict()


    westernteams = OrderedDict()

    
    for index,item in enumerate(scoreboard1):
        x = item.findAll("td")
        y = item.findAll("span")
        teamname = y[3].text
        #teamname = teamname[:-3]
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
        teamInfo.append(x[11].text)
        teamInfo.append(x[12].text)
        teamInfo.append(x[13].text)

        if index<=14:
            easternteams[teamname] = teamInfo
        else:
            westernteams[teamname] = teamInfo

    nbapreviewlist = Content.objects.filter(tags__contains='nbapreview')
    toptenlist = Content.objects.filter(tags__contains='topten')
    teambreakdown = Content.objects.filter(tags__contains='teambreakdown')



    context = {'easternteams': easternteams, 'westernteams': westernteams, 'nbapreviewlist': nbapreviewlist, 'toptenlist':toptenlist, 'teambreakdown':teambreakdown}

    return render(request, 'articles/new/standings.html', context)


