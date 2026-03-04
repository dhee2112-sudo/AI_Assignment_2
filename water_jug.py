from collections import deque
import time

# ---------- BFS Function ----------
def water_jug_bfs(cap1, cap2, goal):
    visited = set()
    queue = deque([((0, 0), [])])  # (state, path)
    
    while queue:
        (jug1, jug2), path = queue.popleft()
        
        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))
        
        path = path + [(jug1, jug2)]
        
        # Goal test
        if jug1 == goal or jug2 == goal:
            return path
        
        # Generate next states
        next_states = [
            (cap1, jug2),  # Fill Jug1
            (jug1, cap2),  # Fill Jug2
            (0, jug2),     # Empty Jug1
            (jug1, 0),     # Empty Jug2
            (max(0, jug1 - (cap2 - jug2)), min(cap2, jug2 + jug1)),  # Pour Jug1→Jug2
            (min(cap1, jug1 + jug2), max(0, jug2 - (cap1 - jug1)))   # Pour Jug2→Jug1
        ]
        
        for state in next_states:
            queue.append((state, path))
    
    return None

# ---------- DFS Function ----------
def water_jug_dfs(cap1, cap2, goal):
    visited = set()
    stack = [((0, 0), [])]  # (state, path)
    
    while stack:
        (jug1, jug2), path = stack.pop()
        
        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))
        
        path = path + [(jug1, jug2)]
        
        # Goal test
        if jug1 == goal or jug2 == goal:
            return path
        
        # Generate next states
        next_states = [
            (cap1, jug2),
            (jug1, cap2),
            (0, jug2),
            (jug1, 0),
            (max(0, jug1 - (cap2 - jug2)), min(cap2, jug2 + jug1)),
            (min(cap1, jug1 + jug2), max(0, jug2 - (cap1 - jug1)))
        ]
        
        for state in next_states:
            stack.append((state, path))
    
    return None

# ---------- Main Execution ----------
if __name__ == "__main__":
    # BFS
    start = time.time()
    bfs_solution = water_jug_bfs(4, 3, 2)
    end = time.time()
    print("BFS Solution Path:")
    for step in bfs_solution:
        print(step)
    print("BFS Time:", end - start)
    
    print("\n---------------------\n")
    
    # DFS
    start = time.time()
    dfs_solution = water_jug_dfs(4, 3, 2)
    end = time.time()
    print("DFS Solution Path:")
    for step in dfs_solution:
        print(step)
    print("DFS Time:", end - start)
