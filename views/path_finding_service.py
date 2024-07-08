from collections import deque

class PathFindingService:
    def bfs(self, start, goal, grid):
        queue = deque([start])
        visited = set()
        visited.add(start)

        while queue:
            current = queue.popleft()
            if current == goal:
                return True

            for neighbor in self.get_neighbors(current, grid):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return False

    def get_neighbors(self, position, grid):
        x, y = position
        neighbors = []
        if x > 0:
            neighbors.append((x - 1, y))
        if x < len(grid) - 1:
            neighbors.append((x + 1, y))
        if y > 0:
            neighbors.append((x, y - 1))
        if y < len(grid[0]) - 1:
            neighbors.append((x, y + 1))
        return neighbors
