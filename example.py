from pymongo import MongoClient

uri = "mongodb://root:example@mongo:27017/"

client = MongoClient(uri)

database = client.crud
collection = database.pessoas

def insert():
    collection.insert({
        'field': 'value'
    })


def read(**args):
    '''
    variacoes do find
    find
    find_one
    find_many

    operator de querys

    '''

    collection.find({
        'field': 'value'
    })

def find_by_oparetor(operator, idade):
    '''
    $eq: igual a (==)
    $ne: diferente de (!=)
    $gt: maior que (>)
    $gte: maior ou igual (>=)
    $lt: menor que (<)
    $lte: menor ou igual (<=)
    $in: Contem em um array (in)
    $nin: nao contem em um array (not in) 
    and more > https://www.mongodb.com/docs/manual/reference/operator/query/
    '''
    collection.find({
        'field': {
            '$operator': 'value'
        }
        
    })


def update():
    '''
    sem o operator set ele substitui o campo tambem 
     collection.update(
        {'name': 'ab'},# find
        {'abacate': 'JJ James'} #update
    )

    agora name vai se chamar abacate 
    ele pega o primeiro registro e troca pelo secundo 

    operator 
    $set: faz o update
    $unset: remove valor
    $rename: renomeia o campo 

    pra atualizar todos update_many
    '''
    collection.update(
        {'name': 'ab'},# find
        {"$set": {'name': 'JJ James'}} #update
    )

def remove():
    collection.remove(
        {'field': {'$op': 'value'}}
    )
