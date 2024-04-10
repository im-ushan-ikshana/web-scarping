# 📝 Web Scraping Report
## Extracting Lecturer Information

### 📌 Table of Contents
1. [Introduction](#introduction)
2. [Code Overview](#code-overview)
3. [Libraries Used](#libraries-used)
4. [Functions and Classes](#functions-and-classes)
5. [Main Functionality](#main-functionality)
6. [Data Extraction](#data-extraction)
7. [Output](#output)
8. [Conclusion](#conclusion)

### <a name="introduction"></a>1. Introduction
Web scraping has emerged as a crucial tool in extracting valuable data from websites across various domains. In this report, we delve into the process of scraping lecturer information from the university website. The main objective of this project is to automate the extraction of data such as lecturer names, designations, contact details, and specialization areas from the website's academic staff page. By leveraging web scraping techniques, we aim to streamline the collection and organization of this data, facilitating further analysis and decision-making processes.

### <a name="code-overview"></a>2. Code Overview
The code comprises a series of functions and classes written in Python, utilizing libraries such as BeautifulSoup (bs4), requests, and pandas. The primary functions include `get_page(url)`, `convert_to_soup(html)`, `init_lecturer(lecturer_obj, soup)`, `findLinkToFullProfile(soup)`, and `csv_writer(data)`. These functions collectively orchestrate the scraping process, from fetching HTML content to writing the extracted data into a CSV file.

### <a name="libraries-used"></a>3. Libraries Used
The BeautifulSoup library is instrumental in parsing HTML content, allowing us to navigate the document's structure and extract relevant information efficiently. The requests library facilitates HTTP requests, enabling us to retrieve web pages' content. Additionally, pandas is utilized for data manipulation and storage, enabling us to organize the extracted data into a structured format easily.

### <a name="functions-and-classes"></a>4. Functions and Classes
Each function and class in the code serves a distinct purpose in the scraping process. For instance, `get_page(url)` retrieves the HTML content of a given URL, while `init_lecturer(lecturer_obj, soup)` initializes a Lecturer object with information extracted from the webpage. These functions are meticulously designed to handle various scenarios and ensure robust data extraction.

#### Functions Overview
1. `get_page(url)`: This function is responsible for fetching the HTML content of a given URL. It utilizes the requests library to make an HTTP GET request to the specified URL. If the request is successful (status code 200), it returns the HTML content as a text string along with the response object. In case of errors such as connection issues or timeouts, appropriate exceptions are handled to ensure graceful error handling.
2. `convert_to_soup(html)`: Once the HTML content is retrieved, this function converts it into a BeautifulSoup object. BeautifulSoup is a Python library for parsing HTML and XML documents, providing a convenient interface for navigating the document tree and extracting data. By passing the HTML content to this function, we obtain a BeautifulSoup object that can be used to search for specific elements and extract desired information.
3. `init_lecturer(lecturer_obj, soup)`: This function initializes a Lecturer object with information extracted from the webpage. It takes a Lecturer object and a BeautifulSoup object representing the webpage as input parameters. Using the BeautifulSoup object, it searches for relevant HTML elements containing information such as lecturer name, designation, contact details, and specialization area. It then populates the attributes of the Lecturer object with the extracted data.
4. `findLinkToFullProfile(soup)`: This function searches for a link to the full profile of a lecturer within the provided webpage. It takes a BeautifulSoup object representing the webpage as input and searches for an anchor tag containing the text "View Full Profile." If such a link is found, it returns the URL to the full profile; otherwise, it returns None.
5. `csv_writer(data)`: Finally, this function writes the extracted data into a CSV file. It takes a list of lists (data) as input, where each inner list represents the data for a single lecturer. Using the pandas library, it creates a DataFrame from the data and then writes it to a CSV file named "lecturer_data.csv." This CSV file serves as the output of the scraping process, containing columns for lecturer name, designation, room, email, phone, and specialization area.

The Lecturer class defines the following attributes:
1. name: Represents the name of the lecturer.
2. designation: Indicates the designation or title of the lecturer.
3. room: Specifies the room number or location of the lecturer.
4. email: Stores the email address of the lecturer.
5. phone: Stores the phone number of the lecturer.
6. specialization_area: Indicates the area of specialization or expertise of the lecturer.

### <a name="main-functionality"></a>5. Main Functionality
The main() function orchestrates the scraping process, starting with fetching the HTML content of the academic staff page. It then iterates through each lecturer's section, extracting their information and storing it in a list. This list is subsequently written into a CSV file using the csv_writer(data) function.
1. Fetching Webpage: The main() function begins by calling the `get_page(url)` function to fetch the HTML content of the academic staff page from the specified URL.
2. Converting to BeautifulSoup Object: Once the HTML content is obtained, it is passed to the `convert_to_soup(html)` function to create a BeautifulSoup object, enabling easy traversal and extraction of data from the webpage.
3. Iterating Through Lecturers: The function then checks if the HTTP request was successful (status code 200) and proceeds to iterate through sections of the webpage containing information about individual lecturers. For each lecturer section, it calls the `findLinkToFullProfile(soup)` function to locate the link to their full profile.
4. Extracting Data: If a link to the full profile is found, the function makes another HTTP request to fetch the detailed profile page. It then initializes a Lecturer object using the `init_lecturer(lecturer, soup)` function, extracting relevant information such as name, designation, contact details, and specialization area.
5. Writing to CSV: The extracted data for each lecturer is appended to a list, and once all lecturers' information has been collected, the function calls `csv_writer(data)` to write the data to a CSV file.

### <a name="data-extraction"></a>6. Data Extraction
The process of data extraction involves parsing the HTML content using BeautifulSoup and identifying relevant elements such as lecturer names, designations, contact details, and specialization areas. Regular expressions are employed to extract specific patterns, such as email addresses and phone numbers, from the text. The extracted data is then structured and stored for further analysis.
1. Parsing HTML Content: The BeautifulSoup library is used to parse the HTML content of web pages, enabling the code to navigate and extract data from the webpage's structure.
2. Identifying Relevant Elements: Using BeautifulSoup's functions, the code identifies specific HTML elements containing the desired information, such as `<h3>` tags for names or `<a>` tags for email addresses.
3. Extracting Information: Once the relevant elements are located, their content is extracted to retrieve the desired information. This typically involves accessing the text within the elements or retrieving attribute values like href for links.
4. Assigning to Object Attributes: The extracted information is assigned to attributes of Lecturer objects. Each attribute represents a specific piece of lecturer information, such as name, email, or designation.
5. Handling Missing Data: Robust error handling is implemented to address cases where certain information may be missing or unavailable. If data cannot be extracted, the corresponding attribute is set to None to indicate missing information.
6. Regular Expressions: Regular expressions are used to extract patterns from text content, such as email addresses or phone numbers, allowing for more precise data extraction.
7. Iteration for Multiple Data Instances: In cases where multiple instances of the same type of information exist (e.g., multiple lecturer names), iteration is used to process each instance sequentially.

### <a name="output"></a>7. Output
The code utilizes the pandas library to output the extracted lecturer information into a CSV file. It converts the data into a DataFrame structure and writes it to a file named "lecturer_data.csv". This CSV file provides a structured representation of the lecturer data, enabling easy access, analysis, and sharing of information.

### <a name="conclusion"></a>8. Conclusion
In conclusion, the web scraping code successfully achieves its objective of extracting lecturer information from the university website. Through the systematic application of BeautifulSoup, requests, and pandas libraries, we are able to automate the data extraction process efficiently. The resulting CSV file provides a valuable resource for academic research, administrative decision-making, and other applications.
