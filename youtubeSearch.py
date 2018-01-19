from bs4 import BeautifulSoup
import urllib.request

def SearchVid(search):
    response = urllib.request.urlopen('https://www.youtube.com/results?search_query='+search)

    soup = BeautifulSoup(response, 'lxml')
    divs = soup.find_all("div", { "class" : "yt-lockup-content"})

    vids = []
    for i in divs:
        href = i.find('a', href=True)
        x = href.text,  "https://www.youtube.com"+href['href']
        #print(x)
        if not 'https://googleads.g.doubleclick.net/‌' in href['href']:
            vids.append(x)
    #print(vids)
    return vids

#print("What are you looking for?")
#SearchString = input()
#print(SearchVid(SearchString.replace(" ", "%20")))
