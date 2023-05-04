import pandas as pd

print("------------------------------------")
print("FILE PROCESSOR START")
print("------------------------------------")

allVideoGameData = pd.read_csv("Data/Video_Games_Sales_as_at_22_Dec_2016.csv")
allVideoGameData = allVideoGameData.loc[:, ['Name', 'Platform', 'Genre', 'Publisher', 'Global_Sales', 'Critic_Score', 'User_Score', 'Rating']]

# saving data based off of consoles
PCData = allVideoGameData[allVideoGameData['Platform'] == 'PC']
XOneData = allVideoGameData[allVideoGameData['Platform'] == 'XOne']
PS4Data = allVideoGameData[allVideoGameData['Platform'] == 'PS4']
WiiUData = allVideoGameData[allVideoGameData['Platform'] == 'WiiU']
DSData = allVideoGameData[allVideoGameData['Platform'] == '3DS']
N64Data = allVideoGameData[allVideoGameData['Platform'] == 'N64']

# checking that dataframes were made correctly
# Checking complete CSV was imported
if allVideoGameData.notnull().any().any():
    print("Complete CSV File import successful.")
else:
    raise AssertionError("Complete CSV File did not import correctly.")

# Checking PCData was created correctly and dropping duplicates if exists
if PCData.notnull().any().any():
    if (PCData.duplicated(subset = ['Name']).any()):
        PCData = PCData.drop_duplicates()
        print("PCData creation successful.")
else:
    raise AssertionError("PCData creation unsuccessful.")

# Checking XOneData was created correctly and dropping duplicates if exists
if XOneData.notnull().any().any():
    if (XOneData.duplicated(subset = ['Name']).any()):
        XOneData = XOneData.drop_duplicates()
    print("XOneData creation successful.")
else:
    raise AssertionError("XOneData creation unsuccessful.")

# Checking PS4Data was created correctly and dropping duplicates if exists
if PS4Data.notnull().any().any():
    if (PS4Data.duplicated(subset = ['Name']).any()):
        PS4Data = PS4Data.drop_duplicates()
    print("PS4Data creation successful.")
else:
    raise AssertionError("PS4Data creation unsuccessful.")

# Checking WiiUData was created correctly and dropping duplicates if exists
if WiiUData.notnull().any().any():
    if (WiiUData.duplicated(subset = ['Name']).any()):
        WiiUData = WiiUData.drop_duplicates()
    print("WiiUData creation successful.")
else:
    raise AssertionError("WiiUData creation unsuccessful.")

# Checking DSData was created correctly and dropping duplicates if exists
if DSData.notnull().any().any():
    if (DSData.duplicated(subset = ['Name']).any()):
        DSData = DSData.drop_duplicates()
    print("3DSData creation successful.")
else:
    raise AssertionError("3DSData creation unsuccessful.")

# Checking N64Data was created correctly and dropping duplicates if exists
if N64Data.notnull().any().any():
    if (N64Data.duplicated(subset = ['Name']).any()):
        N64Data = N64Data.drop_duplicates()
    print("N64Data creation successful.")
else:
    raise AssertionError("N64Data creation unsuccessful.")

# if here, all made it
print("------------------------------------")
print("All dataframes ready.")
print("------------------------------------")

# used for finding all unique platform types and choosing which ones we want to work with
def numberOfUniquePlatforms(dataframe):
    platforms = dataframe['Platform'].unique()
    print("All Platforms Evident in Dataset:")
    for platform in platforms:
        print(platform)

print("FILE PROCESSOR END")
print("------------------------------------")