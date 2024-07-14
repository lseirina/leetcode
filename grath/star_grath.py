class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        x, y = edges[0][0], edges[0][1]
        if x == edges[1][0] or x == edges[1][1]:
            return x
        else:
            return y

"""В star graph все verteces(nodes) соединяются с одним центральным vertex.
Соответсвенно каждый edge будем содержать этот центральный vertex. Нам надо
найти совпадения хотябы в двух edges.
Мы берем первое и второе число первого edges[0][0] и сравниваем первое число и
с первым и вторым числом воторого edge, если совпадение есть то возвращаем
первое число(vertex) первого edge, если нет то второе"""