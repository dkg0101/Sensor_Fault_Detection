from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.logger import logging


logging.info("this is first log")
print('successs')

# if __name__=='__main__':
#     mongodb_client = MongoDBClient()
#     print("collection name: ",mongodb_client.database.list_collection_names())
#     # mongodb_client.client.close()