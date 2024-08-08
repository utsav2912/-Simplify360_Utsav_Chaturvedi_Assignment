from collections import deque, defaultdict

def topological_sort(num_tasks, adj_list):
    # Initialize in-degree of each task to 0
    in_degree = [0] * num_tasks
    for edges in adj_list:
        for v in edges:
            in_degree[v] += 1

    # Queue for tasks with in-degree 0
    q = deque([i for i in range(num_tasks) if in_degree[i] == 0])

    # List to store the topological order
    topo_order = []
    while q:
        u = q.popleft()
        topo_order.append(u)
        for v in adj_list[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)

    return topo_order

def main():
    num_tasks = 6
    duration = [5, 10, 3, 2, 7, 8]  # Duration of each task

    # Adjacency list representing the task dependencies
    adj_list = [
        [1, 2],  # Task 0 -> Task 1, Task 2
        [3],     # Task 1 -> Task 3
        [3, 4],  # Task 2 -> Task 3, Task 4
        [5],     # Task 3 -> Task 5
        [5],     # Task 4 -> Task 5
        []       # Task 5 has no dependencies
    ]

    # Perform topological sorting
    topo_order = topological_sort(num_tasks, adj_list)

    # Calculate Earliest Start Time (EST) and Earliest Finish Time (EFT)
    EST = [0] * num_tasks
    EFT = [0] * num_tasks
    for u in topo_order:
        EFT[u] = EST[u] + duration[u]
        for v in adj_list[u]:
            EST[v] = max(EST[v], EFT[u])

    # Calculate Latest Finish Time (LFT) and Latest Start Time (LST)
    LFT = [EFT[topo_order[-1]]] * num_tasks
    LST = [0] * num_tasks
    for u in reversed(topo_order):
        LST[u] = LFT[u] - duration[u]
        for v in adj_list[u]:
            LFT[u] = min(LFT[u], LST[v])

    earliest_completion_time = max(EFT)
    latest_completion_time = max(LFT)

    print("Earliest Completion Time:", earliest_completion_time)
    print("Latest Completion Time:", latest_completion_time)

if __name__ == "__main__":
    main()
