#Libraries to scrape youtube data
#YouTube Data API v3 in Python
# API client library
import googleapiclient.discovery
# API information
api_service_name = "youtube"
api_version = "v3"
# API key
DEVELOPER_KEY = "AIzaSyCW-UxGriBuHwtpIbJ4O9nSDcbS0eTANNU"
# API client
youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = DEVELOPER_KEY)


def Youtube_Scraper():
    #Request to retrive the data with the requested keyword
    request = youtube.search().list(part="snippet", q="Cooking",maxresults = 10)
    
    # Query execution
    return request.execute()

    #Code the part to comment on the video, only if a coomment has not been posted

#Call the Youtube Scraper function
Youtube_Scraper()