import pandas as pd
import matplotlib.pyplot as plt
# import file_processor as fp

allVideoGameData = pd.read_csv("Data/Video_Games_Sales_as_at_22_Dec_2016.csv")
allVideoGameData = allVideoGameData.loc[:, ['Name', 'Platform', 'Genre', 'Publisher', 'Global_Sales', 'Critic_Score', 'User_Score', 'Rating']]

# ---- FUNCTIONS
def CreateGraphs():
    # Some code to create a graph and save it to Graphs folder.
    genres, counts = allVideoGameData['Genre'].value_counts().index.tolist(), allVideoGameData['Genre'].value_counts().values
    # GenreSplitGraph(genres, counts)

    same_title = allVideoGameData.loc[allVideoGameData['Name'] == 'Call of Duty: Modern Warfare 3']
    titles, platforms, ratings = same_title['Name'], same_title['Platform'], same_title['Critic_Score']
    same_names = []
    for (title, platform) in zip(titles, platforms):
        same_names.append('{}: {}'.format(title, platform))
    # RatingsDifferenceGraph(same_names, ratings)

def RatingsDifferenceGraph(titles, ratings):
    plt.figure(figsize=(17,4))
    plt.barh(titles, ratings)
    plt.title('Ratings on Different Platforms')
    plt.show()
    plt.cla()

def GenreSplitGraph(genres, counts):
    plt.figure(figsize=(13,6))
    plt.bar(genres, counts)
    plt.title('Genres vs. Number of Games')
    plt.show()
    plt.cla()

def asdfasdfasdfasdfasdf(data):
    print("hi")

def asdfasdf(data):
    print("hi")    

main = CreateGraphs()