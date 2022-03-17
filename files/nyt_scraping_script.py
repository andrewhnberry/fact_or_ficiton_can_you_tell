import os
import requests as r
import pandas as pd

api_key = "INSERT_API_KEY"
api_secret = "INSERT_API_SECRET"

month = [12,11,10,9,8,7,6,5,4,3,2,1]
year = [1852]


def export_nyt_headlines(year = [1951], month = [2]):
    headline_count = 0
    
    for y in year:
        for m in month:
            print('Initializing call...')
            headline_list = []
            result = r.get(f"https://api.nytimes.com/svc/archive/v1/{y}/{m}.json?api-key={api_key}").json()
            
            try: 
                headline_count += len(result['response']['docs'])


                for i in range(0, len(result['response']['docs'])):
                    headline_list.append(result['response']['docs'][i]['headline']['main'])
            except KeyError:
                print('logging...Key Error')
                continue
                
                
            
            headline_df = pd.DataFrame({'headlines' : headline_list})
            
            if os.path.isfile(f'nyt_headlines{year[0]}.csv') == True:
                headline_df.to_csv(f'nyt_headlines{year[0]}.csv', mode='a',
                                header = True)
            else: 
                print('CSV file does not exist, creating one.')
                headline_df.to_csv(f'nyt_headlines{year[0]}.csv')
                
            print(f'Scrapped {len(result["response"]["docs"])} for the year of {y} and the month of {m}')
                
    return (f'Operation Done, exported {headline_count} headlines.')
            
export_nyt_headlines(year, month)


    