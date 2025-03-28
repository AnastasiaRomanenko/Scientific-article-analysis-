import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def generate_charts(articles):
    df = pd.DataFrame(articles) #converts the articles to a DataFrame
    
    if df.empty or "num_citations" not in df: #if the DataFrame is empty or does not contain citation data,
        print("No citation data available for visualization.")
        return #exit the function
    
    # Create a histogram of the citation numbers
    sns.histplot(df['num_citations']) #creates a histogram of the citation numbers
    plt.xlabel("Number of Citations") #sets the x-axis label
    plt.ylabel("Number of Articles") #sets the y-axis label
    plt.title("The distribution of citation numbers for retrieved articles") #sets the title of the plot
    plt.show() #displays the plot

    # Create a histogram of the publication years
    sns.histplot(df["pub_year"])
    plt.xlabel("Year of Publication")
    plt.ylabel("Number of Articles")
    plt.title("The distribution of articles by publication year")
    plt.show()
