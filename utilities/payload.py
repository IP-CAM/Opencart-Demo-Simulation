#Functions to build dynamic data from external sources

from utilities.configurations import *


def buildPayLoadFromDB(query):
    addBody = []
    tp = getQuery(query) #tp for tuple
    for row in tp:
        # Assuming row[0] is the product_id, adjust if needed
        payload = {
            "product_id": row[0],
            "quantity": 2
        }
        addBody.append(payload)
    return addBody