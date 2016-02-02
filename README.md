# syncfusion_scrape

Scraping syncfusion for ebooks: [https://www.syncfusion.com/resources/techportal/ebooks](https://www.syncfusion.com/resources/techportal/ebooks)

[https://www.syncfusion.com](https://www.syncfusion.com) is a cool site that offers a nice quantity of ebooks to download on a variety of subjects. Unfortunately downloading each ebook can be quite a painful and repetitive task as you have to fill in a form every time.

This script allows you to download all ebooks to your machine without creating an account. Nevertheless, I recommend creating an account to thank them for the free content.


---
## Instructions

    # First clone the repository
    git clone https://github.com/RyanOM/syncfusion_scrape.git

    # Go to the directory:
    cd syncfusion_scrape

    # Create a virtual environment and activate it
    virtualenv syncfusion_scrape
    source syncfusion_scrape/bin/activate
    
    # Install the requirements
    pip install -r requirements.txt

    # Start scraping with the following command:
    python main.py
