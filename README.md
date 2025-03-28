# Scientific-article-analysis-

## Short description

A Python-based application that retrieves scientific articles from Google Scholar. It extracts metadata and provides analytical insights through visualizations.

## Libraries used

* socket (client-server communication)
* scholarly (Google Scholar integration)
* pandas (data processing)
* matplotlib / seaborn (data visualization)
* openpyxl (Excel export)

## Application features

* Search Google Scholar articles by specified keywords and a range of publication years.
* Collect  information (Authors, Year of Publication, APA-style Citation, Abstract, DOI Number, Number of Citations).
* Save the retrieved search results in an Excel (.xlsx) file and CSV (.csv)  file.
* Generate Charts that represent:
* The distribution of citation numbers for retrieved articles
* The distribution of articles by publication year

## Application workflow

1. Client inputs keywords and publication year range.
2. The client sends a request to the server.
3. The server scrapes data from sources Google Scholar.
4. Extracted data is sent to the user.
5. Results are saved in an Excel file and in a CS.
6. Visualizations are generated and displayed.
