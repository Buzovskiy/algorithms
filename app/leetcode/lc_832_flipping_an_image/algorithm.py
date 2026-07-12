from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        image_new = [[0 for i in range(len(image[0]))] for i in range(len(image))]
        for i in range(len(image)):
            for j in range(len(image[0])):
                image_new[i][len(image[0])-1-j] = image[i][j]
                print(image_new)
                if image_new[i][len(image[0])-1-j] == 0:
                    image_new[i][len(image[0])-1-j] = 1
                else:
                    image_new[i][len(image[0])-1-j] = 0
        return image_new
