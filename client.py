import socket
import json
from reports import save_to_csv, save_to_excel
from charts import generate_charts

HOST = '127.0.0.1'
PORT = 65432
def receive_response(client):
    buffer_size = 4096

    response_length = client.recv(16).decode().strip() #receives the response length from the server
    if not response_length.isdigit(): #if the response length is not a digit,
        print("Invalid response length received from server.")
        return None #exit the function

    response_length = int(response_length) #converts the response length to an integer
    data = b"" #initializes an empty byte string

    while len(data) < response_length: #while the length of the data is less than the response length,
        chunk = client.recv(min(buffer_size, response_length - len(data))) #receives a chunk of data
        if not chunk: #if no data is received,
            break #exit the loop
        data += chunk #appends the chunk to the data

    try:
        return json.loads(data.decode()) #loads the data into a JSON object and returns it
    except json.JSONDecodeError as e: #if an error occurs while decoding the JSON data,
        print("Server response was not valid JSON:", e)
        return None #exit the function

def search_articles(): 
    keywords = input("Enter keywords (space-separated): ").split(' ') #asks the user to enter keywords
    year_low = input("Enter publication year low (e.g., 2024): ") #asks the user to enter the publication year low
    year_high = input("Enter publication year high (e.g., 2025): ") #asks the user to enter the publication year high

    request = {"keywords": keywords, "year_low": year_low, "year_high": year_high}

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client: #creates a TCP socket
        client.connect((HOST, PORT)) #connects to the server
        client.sendall(json.dumps(request).encode()) #sends the request to the server
       
        articles = receive_response(client) #receives the response from the server

        if not articles: #if no articles are found,
            print("No articles found.")
            return #exit the function

        print("\nRetrieved Articles:")
        for i, article in enumerate(articles, 1): #prints the articles
            print(f"{i}. ")
            print(f"   Authors: {article['authors']}")
            print(f"   Publication Year: {article['pub_year']}")
            print(f"   APA-style Citation: {article['apa-style_citation']}")
            print(f"   Abstract: {article['abstract']}")
            print(f"   DOI: {article['DOI']}")
            print(f"   Number of Citations: {article['num_citations']}\n")
            
        print("\nSaving results to files...")
        print("CSV file: articles.csv")
        save_to_csv(articles) #saves the articles to a CSV file
        print("Excel file with openpyxl: articles.xlsx")
        save_to_excel(articles) #saves the articles to an Excel file
        
        generate_charts(articles) #generates charts from the articles

if __name__ == "__main__": #if the script is run directly,
    search_articles() #starts the client