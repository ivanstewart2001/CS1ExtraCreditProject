import json
import ctypes

def checkUserName(userName):
    with open('database.txt', "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith('{'+ '"' +f'{userName}'):
                return f'Welcome back {userName}!'
        return "You do not have an account. Please make an account to start making a playlist!"

def addUser(userName):
    data = {}
    data[userName] = {}
    data[userName].update({
        "Playlist" : None
    })

    with open('database.txt', 'a+') as outfile:
        outfile.write('\n')
        json.dump(data, outfile)

def checkPlaylist(userName):
    with open('database.txt', 'r') as f:
        for x in f:
            data = json.loads(x)
            databaseUsernames = json.dumps(list(data.keys()))
            if userName in databaseUsernames:
                if None in data[userName].values():
                    return True
        return "You already have a playlist created!"


def updatePlaylist(userName, playlist):
    with open('database.txt', 'r') as f:
        lines = f.readlines()
        with open('database.txt', 'w') as f:
            for line in lines:
                if not line.startswith('{'+ '"' +f'{userName}'):
                    f.write(line)
    
    

    data = {}
    data[userName] = {}
    data[userName].update({
        "Playlist" : playlist
    })

    

    with open('database.txt', 'a+') as outfile:
        outfile.write('\n')
        json.dump(data, outfile)

def deleteEPlayist(userName):
    with open('database.txt', 'r') as f:
        lines = f.readlines()
        with open('database.txt', 'w') as f:
            for line in lines:
                if not line.startswith('{'+ '"' +f'{userName}'):
                    f.write(line)
        
    data = {}
    data[userName] = {}
    data[userName].update({
        "Playlist" : None
    })

    with open('database.txt', 'a+') as outfile:
        outfile.write('\n')
        json.dump(data, outfile)


#print(checkUserName('John'))
#createUser('Jack')
# print(checkPlaylist('Bobby'))
# updatePlaylist('Bobby', [1,2,3])
# #deleteEPlayist('Bobby')