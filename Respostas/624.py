class Solution(object):
    def maxDistance(self, arrays):
        minimo = arrays[0][0]
        maximo = arrays[0][-1]
        result = 0

        for i in range(1, len(arrays)):
            cur_min = arrays[i][0]
            cur_max = arrays[i][-1]
            result = max(result, abs(cur_max - minimo), abs(maximo - cur_min))
            minimo = min(minimo, cur_min)
            maximo = max(maximo, cur_max)

        return result
