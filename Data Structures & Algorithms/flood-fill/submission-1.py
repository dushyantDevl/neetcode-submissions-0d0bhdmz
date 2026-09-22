class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        ogColor = image[sr][sc]
        if ogColor == color: # nothing to do; also prevents infinite recursion
            return image
        directions = [(-1,0),(0,1),(1,0),(0,-1)]

        ## We don't need a visited array here, bcoz we're keeping that track by coloring in the input
        ## 'image' itself i.e if it's the valid neighbor cell and not colored that means it's not
        ## visited yet, and tho we could've returned a new output list, the question does says:
        ## Return the modified image after performing the flood fill, so we'll just return this
        ## modified image list

        # Using BFS

        q = deque()
        q.append((sr, sc)) # start filling from given pixel

        while q:
            r, c = q.popleft()
            image[r][c] = color # mark visited (or modify the pixel)

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == ogColor:
                    q.append((nr,nc))

        return image