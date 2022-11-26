import tweepy
import json
import config

lengthConsulta = 5
client = tweepy.Client(bearer_token = config.BEARER_TOKEN)

def buscar(str):
    try:
        usu = client.get_user(username = str, user_fields=['profile_image_url'])  
        # print('\n\n\n\n\n')
        print(usu)
        # print(usu['profile_image_url']) 
        # print('\n\n\n\n\n')
    except:
        return {
            'data':{},
            'followers': {},
            'followings': {},
        }
    
    id = usu.data['id']
    
    followings = getFollowings(id)
    followers = getFollowers(id)
    getTweets(id)
    # recentsTweets(usu.data['name'])
    
        
    user = {
        'data':{'id':id, 'name' :usu.data['name'], 'username': usu.data['username']},
        'followers': followers,
        'followings': followings,
    }
    return user

def recentsTweets(id):
    response = client.search_recent_tweets(q=id)
    # print(response)

def getTweets(id):
    allTweets = client.get_users_tweets(id = id, max_results = lengthConsulta)
    
    # print(allTweets)

def getFollowings(id):
    followings = {
        'followings': {}
    }
    followingResponse = client.get_users_following(id = id, max_results = lengthConsulta)
    if followingResponse.data != None:
        for i in range(len(followingResponse.data)) :
            followings['followings'][i] = {
                'id': followingResponse.data[i]['id'],
                'name': followingResponse.data[i]['name'],
                'username': followingResponse.data[i]['username'],
                'username': followingResponse.data[i]['username'],   
            }
            
    return followings

def getFollowers(id):
    followersResponse = client.get_users_followers(id = id, max_results = lengthConsulta)
    
    followers = {
        'followers': {}
    }
    
    if followersResponse.data != None:
        for i in range(len(followersResponse.data)) :
            followers['followers'][i] = {
                'id': followersResponse.data[i]['id'],
                'name': followersResponse.data[i]['name'],
                'username': followersResponse.data[i]['username'],
                'username': followersResponse.data[i]['username'],   
            }
            
    return followers
# print(metodo('iutria97'))


















