import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey

def read_item(container, doc_id, partition_key):
    # Note that Reads require a partition key to be spcified.
    response = container.read_item(item=doc_id, partition_key=partition_key)
    return response



def read_items(container):

    item_list = list(container.read_all_items(max_item_count=10))
    return item_list