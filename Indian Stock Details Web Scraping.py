import bs4
import requests
"""Either use Stock code or ticker symbol  for every stock and create a list. I will use Tata Consultancy Service, 
Ashok Leyland and ITC"""
stock_list = ['ASHOKLEY','TCS','ITC'] #you can use a excel file or csv instead and loop. I am keeping it simple

for stock in stock_list:
    #sample URL https://www.screener.in/company/<COMPANY-CODE>
    res = requests.get(r"https://www.screener.in/company/" + stock)#Downloading the HTML
    res.raise_for_status()#Nothing happens if the code is exceuted succefully else throws a exception
    soup = bs4.BeautifulSoup(res.text,"html.parser")#Save the HTML File as Soup Object
    elems = soup.select('section:nth-of-type(1) > ul > li:nth-of-type(1) > b') #Scraping the Market Cap From the HTML
    print("The Market Cap of " + stock + " is " + elems[0].text.strip() + " Crores") #Instead of Printing I can save it as a csv file
