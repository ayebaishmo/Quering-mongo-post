SURVIVE_AND_DIED = '''
SELECT 
COUNT(CASE WHEN "Survived"= 1 THEN 1 END) AS survived_count,
COUNT(CASE WHEN "Survived"= 0 THEN 1 END) AS died_count
FROM
titanic_table
'''

EACH_CLASS = '''
SELECT
    "Pclass",
    COUNT(*) AS passenger_count
FROM
    titanic_table
GROUP BY
    "Pclass"
'''

CLASS_SURVIVAL = '''
SELECT 
    "Pclass"
    "Survived",
COUNT(*) AS 
    class_per_survive
FROM 
    titanic_table
GROUP BY
    "Pclass", "Survived"
'''

AVERAGE_AGE = '''
SELECT
    "Survived",
    AVG("Age") AS average_age
FROM 
    titanic_table
GROUP BY
    "Survived"
    '''

AVERAGE_AGE_PER_PASSENGR_CLASS = '''
SELECT
    "Pclass",
    AVG("Age") AS aappc
FROM
    titanic_table
GROUP BY
    "Pclass"
'''

AVERAGE_FARE_BY_CLASS_BY_SURVIVAL ='''
SELECT
    "Pclass"
    "Survived",
    AVG("Fare") AS  Average_fare_by_class_and_survival
FROM 
    titanic_table
GROUP BY
    "Pclass",
    "Survived"
'''

SCIBLINGS_AVG_BY_PASSAGER_CLASS_AND_SURCVIVAL = '''
SELECT 
    "Pclass"
    "Survived",
    AVG("Siblings/Spouses Aboard") AS SAPCS
FROM 
    titanic_table
GROUP BY
    "Pclass",
    "Survived"
'''

CHILDREN_ABOARD_AVG_BY_PASSAGERCLASS_AND_SURVIVAL = '''
SELECT
    "Pclass"
    "Survived",
    AVG("Parents/Children Aboard") AS CBABPAS
FROM 
    titanic_table
GROUP BY
    "Pclass",
    "Survived"
'''

PASSAGERS_HAVE_SAME_NAME = '''
SELECT
    "Name",
    COUNT(*) AS name_count
FROM 
    titanic_table
GROUP BY
    "Name"
HAVING
    COUNT(*) > 1
'''