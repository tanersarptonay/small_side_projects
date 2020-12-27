import requests
from bs4 import BeautifulSoup

while True:
    user = input("Username: ")
    to_search = input("""______________________________________________
    albums
    artists
    tracks
    Which one do you want to search: """)
    date = input("""________________________________________
    Please input the time interval.
    LAST_7_DAYS
    LAST_30_DAYS
    LAST_90_DAYS
    LAST_180_DAYS
    LAST_365_DAYS
    ALL
    Time: """)

    url = "https://www.last.fm/user/" + user + "/library/" + to_search + "?date_preset=" + date
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")

    indexes = soup.find_all("td", {"class": "chartlist-index"})
    scrobbles = soup.find_all("span", {"class": "chartlist-count-bar-value"})


    if to_search == "albums":
        albums = soup.select('a[class="link-block-target"]')
        artists = soup.find_all("td", {"class": "chartlist-artist"})
        for index,album,artist,scrobble in zip(indexes,albums,artists,scrobbles):
            index = index.text.replace("\n", "").lstrip().rstrip()
            artist = artist.text.replace("\n","")
            album = album.text
            scrobble = scrobble.text.replace("\n","").lstrip().rstrip()
            if len(index)==1:
                print("{} -  {}\n     {}\n     {}\n_________________________________".format(index,album,artist,scrobble))
            else:
                print("{} - {}\n     {}\n     {}\n__________________________________".format(index, album, artist,scrobble))

    if to_search == "artists":
        artists = soup.select('a[class="link-block-target"]')
        for index,artist,scrobble in zip(indexes,artists,scrobbles):
            index = index.text.replace("\n", "").lstrip().rstrip()
            artist = artist.text.replace("\n", "")
            scrobble = scrobble.text.replace("\n", "").lstrip().rstrip()
            if len(index)==1:
                print("{} -  {}\n     {}\n_________________________________".format(index,artist,scrobble))
            else:
                print("{} - {}\n     {}\n__________________________________".format(index, artist,scrobble))


    if to_search == "tracks":
        tracks = soup.find_all("td", {"class", "chartlist-name"})
        artists = soup.select('a[class="link-block-target"]')
        for index,track,scrobble in zip(indexes,tracks,scrobbles):
            index = index.text.replace("\n", "").lstrip().rstrip()
            track = track.text.replace("\n", "")
            scrobble = scrobble.text.replace("\n", "").lstrip().rstrip()
            if len(index)==1:
                print("{} -  {}\n     {}\n_________________________________".format(index,track,scrobble))
            else:
                print("{} - {}\n     {}\n__________________________________".format(index, track,scrobble))




