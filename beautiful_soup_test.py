# Import required libraries
import requests  # To make HTTP requests
from bs4 import BeautifulSoup  # For parsing HTML
import logging  # For structured logging

# Step 1: Set up logging for better debugging
# The logging module helps track issues with detailed timestamps and levels
logging.basicConfig(
    level=logging.INFO,  # Log messages at the INFO level or higher
    format='%(asctime)s - %(levelname)s - %(message)s'  # Format: timestamp - log level - message
)

# Step 2: Define a reusable function to fetch webpage content
def scrape_webpage(url):
    """
    Fetches the HTML content of a given webpage URL.

    Args:
        url (str): The URL of the webpage to scrape.

    Returns:
        str: The raw HTML content if the request is successful, otherwise None.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    try:
        # Send a GET request to the URL with custom headers
        response = requests.get(url, headers=headers)

        # Check if the request was successful (HTTP status code 200)
        if response.status_code == 200:
            logging.info(f"Successfully fetched the webpage: {url}")
            return response.text  # Return the HTML content
        else:
            logging.warning(f"Failed to fetch the webpage. Status code: {response.status_code}")
            return None
    except Exception as e:
        # Catch any exceptions (e.g., network errors) and log them
        logging.error(f"Error during request: {e}")
        return None

# Step 3: Function to extract links and buttons
def extract_links_and_buttons(html_content):
    """
    Extracts all links (<a> tags) and buttons (<button> or button-like elements) from the HTML content.

    Args:
        html_content (str): The raw HTML content of a webpage.

    Returns:
        dict: A dictionary with keys 'links' and 'buttons' containing extracted elements.
    """
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'lxml')

    # Extract all unique links (<a> tags with href attribute)
    links = []
    for link in soup.find_all('a', href=True):  # 'href=True' ensures only valid links are captured
        text = link.get_text(strip=True)  # Extract the text within the <a> tag
        href = link['href']  # Extract the hyperlink reference (URL)
        links.append({'text': text, 'url': href})  # Store text and URL as a dictionary

    # Extract all buttons (<button> tags or button-like elements)
    buttons = []
    for button in soup.find_all(['button']):  # Find all <button> tags
        text = button.get_text(strip=True)  # Extract the button's text
        buttons.append({'text': text})  # Store button text as a dictionary
    
    # Find button-like elements (e.g., <div> with role="button")
    for button_like in soup.find_all(attrs={"role": "button"}):
        text = button_like.get_text(strip=True)
        buttons.append({'text': text})

    # Return extracted links and buttons
    return {'links': links, 'buttons': buttons}

# Step 4: Specify the URL to scrape
url = "https://medium.com/@joerosborne/intro-to-web-scraping-build-your-first-scraper-in-5-minutes-1c36b5c4b110"

# Step 5: Fetch the webpage content using the reusable function
webpage_content = scrape_webpage(url)

# Step 6: Process the HTML content and extract links/buttons if it's not empty
if webpage_content:
    try:
        # Extract links and buttons from the webpage content
        extracted_data = extract_links_and_buttons(webpage_content)

        # Print extracted links
        print("\nExtracted Links:")
        for link in extracted_data['links']:
            print(f"Text: {link['text']} | URL: {link['url']}")

        # Print extracted buttons
        print("\nExtracted Buttons:")
        for button in extracted_data['buttons']:
            print(f"Text: {button['text']}")

    except Exception as e:
        # Log and print any exceptions encountered during parsing
        logging.error(f"Error during extraction: {e}")
else:
    logging.warning("No webpage content to process.")