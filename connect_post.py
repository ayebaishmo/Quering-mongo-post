import psycopg2
import Queries as q

DNAME = 'pjksxssb'
USER = 'pjksxssb'
PASSWORD = 'wK01rRzqfi2AHOcB0wHEQRlzwCK4sj0X'
HOST = 'jelani.db.elephantsql.com'

def connect_to_pg(dbname = DNAME, user = USER, password = PASSWORD, host = HOST):
    pg_conn = psycopg2.connect(dbname = DNAME, user = USER, password = PASSWORD, host=HOST)
    pg_curs = pg_conn.cursor()
    return pg_conn, pg_curs

def exequte_q(conn, curs, query):
    curs.execute(query)
    result = curs.fetchall()
    return result

if __name__=="__main__":
    conn, curs = connect_to_pg()
    # How many passengers survived, and how many died?
    # result = exequte_q(conn, curs, SURVIVE_AND_DIED)
    # survived_count, died_count = result
    # print("Survived", survived_count)
    # print("Died", died_count)

    # How many passengers were in each class?
    # result = exequte_q(conn, curs, EACH_CLASS)
    # print(result)
    # for row in result:
    #     Pclass, passenger_count =row
    #     print(f"Class {Pclass}: {passenger_count} passengers")

    # How many passengers survived/died within each class?
    # result = exequte_q(conn, curs, CLASS_SURVIVAL)
    # print(result)
    # for row in result:
    #     Pclass, class_per_survive =row
    #     Survived = 1 if class_per_survive == 0 else 0
    #     status ="Survived" if Survived else "Died"
    #     print(f"class {Pclass}: {class_per_survive} passengers {status}")

    # What was the average age of survivors vs nonsurvivors?
    # result = exequte_q(conn, curs, AVERAGE_AGE)
    # print(result)
    # for row in result:
    #     print(row)

    # What was the average age of each passenger class?
    # result = exequte_q(conn, curs, AVERAGE_AGE_PER_PASSENGR_CLASS)
    # print(result)

    # What was the average fare by passenger class? By survival?
    # result = exequte_q(conn, curs, AVERAGE_FARE_BY_CLASS_BY_SURVIVAL)
    # print(result)

    # How many siblings/spouses aboard on average, by passenger class? By survival?
    # result = exequte_q(conn, curs, SCIBLINGS_AVG_BY_PASSAGER_CLASS_AND_SURCVIVAL)
    # print(result)

    # How many parents/children aboard on average, by passenger class? By survival?
    # result = exequte_q(conn, curs, q.CHILDREN_ABOARD_AVG_BY_PASSAGERCLASS_AND_SURVIVAL)
    # print(result)

    # Do any passengers have the same name?
    result = exequte_q(conn, curs, q.PASSAGERS_HAVE_SAME_NAME)
    print(result)
    conn.close()
