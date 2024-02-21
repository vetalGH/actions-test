import pymongo
import random
import string
import datetime

from constants import MONGO_URL


client = pymongo.MongoClient(MONGO_URL)
db = client["my_db"]
collection = db["users"]


def generate_random_name():
    """Generate a random name."""
    return "".join(random.choices(string.ascii_letters, k=6))


def create_record():
    """Create a record with a random name and current timestamp."""
    name = generate_random_name()
    timestamp = datetime.datetime.now()
    record = {"name": name, "timestamp": timestamp}
    collection.insert_one(record)
    print("Record created:", record)


def main():

    create_record()


if __name__ == "__main__":
    main()
