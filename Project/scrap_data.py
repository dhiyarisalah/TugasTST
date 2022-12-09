import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

def scrapData():
    #write table to csv file
    f = open('namabayi.csv','w')

    # states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
    #           "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
    #           "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
    #           "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
    #           "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

    states = ["NY"]

    url = 'http://www.ssa.gov/cgi-bin/namesbystate.cgi'

    #iterate over all states and years
    for state in states:
        for year in range(1960,2022):
            post_data = {
                'state': state,
                'year': str(year)
            }

            post_encode = urllib.parse.urlencode(post_data)
            post_encode = post_encode.encode('UTF-8')

            request = urllib.request.Request(url, post_encode)
            page = urllib.request.urlopen(request).read().decode('UTF-8', 'ignore')

            soup = BeautifulSoup(page, "html.parser")
            table = soup.find("table",{"width":"72%"})

            #iterate over each row
            for row in table.findAll("tr"):
                cells = row.findAll("td")
                if len(cells) == 5:
                    rank = cells[0].find(text=False)
                    male = cells[1].find(text=True)
                    maleN = cells[2].find(text=False)
                    female = cells[3].find(text=True)
                    femaleN = cells[4].find(text=False)
                    write_to_file=str(year)+","+male+","+female+"\n"
                    f.write(write_to_file)
    f.close()
scrapData()

# def scrapDataGirl(year):
#     #write table to csv file
#     f = open('girl_name.txt','w')

#     # states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
#     #           "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
#     #           "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
#     #           "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
#     #           "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

#     states = ["NY"]

#     url = 'http://www.ssa.gov/cgi-bin/namesbystate.cgi'

#     #iterate over all states and years
#     for state in states:
#         for year in range(year,year+1):
#             post_data = {
#                 'state': state,
#                 'year': str(year)
#             }

#             post_encode = urllib.parse.urlencode(post_data)
#             post_encode = post_encode.encode('UTF-8')

#             request = urllib.request.Request(url, post_encode)
#             page = urllib.request.urlopen(request).read().decode('UTF-8', 'ignore')

#             soup = BeautifulSoup(page, "html.parser")
#             table = soup.find("table",{"width":"72%"})

#             #iterate over each row
#             for row in table.findAll("tr"):
#                 cells = row.findAll("td")
#                 if len(cells) == 5:
#                     rank = cells[0].find(text=False)
#                     male = cells[1].find(text=False)
#                     maleN = cells[2].find(text=False)
#                     female = cells[3].find(text=True)
#                     femaleN = cells[4].find(text=False)
#                     write_to_file=female+"\n"
#                     f.write(write_to_file)
#     f.close()

# scrapDataBoy(2003)
# scrapDataGirl(2003)