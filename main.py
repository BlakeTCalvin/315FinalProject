import warnings
import file_processor as fp
import graphs as g
import matplotlib as plt
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

warnings.filterwarnings("ignore")

def main():
    print("GRAPH CREATION START")
    print("------------------------------------")

    # ---- GRAPH CREATION
    g.CreateGraphs()

    print("GRAPH CREATION END")
    print("------------------------------------")

    print("PROGRAM START")
    print("------------------------------------")
    #file_processor.numberOfUniquePlatforms(file_processor.allVideoGameData)
    #fp.PCData fp.XOneData fp.PS4Data fp.WiiUData fp.DSData fp.N64Data

    print("CREATING MATRICES")
    print("------------------------------------")

    # saving a new column in the dataframe to give our matrices values to run off of for recomendations.
    fp.PCData['Recommended'] = fp.PCData.apply(lambda row: str(list(row[['Genre', 'Publisher', 'Global_Sales', 'Critic_Score', 'User_Score', 'Rating']])), axis = 1)
    fp.XOneData['Recommended'] = fp.XOneData.apply(lambda row: str(list(row[['Genre', 'Publisher', 'Global_Sales', 'Critic_Score', 'User_Score', 'Rating']])), axis = 1)
    fp.PS4Data['Recommended'] = fp.PS4Data.apply(lambda row: str(list(row[['Genre', 'Publisher', 'Global_Sales', 'Critic_Score', 'User_Score', 'Rating']])), axis = 1)
    fp.WiiUData['Recommended'] = fp.WiiUData.apply(lambda row: str(list(row[['Genre', 'Publisher', 'Global_Sales', 'Critic_Score', 'User_Score', 'Rating']])), axis = 1)
    fp.DSData['Recommended'] = fp.DSData.apply(lambda row: str(list(row[['Genre', 'Publisher', 'Global_Sales', 'Critic_Score', 'User_Score', 'Rating']])), axis = 1)
    fp.N64Data['Recommended'] = fp.N64Data.apply(lambda row: str(list(row[['Genre', 'Publisher', 'Global_Sales', 'Critic_Score', 'User_Score', 'Rating']])), axis = 1)


    # creating the transform matrix's for each platform
    # PC
    fp.PCData['Recommended'] = fp.PCData['Recommended'].apply(ChangeFormat)
    fp.PCData['Recommended'] = fp.PCData['Recommended'] + ' ' + fp.PCData['Name'].apply(FixTitleFormat)
    PCMatrix = TfidfVectorizer().fit_transform(fp.PCData['Recommended'])
    PCcsMatrix = cosine_similarity(PCMatrix, PCMatrix)

    # Xbox One
    fp.XOneData['Recommended'] = fp.XOneData['Recommended'].apply(ChangeFormat)
    fp.XOneData['Recommended'] = fp.XOneData['Recommended'] + ' ' + fp.XOneData['Name'].apply(FixTitleFormat)
    XOneMatrix = TfidfVectorizer().fit_transform(fp.XOneData['Recommended'])
    XOnecsMatrix = cosine_similarity(XOneMatrix, XOneMatrix)

    # PS 4
    fp.PS4Data['Recommended'] = fp.PS4Data['Recommended'].apply(ChangeFormat)
    fp.PS4Data['Recommended'] = fp.PS4Data['Recommended'] + ' ' + fp.PS4Data['Name'].apply(FixTitleFormat)
    PS4Matrix = TfidfVectorizer().fit_transform(fp.PS4Data['Recommended'])
    PS4csMatrix = cosine_similarity(PS4Matrix, PS4Matrix)

    # Wii U
    fp.WiiUData['Recommended'] = fp.WiiUData['Recommended'].apply(ChangeFormat)
    fp.WiiUData['Recommended'] = fp.WiiUData['Recommended'] + ' ' + fp.WiiUData['Name'].apply(FixTitleFormat)
    WiiUMatrix = TfidfVectorizer().fit_transform(fp.WiiUData['Recommended'])
    WiiUcsMatrix = cosine_similarity(WiiUMatrix, WiiUMatrix)

    # 3DS
    fp.DSData['Recommended'] = fp.DSData['Recommended'].apply(ChangeFormat)
    fp.DSData['Recommended'] = fp.DSData['Recommended'] + ' ' + fp.DSData['Name'].apply(FixTitleFormat)
    DSMatrix = TfidfVectorizer().fit_transform(fp.DSData['Recommended'])
    DScsMatrix = cosine_similarity(DSMatrix, DSMatrix)

    # N64
    fp.N64Data['Recommended'] = fp.N64Data['Recommended'].apply(ChangeFormat)
    fp.N64Data['Recommended'] = fp.N64Data['Recommended'] + ' ' + fp.N64Data['Name'].apply(FixTitleFormat)
    N64Matrix = TfidfVectorizer().fit_transform(fp.N64Data['Recommended'])
    N64csMatrix = cosine_similarity(N64Matrix, N64Matrix)

    print("MATRICES CREATED")
    print("------------------------------------")

    print("GAME RECOMMENDATIONS START")
    print("------------------------------------")

    # ----- Creating Recommendations
    GameRecommendation('The Sims: Unleashed', PCcsMatrix, "PC")
    
    # Notice how same game gives different recommendations for different platforms
    GameRecommendation('Call of Duty: Ghosts', XOnecsMatrix, "XOne")
    GameRecommendation('Call of Duty: Ghosts', PS4csMatrix, "PS4")

    GameRecommendation('Super Mario Maker', WiiUcsMatrix, "WiiU")
    GameRecommendation('Pokemon Omega Ruby/Pokemon Alpha Sapphire', DScsMatrix, "3DS")
    GameRecommendation('Donkey Kong 64', N64csMatrix, "N64")

    print("------------------------------------")
    print("GAME RECOMMENDATIONS END")
    print("------------------------------------")

    print("PROGRAM END")
    print("------------------------------------")


