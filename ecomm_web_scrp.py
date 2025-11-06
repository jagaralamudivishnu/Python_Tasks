import pandas as pd
import requests
from bs4 import BeautifulSoup

try:
    response = requests.get("https://www.flipkart.com/televisions/pr?sid=ckf%2Cczl&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&otracker=categorytree&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&p%5B%5D=facets.brand%255B%255D%3DLG&otracker=nmenu_sub_TVs%20%26%20Appliances_0_LG")
    print(f"response: {response} type is {type(response)}")
    if response.status_code == 200:
        #fetch the page content
        page_content = BeautifulSoup(response.content,'html.parser')
        #print(page_content)
        '''
        Build the dataframe to include the following:
        a) Model
        b) Price
        c) Ratings
        d) Deal info
        e) discount percent
        f) Filpkart assured
        '''
        model_list = []
        price_list = []
        disc_pct = []
        rating_list = []
        # deal_descr_list = []
        # flipkart_assured_list = []
        models = page_content.find_all('div',class_="KzDlHZ")
        for i in models[0:20]:
            model_list.append(i.get_text())
        # print(f"model list: {model_list}")

        price = page_content.find_all('div',class_="Nx9bqj _4b5DiR")
        for i in price[0:20]:
            price_list.append(i.get_text())
        unformat_price = [x.replace("₹","").replace(",","") for x in price_list]
        #print(f"Rate list: {price_list} unformat: {unformat_price}")
        
        discount = page_content.find_all('div',class_='UkUFwK')
        for i in discount[0:20]:
            disc_pct.append(i.get_text())
        unformat_disc_pct = [int(x.replace("% off","")) for x in disc_pct]
        # print(f"Disc Pct list: {disc_pct}")
        
        rating = page_content.find_all('div',class_="XQDdHH")
        for i in rating[0:20]:
            rating_list.append(float(i.get_text()))
        # print(f"Rating list: {rating_list}")
                
        # flipkart_assured = page_content.find_all('img',class_="_0CSTHy")
        # print(flipkart_assured)
        # for i in flipkart_assured[0:20]:
        #     d= i['src'] 
        #     flipkart_assured_list.append(d)
        # # print(f"Rating list: {flipkart_assured_list}")
        
        # deal_descr = page_content.find_all('div',class_="yiggsN O5Fpg8")
        # for i in deal_descr[0:20]:
        #     deal_descr_list.append(i.get_text())
        # # print(f"Rating list: {deal_descr_list}")

        #create a dataframe from above lists
        # model_list = []
        # price_list = []
        # disc_pct = []
        # rating_list = []
        # deal_descr_list = []
        # flipkart_assured_list = []
        df = pd.DataFrame()
        df['Models'] = model_list
        # df['Price'] = price_list
        df['Price'] = unformat_price
        # df['disc_pct'] = disc_pct
        df['disc_pct'] = unformat_disc_pct
        df['rating'] = rating_list
        # df['deal_info'] = deal_descr_list
        # df['flipkart_assured'] = flipkart_assured_list

        df.to_csv("flipkart_tv_deals.csv")

    else:
        print(f"Request failed with status code: {response.status_code}")    

except Exception as e:
    print(f"unexpected exception occurred {e}")

