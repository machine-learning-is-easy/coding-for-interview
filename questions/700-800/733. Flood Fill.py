
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color: return image
        def fill(image, sr, sc, color, value):
            if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
                return

            if image[sr][sc] != value:
                return
            else:
                image[sr][sc] = color
                fill(image, sr-1, sc, color, value);
                fill(image, sr+1, sc, color, value);
                fill(image, sr, sc-1, color, value);
                fill(image, sr, sc+1, color, value);

        # Run the fill function starting at the position given...
        fill(image, sr, sc, color, image[sr][sc]);
        return image