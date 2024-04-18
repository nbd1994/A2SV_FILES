class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # image2 = [img[::-1] for img in image]
        # for img in image2:
        #     for i in range(len(img)):
        #         if img[i]==1:
        #             img[i] = 0
        #         else:
        #             img[i] = 1
        # return image2
        for row in image:
            left = 0
            right = len(row)-1
            while left <= right:
                row[left], row[right] = row[right]^1, row[left]^1
                left+=1
                right-=1
        return image