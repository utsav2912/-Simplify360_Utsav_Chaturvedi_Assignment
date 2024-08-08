from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.adj_list = defaultdict(set)

    def add_friendship(self, person1, person2):
        # Add an undirected edge between person1 and person2
        self.adj_list[person1].add(person2)
        self.adj_list[person2].add(person1)

    def get_friends(self, person):
        # Return the set of friends for a given person
        return self.adj_list[person]

    def get_common_friends(self, person1, person2):
        # Get the intersection of friends sets of person1 and person2
        return self.adj_list[person1].intersection(self.adj_list[person2])

    def find_connection(self, person1, person2):
        # Return -1 if either person is not in the graph
        if person1 not in self.adj_list or person2 not in self.adj_list:
            return -1
        
        # BFS to find the shortest path between person1 and person2
        queue = deque([(person1, 0)])
        visited = set([person1])
        
        while queue:
            current, level = queue.popleft()
            if current == person2:
                return level
            
            for neighbor in self.adj_list[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, level + 1))
        
        return -1

def main():
    g = Graph()
    g.add_friendship("Alice", "Bob")
    g.add_friendship("Bob", "Janice")
    g.add_friendship("Alice", "Charlie")
    g.add_friendship("Charlie", "Diana")

    # Find friends of Alice
    alice_friends = g.get_friends("Alice")
    print("Friends of Alice:", alice_friends)

    # Find friends of Bob
    bob_friends = g.get_friends("Bob")
    print("Friends of Bob:", bob_friends)

    # Find common friends of Alice and Bob
    common_friends = g.get_common_friends("Alice", "Bob")
    print("Common friends of Alice and Bob:", common_friends)

    # Find connection between Alice and Janice
    connection = g.find_connection("Alice", "Janice")
    print("Connection between Alice and Janice:", connection)

    # Find connection between Alice and Diana
    connection = g.find_connection("Alice", "Diana")
    print("Connection between Alice and Diana:", connection)

if __name__ == "__main__":
    main()
