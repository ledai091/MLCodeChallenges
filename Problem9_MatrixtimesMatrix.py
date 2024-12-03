# Multiply two matrices together (return -1 if shapes of matrix dont aline), i.e. C = A dot product B

# Example 1:
#         input: A = [[1,2],
#                     [2,4]], 
#                B = [[2,1],
#                     [3,4]]
#         output:[[ 8,  9],
#                 [16, 18]]
#         reasoning: 1*2 + 2*3 = 8;
#                    2*2 + 3*4 = 16;
#                    1*1 + 2*4 = 9;
#                    2*1 + 4*4 = 18
                    
# Example 2:
#         input: A = [[1,2],
#                     [2,4]], 
#                B = [[2,1],
#                     [3,4],
#                     [4,5]]
#         output: -1
#         reasoning: the length of the rows of A does not equal
#           the column length of B

def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
	if len(a[0]) != len(b):
		return -1
	temp = [[0] * len(b) for _ in range(len(b[0]))]
	for i in range(len(b)):
		for j in range(len(b[0])):
			temp[j][i] = b[i][j]

	c = []
	for i in a:
		list_temp = []
		for j in temp:
			list_temp.append(sum([i[k] * j[k] for k in range(len(i))]))
		c.append(list_temp)
	return c