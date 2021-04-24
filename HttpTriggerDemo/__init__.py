import logging
import azure.functions as func



def main(req: func.HttpRequest, dbag: func.DocumentList) -> str:
    logging.info('Python HTTP trigger function processed a request.')

    if not dbag:
        logging.warning("ToDo item not found")
    else:
        for document in dbag:
            logging.info("Found ToDo item, Description=%s",
                     document['id'])

    return 'OK'
