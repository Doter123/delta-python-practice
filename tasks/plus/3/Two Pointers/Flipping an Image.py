from typing import List

def flipAndInvertImage(image: List[List[int]]) -> List[List[int]]:
    for row in image:
        l,r=0,len(row)-1
        while l <= r:
            # row[l], row[r] = int(not row[r]), int(not row[l])

            row[l], row[r] = row[r], row[l]

            row[l] = 0 if row[l] else 1
            if l == r: break
            row[r] = 0 if row[r] else 1

            l += 1
            r -= 1

    return image

print(flipAndInvertImage(
    [[1,1,0],[1,0,1],[0,0,0]]  # =>  [[1,0,0],[0,1,0],[1,1,1]]
))

print(flipAndInvertImage(
    [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]  # =>  [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
))