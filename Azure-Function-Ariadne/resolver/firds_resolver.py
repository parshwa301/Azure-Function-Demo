from ariadne import gql, QueryType
from common.cosmos.databaseconnection import *
from azure.cosmos import *
from common.cosmos.documentManagement import *
from ariadne import ObjectType, make_executable_schema

query = QueryType()
#query = ResolverMap("Query")

@query.field("firds")
def resolve_firds(*_):

    container = CosmosDataSet().dbconnection("firds")
    fird_data = read_items(container)
    return fird_data

@query.field("firdsByPartitionKey")
def resolve_firdsByPartitionKey(*_,FinInstrmGnlAttrbtsId):
    container = CosmosDataSet().dbconnection("firds")
    fird_data = read_item(container,"2",FinInstrmGnlAttrbtsId)
    return fird_data
    