# ------ FUNCTIONS
# Fixes the labeling of the name in the csv to be parseable and readable for the matrix
def FixTitleFormat(value):
    return value.replace(' ', '')

# fixes the recommended column to be parseable and readable for the matrix
def ChangeFormat(value):
    return ' '.join(value)


# -----FUNCTIONS
# Function handeling actual recommendations
def GameRecommendation(title, matrix, platform):
    # Searching the specific dataframe for the title
    if platform == "PC":
        print("----------- Top Recommendations for " + title + " on PC ------------")
        localFrame = fp.PCData
        name = fp.PCData[fp.PCData['Name'] == title].index[0]
    elif platform == "XOne":
        print("----------- Top Recommendations for " + title + " on the XboxOne ------------")
        localFrame = fp.XOneData
        name = fp.XOneData[fp.XOneData['Name'] == title].index[0]
    elif platform == "PS4":
        print("----------- Top Recommendations for " + title + " on the Playstation4 ------------")
        localFrame = fp.PS4Data
        name = fp.PS4Data[fp.PS4Data['Name'] == title].index[0]
    elif platform == "WiiU":
        print("----------- Top Recommendations for " + title + " on the WiiU ------------")
        localFrame = fp.WiiUData
        name = fp.WiiUData[fp.WiiUData['Name'] == title].index[0]
    elif platform == "3DS":
        print("----------- Top Recommendations for " + title + " on the 3DS ------------")
        localFrame = fp.DSData
        name = fp.DSData[fp.DSData['Name'] == title].index[0]
    elif platform == "N64":
        print("----------- Top Recommendations for " + title + " on the N64 ------------")
        localFrame = fp.N64Data
        name = fp.N64Data[fp.N64Data['Name'] == title].index[0]
    else:
        raise AssertionError("Invalid Platform.")
    
    # List of cosine similarity pairs that has the name
    csScores = list(enumerate(matrix[name]))

    # sorted the similarity scores and finding the top 5 recomendations
    csScoresSorted = sorted(csScores, key=lambda pair: pair[1], reverse=True)
    highestScores = csScoresSorted[1:6]
    # print(highestScores)
    
    i = 0
    for pair in enumerate(highestScores):
        i = i + 1
        print('Recommendation ' + str(i) + ': ' + localFrame['Name'].iloc[pair[0]])
    print('-------------------------')
    
main = main()