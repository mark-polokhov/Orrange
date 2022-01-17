import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
from typing import List, Dict, Any


# Exception if the page was not found at the specified URL
class PageNotFound(BaseException):
    def __init__(self):
        print("Page is not found. Please, check the URL.")


class WikiPlacesRecognition:

    # Code if any similar place is found
    STATUS_CODE_FOUND = 200

    FoundPlacesList = List[Dict[str, Any]]

    def __init__(self, api_token):
        self.api = api_token

    @staticmethod
    def from_api_token_path(token_file_path: str):
        with open(token_file_path) as api_token_file:
            api_token = api_token_file.read()
        return WikiPlacesRecognition(api_token=api_token)

    # Determining a list of places from a given list using requests to the Mapbox API
    def __call__(self, wiki_page_url) -> FoundPlacesList:

        # Collecting information from scraping
        try:
            ref_texts = self._scrap_wiki_page(wiki_page_url)
        except PageNotFound:
            raise
        queries = []

        # Creating an API request for each possible location
        for place in ref_texts:
            search = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{place}.json?access_token={self.api}"
            queries.append(search)

        # Getting an answer from the API and checking for a match
        founded_places = []
        for i in tqdm(range(len(queries))):
            answer = requests.get(queries[i])
            if answer.status_code == self.STATUS_CODE_FOUND:
                if len(answer.json()["features"]) > 0:
                    for location in answer.json()["features"]:

                        # if the location name matches the query,
                        # and the location type is not "address" or "point of interest"
                        # than it adds to the list
                        if (
                            location["text"].lower().split()
                            == ref_texts[i].lower().split("%20")
                            and "address" not in location["place_type"]
                            and "poi" not in location["place_type"]
                        ):
                            founded_places.append(
                                {
                                    "name": " ".join(ref_texts[i].capitalize().split("%20")),
                                    "longitude": location["center"][0],
                                    "latitude": location["center"][1],
                                }
                            )

        return founded_places

    # Scraping a wiki page and collecting possible places
    def _scrap_wiki_page(self, wiki_page_url) -> List[str]:

        # Getting the HTML code
        try:
            response = requests.get(wiki_page_url)
        except requests.exceptions.RequestException:
            raise PageNotFound
        if response.status_code != self.STATUS_CODE_FOUND:
            raise PageNotFound
        soup = BeautifulSoup(response.content, "html.parser")

        # Collecting only names and formatting them
        ref_texts = [ref.text for ref in soup.find_all("a") if len(ref.text) > 0]
        ref_texts = [ref.strip().replace(" ", "%20") for ref in ref_texts if ref[0].isupper()]

        # Deleting the copies
        for i in range(len(ref_texts) - 1, -1, -1):
            if ref_texts.count(ref_texts[i]) > 1:
                ref_texts.pop(i)

        return ref_texts

    def get_api_key(self) -> str:
        return self.api
