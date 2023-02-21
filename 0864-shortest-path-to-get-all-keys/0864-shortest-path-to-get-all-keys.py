class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        
        grid_coords = set()
        keys_count = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != '#':
                    if grid[r][c] == '@':
                        starting = (r,c)
                    if grid[r][c].isalpha():
                        if grid[r][c].islower():
                            keys_count += 1 
                    grid_coords.add((r,c))

        r,c = starting
        queue = deque([(r,c, [], 0)])
        seen = set()

        while queue:
            r, c, keys, count = queue.popleft()
            count += 1

            for dr, dc in ((-1,0), (1,0), (0,-1), (0,1)):
                curr_keys = keys.copy()
                nr = r + dr
                nc = c + dc 

                if (nr,nc) not in grid_coords or (nr,nc,str(curr_keys)) in seen:
                    continue

                elem = grid[nr][nc]

                if elem.isalpha():
                    if elem.isupper() and elem.lower() not in keys:
                        continue
                    elif elem.islower() and elem not in curr_keys:
                        curr_keys.append(elem)


                if len(curr_keys) == keys_count:
                    return count

                queue.append((nr,nc, curr_keys, count))
                seen.add((nr,nc,str(keys)))

        return -1 