# Webscraping_animelist
This project is a tool for collecting anime data the Myanimelist website, built with Python using libraries like BeautifulSoup and Requests. This tool extracts and aggregates data from websites such as MyAnimeList to create a database for analysis, collection, or anime recommendations.

# Sample Result
<img width="701" alt="minhhoa" src="https://github.com/user-attachments/assets/9e0056a7-633d-43c2-99cf-6bff3abbbab2">


# Features
* Anime Data Extraction: Collects information such as anime titles, genres, ratings, summaries, episode counts, and release dates.
* Support for Multiple Websites: Compatible with various popular anime websites, ensuring a diverse and rich database.
* Customizable Data Collection: Allows users to specify the type of data to collect and from which website.
* Data Storage: Stores extracted data in structured formats like CSV or JSON for easy access and further analysis.
* Error Handling: Implements robust error handling mechanisms to manage issues such as website downtime, structural changes, and connection errors.

# Installation
To use this tool, you need to have Python installed on your computer. Clone the repository and install the required libraries:

```ruby
bash
Copy code
git clone https://github.com/tennguoidung/webscraping_animelist.git
cd webscraping_animelist
pip install -r requirements.txt
```

NOTE: The requirements.txt file includes the following libraries:
* beautifulsoup4 (also known as bs4): Used for parsing and handling HTML syntax.
* requests: Used to send HTTP requests to websites.
* openpyxl: Supports working with Excel (.xlsx) files, facilitating data storage in spreadsheet format.

# Usage
Run the script with the desired options:

```ruby
bash
Copy code
python main.py --site="trang_web_anime" --output="anime_list.csv"
Các tùy chọn:
```

Options:
* site: Specify the website to collect data from.
* output: Define the name and format of the output file (CSV or JSON).





