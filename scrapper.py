import requests
from bs4 import BeautifulSoup

def scrape_stars_data():
    # URL of the SkyServer page with star information
    url = "https://skyserver.sdss.org/dr16/en/tools/search/sql.aspx"

    # Sending a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract relevant information about stars (modify as needed)
        star_data = []

        # Example: Extracting star names
        star_name_elements = soup.select('.star-name-class')  # Adjust the class selector accordingly
        for star_name_element in star_name_elements:
            star_name = star_name_element.text.strip()
            star_data.append({'Star Name': star_name})

        # Example: Extracting other star information
        # You can add more elements and details to scrape

        return star_data

    else:
        print("Failed to retrieve data. Status Code:", response.status_code)
        return None

if __name__ == "__main__":
    stars_data = scrape_stars_data()

    if stars_data:
        # Print the scraped data (modify as needed)
        for star in stars_data:
            print(star)
