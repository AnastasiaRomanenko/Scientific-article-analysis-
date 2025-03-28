from scholarly import scholarly

def search_article(keywords, year_low, year_high):
    
    query = " ".join(keywords) #converts the keywords to a single string
    search_results = scholarly.search_pubs(query, year_low=year_low, year_high=year_high) #searches for articles with the given keywords and years
 
    articles = [] #initializes an empty list to store the articles
    for result in search_results: #iterates over the search results
        authors = result.get('bib', {}).get('author', ['Unknown']) #extracts the authors from the search result
        if isinstance(authors, list): #if the authors are a list of strings, 
            authors = ", ".join(authors) #converts the authors to a string
            
        apa = [authors, " (", result.get('bib', {}).get('pub_year', 'Unknown'), "). ", result.get('bib', {}).get('title', 'Unknown'), ". "] #creates an APA-style citation
        
        #creates a dictionary to store the article information
        article = { 
            "authors": authors, 
            "pub_year": result.get('bib', {}).get('pub_year'), #
            
            "apa-style_citation": "".join(apa),
            
            "abstract": result.get('bib', {}).get('abstract', 'No abstract available'), 
            "DOI": result.get('pub_url', 'No DOI'),
            "num_citations": result.get('num_citations', 0),
            
        }
        year = (article['pub_year']) #extracts the year of publication from the article
        if year.isdigit(): #if the year is a digit,
            articles.append(article) #appends the article to the list of articles
            print(f"Length of articles: {len(articles)}") 
    
    return articles