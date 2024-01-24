# API Citations en local et déploiement

This API scrapes quotes and their authors with scrapy from the website quotes.toscrape.com.

## Local

Save them in a dictionnary in a NoSQL database (here MongoDb) via a docker.
Make resquestes via Flask to the MongoDb to achieve researches by word or author
or to get a random quote.
Display the result with Streamlit.

### Make it works

* Clone the repository.
* Go to the second craiglist directories.
* Install the required librairies: *pip install -r requirements.txt*
* Launch the docker desktop.
* Create a docker with: *docker pull mongo:5.0*
* Instantiate the docker on port 27017: *docker run --scrapy_db -p 27017:27017 -d mongo*
* Fullfill scrapy_db with scrapy : *scrapy crawl jobs*
* Launch the Flask server: *flask --app server.py run*
* Launch the streamlit app: *streamlit run streamlit_client.py*

## Remote

This API saves them in a JSON.
Makes request via Flask to the JSON file to get a random quote.
Display the result with HTML and CSS.

### Make it works

* Clone the repository
* Go to [pythonanywhere](https://www.pythonanywhere.com/)
* Click on add a new web app.
* Click on next and choose Flask when prompted.
* Click on the Files tab.
* Click on mysite/ directory.
* Upload the file server.py from 16-scrapy -> craiglist -> craiglist 
* Create three directories: data, static and templates (don't forget the s at the end or it won't works).
* In data upload the JSON files named scraped_data.json from 16-scrapy -> test -> data.
* In static upload the quotes.css file from 16-scrapy -> test -> static.
* In templates upload vue.html from 16-scrapy -> test -> templates.
* Go the web tab and scroll down until Stactic files section.
* In the URL column enter /data/ then below /templates/ then below /static/.
* In the directory column enter /home/JoachimLombardi/mysite/data/ then below /home/JoachimLombardi/mysite/templates/ then below /home/JoachimLombardi/mysite/static/.
* Scroll up to the top and click on the green button: Reload joachimlombardi.pythonanywhere.com.
* Above click on JoachimLombardi.pythonanywhere.com.
* On the new page click on the refresh button of the navigator to load a new quote.
