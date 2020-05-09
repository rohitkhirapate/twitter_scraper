# Twitter Image Scraper and Hashtag Generator

This python script uses <bisguzar/twitter-scraper> to scrape profile to extract Tweet Content and Media associated with it. Generate Hashtags using Google Computer Vision API and prepare AutoPost Pictures folder for <instagrambot/instabot>


## Prerequisites

Before you begin, ensure you have met the following requirements:

* Internet Connection
* Python 3.6+

```bash
Dependencies

pip3 install twitter_scraper
pip3 install google-cloud
pip3 install google-cloud-vision

```
## Using twitter_scraper

```bash
Linux and macOS:

git clone https://github.com/rohitkhirapate/twitter_scraper.git
cd twitter-scraper
python twitter_scraper.py -p <twitter_handle>
```
To create your own client-secrets.json file, create Google Cloud Console account. Follow https://console.developers.google.com

## Credits

Thanks to the following people:

* @kennethreitz (author)
* @bisguzar (maintainer)
* @purvil12c (Automatic-HashTags-Generator-for-Images)


## Contact
If you want to contact me you can reach me at [@rohitkhirapate](https://twitter.com/rohitkhirapate).
