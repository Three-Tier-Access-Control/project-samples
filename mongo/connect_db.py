from pymongo import MongoClient


def get_database():

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    # CONNECTION_STRING = "mongodb+srv://ashleytshumba:02june1997@cluster0.ie2a2.mongodb.net/?retryWrites=true&w=majority"
    CONNECTION_STRING = 'mongodb://localhost:27017/'

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['face_db']


def main():
    # Get Database
    dbname = get_database()
    faces = dbname["face"]
    count = faces.count_documents({})
    print(count)

if __name__ == "__main__":
    main()

    
