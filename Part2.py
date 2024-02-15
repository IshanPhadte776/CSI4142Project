import pandas as pd

#Data Staging Steps (ETL)

#Extract 

# Read the csv file into a pandas dataframe
df= pd.read_csv('Bangalore.csv')


#Transform

#Converting Data Types

exclude_cols = ['Price', 'Area', 'Location', 'No. of Bedrooms']
# Convert all columns except the ones in exclude_cols to boolean type
df[df.columns.difference(exclude_cols)] = df[df.columns.difference(exclude_cols)].astype(bool)
df['Price'] = df['Price'].astype(int)
df['Area'] = df['Area'].astype(int)
df['No. of Bedrooms'] = df['No. of Bedrooms'].astype(int)
# Print a Series with the data type of each column
#print(df.dtypes)
df = df.drop(columns=['LiftAvailable'])

#Handling Incomplete Data 

#Keep only the first 1951 Rows, throw out the rest (incomplete rows)
df = df.iloc[:1951]
# Get the number of rows
num_rows = df.shape[0]
#print("Number of rows:", num_rows)

#Handling Typos / Data Consistency 
df = df.rename(columns={'No. of Bedrooms': 'NumOfBedrooms'})
df = df.rename(columns={"Children'splayarea": "ChildrenPlayArea"})
df = df.rename(columns={"Gasconnection": "GasConnection"})
df = df.rename(columns={"BED": "Bed"})
df = df.rename(columns={"ClubHouse": "Clubhouse"})

#Removing unused columns
df = df.drop(columns=['VaastuCompliant'])

#Converting the Strings of Location to a Set for Analysis
df['Location'] = df['Location'].str.split(',')
df['Location'] = df['Location'].apply(set)


# Providing a Surrogate Key for each row 
df['SurrogateKey'] = df.reset_index().index + 1

#Creating the Dimension Tables  

salesPriceDF = df[['Location', 'Area', 'Price']].reset_index()
salesPriceDF['SaleID'] = salesPriceDF.index + 1



householdApplianceDF = df[['WashingMachine', 'AC', 'Microwave', 'TV','Wardrobe','Refrigerator' ]]
outdoorAmentitiesDF = df[['SwimmingPool', 'LandscapedGardens', 'JoggingTrack', 'RainWaterHarvesting']]
communityDF = df[['ShoppingMall', 'SportsFacility', 'School','Hospital']]
indoorRoomsDF = df[['NumOfBedrooms', 'Gymnasium', 'IndoorGames','Clubhouse','MultipurposeRoom','ChildrenPlayArea']]

householdApplianceDF['HouseHoldApplianceID'] = salesPriceDF['SaleID']
outdoorAmentitiesDF['OutdoorAmentitieseID'] = salesPriceDF['SaleID']
communityDF['CommunityID'] = salesPriceDF['SaleID']
indoorRoomsDF['IndoorRoomID'] = salesPriceDF['SaleID']

salesPriceDF['HouseHoldApplianceID'] = householdApplianceDF['HouseHoldApplianceID']
salesPriceDF['OutdoorAmentitiesID'] = outdoorAmentitiesDF['OutdoorAmentitieseID']
salesPriceDF['CommunityID'] = communityDF['CommunityID']
salesPriceDF['IndoorRoomID'] = indoorRoomsDF['IndoorRoomID']


# print(salesPriceDF.dtypes)
# print(householdApplianceDF.dtypes)
# print(outdoorAmentitiesDF.dtypes)
# print(communityDF.dtypes)

#print(communityDF.dtypes)

# print(salesPriceDF[:25])
# print(householdApplianceDF[:25])


#Load
#Pick a DBMS (Probably SQL > NoSQL)
#Probably MongoDB (NOSQL) Its Cloud Based and very popular database