from sqlalchemy import create_engine
import pandas as pd

connection_string = ""

# Create SQLAlchemy engine
engine = create_engine(connection_string)

# SQL query
drillDownQuery = """
SELECT NumOfBedrooms, MultipurposeRoom, ChildrenPlayArea, COUNT(*) AS numOfEntries
FROM indoorroomsdimension
GROUP BY NumOfBedrooms, MultipurposeRoom, ChildrenPlayArea
ORDER BY NumOfBedrooms DESC, MultipurposeRoom, ChildrenPlayArea;
"""

rollUpQuery = """
SELECT
    COALESCE("numofbedrooms"::text, "multipurposeroom"::text) AS indoor_room,
    COUNT(*) AS numOfEntries
FROM
    indoorroomsdimension
GROUP BY ROLLUP ("numofbedrooms", "multipurposeroom")
ORDER BY indoor_room;
"""

sliceQuery = """
SELECT refrigerator FROM householddimension

"""

diceQuery1 = """
SELECT *
FROM communitydimension
WHERE School = true AND Hospital = true;
"""

diceQuery2 = """
SELECT *
FROM householddimension
WHERE ac = true AND tv = true;
"""

combinedQuery1 = """

SELECT spft.price
FROM salespricefactstable spft
JOIN outdooramentitiesdimension oad ON spft.outdooramentitiesid = oad.outdooramentitiesid
WHERE oad.swimmingpool = true;

"""

combinedQuery2 = """
SELECT 
    spft.price
FROM 
    salespricefactstable spft
JOIN 
    outdooramentitiesdimension oad ON spft.outdooramentitiesid = oad.outdooramentitiesid
WHERE 
    oad.joggingtrack = true;

"""



combinedQuery3 = """
    SELECT 
        spft.price
    FROM 
        salespricefactstable spft
    JOIN 
        householddimension had ON spft.householdapplianceid = had.householdapplianceid
    WHERE 
        had.refrigerator = true;

"""

combinedQuery4 = """
    SELECT 
        spft.price
    FROM 
        salespricefactstable spft
    JOIN 
        householddimension had ON spft.householdapplianceid = had.householdapplianceid
    WHERE 
        had.washingmachine = true;


"""

icebergQuery = """
SELECT *
FROM salespricefactstable
WHERE price > 60000000;

"""

windowingQuery = """
SELECT
    *,
    AVG(Price / Area) OVER () AS avg_price_per_sqm,
    RANK() OVER (ORDER BY Price / Area DESC) AS price_per_sqm_rank
FROM
    salespricefactstable;
"""

windowQuery = """
SELECT
    Location,
    Price,
    ROW_NUMBER() OVER (PARTITION BY Location ORDER BY Price) AS position
FROM
    salespricefactstable
WHERE
    Location IN ('Kengeri', 'Horamavu')
WINDOW
    exclude_cols AS (PARTITION BY Location ORDER BY (SELECT 1))


"""


# Execute the query and read into DataFrame
#drillDown = pd.read_sql(drillDownQuery, engine)
#rollUp = pd.read_sql(rollUpQuery, engine)
#slice = pd.read_sql(sliceQuery, engine)
# dice1 = pd.read_sql(diceQuery1, engine)
#dice2 = pd.read_sql(diceQuery2, engine)


#combined1 = pd.read_sql(combinedQuery1, engine)
#combined2 = pd.read_sql(combinedQuery2, engine)
#combined3 = pd.read_sql(combinedQuery3, engine)
#combined4 = pd.read_sql(combinedQuery4, engine)


# iceBerg = pd.read_sql(icebergQuery, engine)

#window = pd.read_sql(windowQuery, engine)

#windowing = pd.read_sql(windowingQuery, engine)



