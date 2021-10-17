# Down below we have fixed all
import requests
from bs4 import BeautifulSoup
import pprint # use for nice printing

# Page 1 response and Page 2 response
res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')

# Created object of both the pages
soup_object = BeautifulSoup(res.text, 'html.parser')
soup_object2 = BeautifulSoup(res2.text, 'html.parser')

links = soup_object.select('.storylink') # gives all the headline links of Page 1 
subtext = soup_object.select('.subtext')  # gives subtext of all the headlines on Page 1
links2 = soup_object2.select('.storylink') # gives all the headline links of Page 2
subtext2 = soup_object2.select('.subtext')  # gives subtext of all the headlines on Page 2

mega_links = links + links2  # combined 
mega_subtext = subtext + subtext2


# for sorting
def sort_by_score(hnlist):
    return sorted(hnlist, key = lambda d:d['score'], reverse = True) # key means by which you want to sort. Here we used lamda function because we need to sort by score which is in dictionary. In lambda function d is for dictionary element of the list, lambda is going to return d['score'] which is going to give score of every dictionary element of the list which is going to be set as key, after that all the dictionary elements of the list are going to get sorted by score. reverse is used for going from higher to small score


# Now to filter all the data in way we want we will create a function for it.
def new_hn(links, subtext):
    hn = []
    for index, item in enumerate(links):
        # enumerate gives the link (item) and its index
        title = item.getText()
        # To get the text of Links
        # above expression is same as title = links[index].getText()
        
        href = item.get('href', None) # to get the actual links, None is their beacuse if the link is broken.
        
        score = subtext[index].select('.score')
        # we got score in the list format
        # note this score is going to be a list containing only one element, and that single element is going to change till for loop ends.
        
        if len(score):
            points = int(score[0].getText().replace(' points', ''))
            # score[0] because to grab the first element of score list.
            if points > 99:
                hn.append({'title': title, 'href': href, 'score': points}) # By this we combine link text and link 
    return sort_by_score(hn)
  
pprint.pprint(new_hn(mega_links, mega_subtext))
