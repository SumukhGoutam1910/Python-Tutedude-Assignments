import psycopg2
def table():
    connect = psycopg2.connect(dbname="postgres",user="postgres",password="1910",host="localhost",port="5432")

    cursor=connect.cursor()
    cursor.execute('''create table Aadhar(Name text,ID int,Age int);''')

    print("Table created successfully")

    connect.commit()
    connect.close()

def insert():
    connect = psycopg2.connect(dbname="postgres",user="postgres",password="1910",host="localhost",port="5432")

    cursor=connect.cursor()
    name=input("Enter your name:")
    id=int(input("Enter your ID:"))
    age=int(input("Enter your age:"))
    query=f'''insert into Aadhar values('{name}',{id},{age});'''
    cursor.execute(query)

    print("Values inserted successfully")

    connect.commit()
    connect.close()    

def extract():
    connect = psycopg2.connect(dbname="postgres",user="postgres",password="1910",host="localhost",port="5432")

    cursor=connect.cursor()
    cursor.execute('''select * from Aadhar;''')
    data=cursor.fetchall()
    for i in data:
        print(i)
    connect.commit()
    connect.close()

insert()
extract()