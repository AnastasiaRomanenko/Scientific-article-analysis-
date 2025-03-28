import socket
import json
from search import search_article

HOST = '127.0.0.1'
PORT = 65432

def handle_client(conn):
    data = conn.recv(1024).decode() #receives data from the client
    if not data: #if no data is received, 
        return #exit the function
    request = json.loads(data) #loads the data into a JSON object
    
    keywords = request["keywords"] #extracts the keywords from the JSON object
    year_low = request["year_low"] #extracts the year_low from the JSON object
    year_high = request["year_high"] #extracts the year_high from the JSON object

    print(f"Searching for articles with keywords: {keywords} in years {year_low}-{year_high}")
    articles = search_article(keywords, year_low, year_high) #searches for articles with the given keywords and years

    response = json.dumps(articles) #converts the articles to a JSON string
    response = response.encode('utf-8') #encodes the JSON string to bytes
    response_length = len(response) #gets the length of the response

    if not response_length: #if the response is empty,
        return #exit the function
    conn.sendall(f"{response_length:<16}".encode('utf-8')) #sends the length of the response to the client

    print(f"Sending response of length {response_length}") 
    chunk_size = 4096 
    for i in range(0, response_length, chunk_size): #sends the response in chunks
        conn.sendall(response[i:i+chunk_size]) 


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server: #creates a TCP socket
        server.bind((HOST, PORT)) #binds the socket to the address and port
        server.listen() #listens for incoming connections
        print(f"Server listening on {HOST}:{PORT}")
        
        while True:
            conn, addr = server.accept() #accepts a connection
            with conn: #closes the connection when the block is exited
                print(f"Connected by {addr}")
                handle_client(conn) #handles the client connection

if __name__ == "__main__": #if the script is run directly,
    start_server() #starts the server