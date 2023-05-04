import pandas as pd
import matplotlib.pyplot as plt
import file_processor as fp

GraphVideoGameData = fp.allVideoGameData.loc[:, ['Name', 'Platform', 'Genre', 'Publisher', 'Global_Sales', 'Critic_Score', 'User_Score', 'Rating']]

# ---- FUNCTIONS
def CreateGraphs():
    # Some code to create a graph and save it to Graphs folder.
    consoles, genres, consoleCounts, genreCounts = GraphVideoGameData['Platform'].value_counts().index.tolist(), GraphVideoGameData['Genre'].value_counts().index.tolist(), GraphVideoGameData['Platform'].value_counts().values, GraphVideoGameData['Genre'].value_counts().values

    same_title = GraphVideoGameData.loc[GraphVideoGameData['Name'] == 'Call of Duty: Modern Warfare 3']
    titles, platforms, ratings = same_title['Name'], same_title['Platform'], same_title['Critic_Score']
    same_names = []
    for (title, platform) in zip(titles, platforms):
        same_names.append('{}: {}'.format(title, platform))
    
    # graph calling
    RatingsDifferenceGraph(same_names, ratings)
    GenreSplitGraph(genres, genreCounts)
    PlatformSplitGraph(consoles, consoleCounts)

# Explains why we have different dataframes for each platform
def RatingsDifferenceGraph(titles, ratings):
    plt.figure(figsize=(17,4))
    plt.barh(titles, ratings)
    plt.title('Ratings on Different Platforms')
    plt.savefig('Graphs/RatingsDifferenceGraph.png', dpi = 300, bbox_inches = 'tight')
    #plt.show()
    #plt.cla()

# explains that most common genre is recommended more frequently
def GenreSplitGraph(genres, counts):
    plt.figure(figsize=(13,6))
    plt.bar(genres, counts)
    plt.title('Genres vs. Number of Games')
    plt.savefig('Graphs/GenreSplitGraph.png', dpi = 300, bbox_inches = 'tight')
    # plt.show()
    # plt.cla()

# explains why we chose the platforms we did, lower game options for our chosen platforms so its a newer console and less information is posted on it.
def PlatformSplitGraph(platforms, counts):
    plt.figure(figsize=(25,6))
    plt.bar(platforms, counts)
    plt.title('Platforms vs. Number of Games')
    plt.savefig('Graphs/PlatformSplitGraph.png', dpi = 300, bbox_inches = 'tight')   

main = CreateGraphs()