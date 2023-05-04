import warnings
import file_processor as fp
import graphs as g
import matplotlib as plt
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

warnings.filterwarnings("ignore")

print("GRAPH CREATION START")
print("------------------------------------")

# ---- GRAPH CREATION
#g.CreateGraphs(fp.allVideoGameData)
#CreateGraph(fp.PCData)
# Other graphs that might be necessary

print("GRAPH CREATION END")
print("------------------------------------")

print("PROGRAM START")
print("------------------------------------")

# -----FUNCTIONS
# Function handeling actual recommendations
def GameRecommendation(title, matrix):
    print("Hello")

# Fixes the labeling of the name in the csv to be parseable and readable for the matrix
def FixTitleFormat(value):
    return value.replace(' ', '')

# fixes the recommended column to be parseable and readable for the matrix
def ChangeFormat(value):
    return ' '.join(value)

#file_processor.numberOfUniquePlatforms(file_processor.allVideoGameData)
# fp.PCData fp.XOneData fp.PS4Data fp.WiiUData fp.DSData fp.N64Data

print("CREATING MATRICES")
print("------------------------------------")

# saving a new column in the dataframe to give our matrices values to run off of.
# New column is just all the columns we already parsed since we deem them necessary for recommendations
fp.PCData['Recommended'] = fp.PCData.apply(lambda row: row.index[row != row['Name']].to_list(), axis = 1)
fp.XOneData['Recommended'] = fp.XOneData.apply(lambda row: row.index[row != row['Name']].to_list(), axis = 1)
fp.PS4Data['Recommended'] = fp.PS4Data.apply(lambda row: row.index[row != row['Name']].to_list(), axis = 1)
fp.WiiUData['Recommended'] = fp.WiiUData.apply(lambda row: row.index[row != row['Name']].to_list(), axis = 1)
fp.DSData['Recommended'] = fp.DSData.apply(lambda row: row.index[row != row['Name']].to_list(), axis = 1)
fp.N64Data['Recommended'] = fp.N64Data.apply(lambda row: row.index[row != row['Name']].to_list(), axis = 1)

# creating the transform matrix's for each platform
# PC
fp.PCData['Recommended'] = fp.PCData['Recommended'].apply(ChangeFormat)
fp.PCData['Recommended'] = fp.PCData['Recommended'] + ' ' + fp.PCData['Name'].apply(ChangeFormat)
PCMatrix = CountVectorizer().fit_transform(fp.PCData['Recommended'])
PCcsMatrix = cosine_similarity(PCMatrix, PCMatrix)

# Xbox One
fp.XOneData['Recommended'] = fp.XOneData['Recommended'].apply(ChangeFormat)
fp.XOneData['Recommended'] = fp.XOneData['Recommended'] + ' ' + fp.XOneData['Name'].apply(ChangeFormat)
XOneMatrix = CountVectorizer().fit_transform(fp.XOneData['Recommended'])
XOnecsMatrix = cosine_similarity(XOneMatrix, XOneMatrix)

# PS 4
fp.PS4Data['Recommended'] = fp.PS4Data['Recommended'].apply(ChangeFormat)
fp.PS4Data['Recommended'] = fp.PS4Data['Recommended'] + ' ' + fp.PS4Data['Name'].apply(ChangeFormat)
PS4Matrix = CountVectorizer().fit_transform(fp.PS4Data['Recommended'])
PS4csMatrix = cosine_similarity(PS4Matrix, PS4Matrix)

# Wii U
fp.WiiUData['Recommended'] = fp.WiiUData['Recommended'].apply(ChangeFormat)
fp.WiiUData['Recommended'] = fp.WiiUData['Recommended'] + ' ' + fp.WiiUData['Name'].apply(ChangeFormat)
WiiUMatrix = CountVectorizer().fit_transform(fp.WiiUData['Recommended'])
WiiUcsMatrix = cosine_similarity(WiiUMatrix, WiiUMatrix)

# 3DS
fp.DSData['Recommended'] = fp.DSData['Recommended'].apply(ChangeFormat)
fp.DSData['Recommended'] = fp.DSData['Recommended'] + ' ' + fp.DSData['Name'].apply(ChangeFormat)
DSMatrix = CountVectorizer().fit_transform(fp.DSData['Recommended'])
DScsMatrix = cosine_similarity(DSMatrix, DSMatrix)

# N64
fp.N64Data['Recommended'] = fp.N64Data['Recommended'].apply(ChangeFormat)
fp.N64Data['Recommended'] = fp.N64Data['Recommended'] + ' ' + fp.N64Data['Name'].apply(ChangeFormat)
N64Matrix = CountVectorizer().fit_transform(fp.N64Data['Recommended'])
N64csMatrix = cosine_similarity(N64Matrix, N64Matrix)

print("MATRICES CREATED")
print("------------------------------------")

print("GAME RECOMMENDATIONS START")
print("------------------------------------")

# ----- Creating Recommendations
#GameRecommendation('Call of Duty: Ghosts', XOnecsMatrix)
#GameRecommendation('Call of Duty: Ghosts', PS4csMatrix)

print("GAME RECOMMENDATIONS END")
print("------------------------------------")

print("PROGRAM END")
print("------------------------------------")