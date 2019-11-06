import random
# friendship is a 2-way thing. so it's an undirected graph 


class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    
    def addFriendship(self, userID, friendID):
        # addFriendship is basically adding an edge. Because the graph edges are the friendships 
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        # addUser is like adding vertices. Users are nodes/vertices
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set() #this tells us its an adjacency list 

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments
​
        Creates that number of users and a randomly distributed friendships
        between those users.
​
        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # call addUser() until our number of users is numUsers
        for i in range(numUsers):
            self.addUser(f"User {i+1}")

        # Create random friendships
        # totalFriendships = avgFriendships * numUsers
        # Generate a list of all possible friendships
        possibleFriendships = []
        # Avoid dups by ensuring the first ID is smaller than the second
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                possibleFriendships.append( (userID, friendID) )

        # Shuffle the list
        random.shuffle(possibleFriendships)
        print("random friendships:")
        print(possibleFriendships)

        # Slice off totalFriendships from the front, create friendships
        totalFriendships = avgFriendships * numUsers // 2
        # need to divide by two because every time we call self.addFriendship, we're adding two friendships (but they're really the same one. like 1 is friends with 2 AND 2 is friends with 1)
        print(f"Friendships to create: {totalFriendships}\n")
        for i in range(totalFriendships):
            friendship = possibleFriendships[i]
            self.addFriendship( friendship[0], friendship[1] )




    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        
        # !!!! IMPLEMENT ME
        

        # Use a BFS to find the shortest path
        # Instead of using a set to mark users as visited, you could use a dictionary

        # q = Queue()
        # q.enqueue([userID])
        # visited = {}  # Note that this is a dictionary, not a set
        # while q.size() > 0:
        #     temp_ID = q.dequeue()
            
        #     for i in self.friendships[temp_ID]:
        #         if i not in visited:
        #             q.enqueue(i)
        #             visited[i] = [*visited[temp_ID], i]
            

        # return visited

        visited = {}  # Note that this is a dictionary, not a set
        visited[userID] = [userID] # start up the dictionary 
        q = Queue()
        q.enqueue(userID)

        while q.size() > 0:
            temp_ID = q.dequeue()

            for i in self.friendships[temp_ID]: # this is looking at all the "neighbors" of temp_id. id is the vertex and friendships are edges
                if i not in visited:
                    q.enqueue(i)
                    visited[i] = [visited[temp_ID], i] 
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(11, 3)
    # print("USERS:")
    # print(sg.users)
    # print("FRIENDSHIPS:")
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print("DEGREES BROOOO")
    print(connections)
    print("Friendships........")
    print(sg.friendships)