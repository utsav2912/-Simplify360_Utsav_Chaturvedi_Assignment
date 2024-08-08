from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.adj_list = defaultdict(set)

    def add_friendship(self, person1, person2):
        # Add an undirected edge between person1 and person2
        self.adj_list[person1].add(person2)
        self.adj_list[person2].add(person1)

    def bfs(self, start):
        # Perform BFS to find all friends and distances from start
        visited = set()
        queue = deque([(start, 0)])
        friends = {}
        while queue:
            person, distance = queue.popleft()
            if person not in visited:
                visited.add(person)
                friends[person] = distance
                for neighbor in self.adj_list[person]:
                    if neighbor not in visited:
                        queue.append((neighbor, distance + 1))
        return friends

def main():
    graph = Graph()
    
    # Add friendships
    graph.add_friendship("Alice", "Bob")
    graph.add_friendship("Alice", "Charlie")
    graph.add_friendship("Bob", "David")
    graph.add_friendship("Charlie", "Eve")
    graph.add_friendship("David", "Eve")

    # Find all friends of Alice
    alice_friends = graph.bfs("Alice")
    print("Friends of Alice:", alice_friends)

    # Find all friends of Bob
    bob_friends = graph.bfs("Bob")
    print("Friends of Bob:", bob_friends)

    # Find common friends of Alice and Bob
    common_friends = set(alice_friends.keys()).intersection(bob_friends.keys())
    print("Common Friends of Alice and Bob:", common_friends)

    # Find nth connection between Alice and Eve
    nth_connection = alice_friends.get("Eve", -1)
    print("Nth connection between Alice and Eve:", nth_connection)

if __name__ == "__main__":
    main()
