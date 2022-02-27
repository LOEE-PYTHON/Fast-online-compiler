from authomatic.providers import oauth2
import os


# CONFIG = {
#     'github': {
#         'class_': oauth2.GitHub,
#         'consumer_key':os.environ.get('GITHUB_CLIENT_ID'),
#         'consumer_secret':os.environ.get('GITHUB_CLIENT_SECRET'),
#         'access_headers': {'User-Agent': 'fast-compiler'},
#     }
# }

appConfig = {
    #MongoDB Configurations
    'MONGODB_SETTINGS':{
        'db': 'fast_compiler',
        'host': 'mongodb_container',
        'port': 27017,
        'username':os.environ.get('MongoUserName'),
        'password':os.environ.get('MongoPassWord'),
    }
}