# Download all KBAI videos for offline viewing

I created this script so that I could watch the videos when I was travelling and did not have access to internet. Feel free to modify and/or distribute it in any way you'd like. I hope I was able to make someone's day! :)

1. First, obtain a Youtube API key.
  - Go to [Google API's Console](https://console.developers.google.com/apis/dashboard) and create a new project
  - Go to the [Enabled APIs Page](https://console.developers.google.com/apis/enabled) and enable the **YouTube Data API v3** API
  - Go to the [Credentials Page](https://console.developers.google.com/apis/credentials) and create an API key (restrict if you'd like)
  - See [https://developers.google.com/youtube/v3/getting-started](https://developers.google.com/youtube/v3/getting-started) for details or if you get stuck

2. `pip install virtualenv` (if you don't already have it installed)
3. `git clone https://github.com/pmalbu/OMSCS_CS7637_youtube_downloader.git cs7637_dl`
4. `cd cs7637_dl`
5. `virtualenv venv`
6. `source venv/bin/activate`
7. `pip install -r requirements.txt`
8. Copy your API key into the *API_KEY='Your-Key-Here'* section of `dl.py`
9. `python dl.py`
10. Enjoy!