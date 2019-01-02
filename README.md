# Webscrapper for IMDb and data visualization

# Running the spiders
### To create a scrapy project:
```
scrapy startproject imdbtopboxoffice
cd imdbtopboxoffice
scrapy genspider imdb imdb.com
```
### Start scrapping
```
scrapy crawl imdb
```
### Save the data in a json file
```
scrapy crawl imdb -o imdb.json
```
This will crawl imdb.com and save the data in a file called imdb.json.

# The structure of imdb spider
This spider can mainly scrape information about the rating and popularity of the films on the IMDb top box office page.

The extracted data of a Imdbtopboxofficesitem is in this form:
```
{
  "name": "The Grinch", 
  "url": "https://www.imdb.com/title/tt2709692/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f9f31d04-fc22-4d12-86b4-f46e25aa2f6f&pf_rd_r=2V27JT0FAH5YK8Z5PEAJ&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=boxoffice&ref_=cht_bo_10", 
  "user_rating": "6.4", 
  "num_of_user": "15802", 
  "metascore": "51", 
  "popularity": "3", 
  "budget": "75000000", 
  "length": "1h 26min"
}
```

There is also a log file that can be used for debug. Write anything that you want in the log file by importing logging:
```
import logging
```

# Data Visualization
Extract the data that are stored in MongoDB. Using jupyter notebook, pandas and matplotlib, we can analyze the data. 
![Pandas](https://github.com/zhangshyue/webscrapper-for-IMDb-and-data-visualization/blob/master/img1.png)
