
import sys


def take_input1():
  m,n,h = [int(x) for x in input().split(' ')]
  
  matrix = []
  for i in range(m):
    temp = [int(x) for x in input().split(' ')]
    matrix.append(temp)

  return m,n,h,matrix


def take_input2():
  m,n,h,k = [int(x) for x in input().split(' ')]
  
  matrix = []
  for i in range(m):
    temp = [int(x) for x in input().split(' ')]
    matrix.append(temp)

  return m,n,h,k,matrix

def ALG1():

  m,n,h,matrix = take_input1()
  result = [0 ,0, 0, 0]
  
  #Traversing through matrix
  for start_r in range(m):
    for start_col in range(n):

      # If no of trees in plot>=h, traverse through all squares starting from that plot
      if(matrix[start_r][start_col]>=h):
        end_r,end_col = start_r,start_col
        while (end_r< m and end_col<n):      
            flag = True

            #Traversing through square area to check whether every plot has no of trees >=h
            for i in range(start_r,end_r+1):
              for j in range(start_col, end_col+1):
                if matrix[i][j]>=h:
                  continue
                else:
                  flag = False
            
            #updating latest max square area
            if flag==True:
              temp = [start_r,start_col,end_r,end_col]
              temp_area = (end_r-start_r)*(end_col-start_col)
              max_area = (result[2]-result[0])*(result[3]- result[1])
              if max_area<temp_area:
                result= temp

            end_r+=1
            end_col+=1
  result  = [x + 1 for x in result]   
  return result


def ALG2():
  m,n,h,matrix = take_input1()
  result = [0 ,0, 0, 0]

  #Traversing through matrix
  for start_r in range(m):
    for start_col in range(n):

      '''
       # If no of trees in plot>=h, increasing square plot size by one r and one column
       # and checking no of trees in only newly added r and col
       '''

      if(matrix[start_r][start_col]>=h):
        flag = True
        square_size= 0
        end_r,end_col = start_r,start_col
        while (end_r< m and end_col<n and flag):

          for j in range(start_col,end_col+1):
            if matrix[end_r][j] < h:
              flag = False
              break
            
          for i in range(start_r,end_r+1):
            if matrix[i][end_col] < h:
              flag=False
              break

          #updating latest max square area    
          if flag==True:
            temp = [start_r,start_col,end_r,end_col]
            temp_area = (end_r-start_r)*(end_col-start_col)
            max_area = (result[2]-result[0])*(result[3]- result[1])
            if max_area<temp_area:
              result= temp
            
            end_r,end_col = start_r+square_size,start_col+square_size
            square_size+=1

  result  = [x + 1 for x in result]        
  return result


def ALG3():
  m,n,h,matrix = take_input1()
  result = [0 ,0, 0, 0]
  
  #create matrix to store sqaure_size 
  square_size = [[0 for x in range(n+1)] for x in range(m+1)]
  max_square = 0

  #Traversing through matrix
  for end_r in range(1,m+1):
    for end_col in range(1,n+1):
      if(matrix[end_r-1][end_col-1]>=h):
        square_size[end_r][end_col] = min(square_size[end_r-1][end_col],square_size[end_r-1][end_col-1],square_size[end_r][end_col-1])+1
        if(square_size[end_r][end_col]>max_square):
          max_square = square_size[end_r][end_col]
          result = [end_r-max_square+1, end_col-max_square+1,end_r,end_col]

  return result


def ALG4():

  m,n,h,matrix = take_input1()
  result = [0 ,0, 0, 0]

  dp = [[[0 for k in range(n+1)] for j in range(n+1)] for i in range(m+1)]
  max_square = 0
  
  for r in range(1,m+1):
    for c1 in range(1,n+1):
      val = 1 if matrix[r-1][c1-1] < h else 1+dp[r-1][c1][c1]
      for c2 in range(c1,n+1):
        dp[r][c1][c2] = 1 if val == 1 else 1+dp[r-1][c1][c2]
        temp_sq = dp[r-1][c1][c2] + 1 if c2-c1+1 == dp[r-1][c1][c2] + 1 else 1
        if(temp_sq > max_square):
          max_square = temp_sq
          result = [r-max_square+1,c2-max_square+1, r,c2]
        if matrix [r-1][c2-1] < h and c1!=c2:
          dp[r][c1][c2] = 1
          break
  return result

def ALG5A():
    m, n, h, matrix = take_input1()
    def TopLeftCorner(matrix, dpD, r, c, h):
        # Check if element is 0
        if matrix[r][c] < h:
            dpD[r][c] = 1
        elif matrix[r][c-1] < h or matrix[r-1][c] < h:
            dpD[r][c] = 1
        else:
            if dpD[r][c-1] == -1:
                    TopLeftCorner(matrix, dpD, r, c-1, h)
            if dpD[r-1][c] == -1:
                    TopLeftCorner(matrix, dpD, r-1, c, h)
            if dpD[r-1][c-1] == -1:
                    TopLeftCorner(matrix, dpD, r-1, c-1, h)
            dpD[r][c] = min(dpD[r][c-1], dpD[r-1][c], dpD[r-1][c-1])+1

    def TopRightCorner(matrix, dpR, r, c, h):
            # Check if element is 0
            if matrix[r][c] < h:
                dpR[r][c] = 1
            elif matrix[r-1][c-1] < h or matrix[r][c-1] < h:
                dpR[r][c] = 1
            else:
                if dpR[r][c-1] == -1:
                        TopLeftCorner(matrix, dpR, r, c-1, h)
                if dpR[r-1][c] == -1:
                        TopLeftCorner(matrix, dpR, r-1, c, h)
                if dpR[r-1][c-1] == -1:
                        TopLeftCorner(matrix, dpR, r-1, c-1, h)
                dpR[r][c] = min(dpR[r][c-1], dpR[r-1][c], dpR[r-1][c-1])+1

    def BottomLeftCorner(matrix, dpL, r, c, h):
            # Check if element is 0
            if matrix[r][c] < h:
                dpL[r][c] = 1
            elif matrix[r-1][c-1] < h or matrix[r-1][c] < h:
                dpL[r][c] = 1
            else:
                if dpL[r][c-1] == -1:
                        TopLeftCorner(matrix, dpL, r, c-1, h)
                if dpL[r-1][c] == -1:
                        TopLeftCorner(matrix, dpL, r-1, c, h)
                if dpL[r-1][c-1] == -1:
                        TopLeftCorner(matrix, dpL, r-1, c-1, h)
                dpL[r][c] = min(dpL[r][c-1], dpL[r-1][c], dpL[r-1][c-1])+1
    rs, cs = len(matrix), len(matrix[0]) if len(matrix) > 0 else 0
    dp = [[0]*cs for _ in range(rs)]
    dpR = [[-1]*cs for _ in range(rs)]
    dpD = [[-1]*cs for _ in range(rs)]
    dpL = [[-1]*cs for _ in range(rs)]

    for i in range(rs):
        for j in range(cs):
            if i==0 or j==0:
                dp[i][j] = 1
                dpD[i][j] = 1
                dpR[i][j] = 1
                dpL[i][j] = 1
            else:
                if dpD[i-1][j-1] == -1:
                    TopLeftCorner(matrix, dpD, i-1, j-1, h)
                if dpR[i-1][j] == -1:
                    TopRightCorner(matrix, dpR, i-1, j, h)
                if dpL[i][j-1] == -1:
                    BottomLeftCorner(matrix, dpL, i, j-1, h)
                dp[i][j] = min(dpD[i-1][j-1], dpR[i-1][j], dpL[i][j-1])+1
    
    maxSquareSize = 0
    for r in range(len(dp)):
        for c in range(len(dp[0])):
            if dp[r][c] >= maxSquareSize:
                maxSquareSize = dp[r][c]
                max_square = dp[r][c]
                result = [r-max_square + 1, c - max_square + 1,r,c]
    result  = [x + 1 for x in result]  
    return result


# Task 5B - Bottom Up DP for Problem 2 in O(mn)
def ALG5B():
  m,n,h,matrix = take_input1()
  rows, cols = m,n if len(matrix) > 0 else 0

  # Pad original matrix with 0's for simplicity
  for i in range(rows):
      matrix[i].insert(0,0)
  matrix.insert(0,[0 for i in range(cols+1)])

  dp = [[0] * (cols + 1) for _ in range(rows + 1)]
  dpT = [[0] * (cols + 1) for _ in range(rows + 1)]
  dpL = [[0] * (cols + 1) for _ in range(rows + 1)]
  dpD = [[0] * (cols + 1) for _ in range(rows + 1)]

  for i in range(1, rows+1):
      for j in range(1, cols+1):
          if i == 1 or j == 1:
              dpT[i][j] = 1
          else:
              if matrix[i][j] < h:
                  dpT[i][j] = 1
              elif matrix[i-1][j-1] < h or matrix[i][j-1] < h:
                  dpT[i][j] = 1
              else:
                  dpT[i][j] = min(dpT[i][j-1], dpT[i-1][j], dpT[i-1][j-1])+1
  
  for i in range(1, rows+1):
      for j in range(1, cols+1):
          if i == 1 or j == 1:
              dpL[i][j] = 1
          else:
              if matrix[i][j] < h:
                  dpL[i][j] = 1
              elif matrix[i-1][j-1] < h or matrix[i-1][j] < h:
                  dpL[i][j] = 1
              else:
                  dpL[i][j] = min(dpL[i][j-1], dpL[i-1][j], dpL[i-1][j-1])+1

  for i in range(1, rows+1):
      for j in range(1, cols+1):
          if i == 1 or j == 1:
              dpD[i][j] = 1
          else:
              if matrix[i][j] < h:
                  dpD[i][j] = 1
              elif matrix[i][j-1] < h or matrix[i-1][j] < h:
                  dpD[i][j] = 1
              else:
                  dpD[i][j] = min(dpD[i][j-1], dpD[i-1][j], dpD[i-1][j-1])+1
  
  maxSquareSize = 0
  result = [0,0,0,0]
  for r in range(1, rows+1):
      for c in range(1, cols+1):
          if r == 1 or c == 1:
              dp[r][c] = 1
          else:
              dp[r][c] = min(dpD[r-1][ c-1], dpT[r-1][c], dpL[r][c-1])+1
          if dp[r][c] >= maxSquareSize:
              maxSquareSize = dp[r][c]
              max_square = dp[r][c]
              result = [r-max_square + 1, c - max_square + 1,r,c]
  return result


def ALG6():
  m,n,h,k,matrix = take_input2()
  result = [0,0,0,0]
  #Traversing through matrix
  for start_r in range(m):
    for start_col in range(n):

      #traverse through all squares starting from the plot
      increament = 1
      end_r,end_col = start_r,start_col
      
      while (end_r< m and end_col<n):      
          count = 0

          #Traversing through square area and keeping count of plot where no of trees<h
          for i in range(start_r,end_r+1):
            for j in range(start_col, end_col+1):
              if matrix[i][j]>=h:
                continue
              
              else:
                count+=1
                
          
          #updating latest max square area
          if count<=k:
            temp = [start_r,start_col,end_r,end_col]
            temp_area = (end_r-start_r)*(end_col-start_col)
            max_area = (result[2]-result[0])*(result[3]- result[1])
            if max_area<temp_area:
              result= temp
          end_r+=increament
          end_col+=increament
  result  = [x + 1 for x in result] 
  return result
def getDpRow(m,n,k,h,arr):
  dpRow = [[[0 for x in range(k+1)] for j in range(m+1)] for i in range(n+1)]
  for i in range(1,m+1):
    for j in range(1,n+1):
      for k1 in range(0,k+1):
        if(arr[i][j] == k1):
          dpRow[i][j][k1] = 1
        if(dpRow[i][j-1][k1-arr[i][j]] !=0):
          dpRow[i][j][k1] = 1+dpRow[i][j-1][k1-arr[i][j]]
  return dpRow

def getDpCol(m,n,k,h,arr):
  dpCol = [[[0 for x in range(k+1)] for j in range(m+1)] for i in range(n+1)]
  for i in range(1,m+1):
    for j in range(1,n+1):
      for k1 in range(0,k+1):
        if(arr[i][j] == k1):
          dpCol[i][j][k1] = 1
        if(dpCol[i-1][j][k1-arr[i][j]] !=0):
          dpCol[i][j][k1] = 1+dpCol[i-1][j][k1-arr[i][j]]
  return dpCol

def preproces(m,n,k,h,arr):
  presum = [[0 for j in range(m+1)] for i in range(n+1)]
  for i in range(1,m+1):
    for j in range(1,n+1):
      presum[i][j] = arr[i][j]+presum[i][j-1]
  
  for i in range (2,m+1):
    for j in range(1, n+1):
      presum[i][j] += presum[i-1][j]
  
  return presum

def getSumMatrixSum(r1,c1,r2,c2,presum):
  return presum[r2][c2]-presum[r2][c1-1]-presum[r1-1][c2]+presum[r1-1][c1-1]
  

def isValid(side,r,c):
  return True if side <= min(r,c) else False

def bin_matrix(m,n,h,matrix):
  matrix_temp = [[0 for j in range(m+1)] for i in range(n+1)]
  for r in range(1,m):
    for c in range(1,n):
      if(matrix[r-1][c-1]<h):
        matrix_temp[r][c]=0
      else:
        matrix_temp[r][c]=1
  return matrix_temp

def ALG7A():
  m,n,h,k,matrix = take_input2()
  new_mat = bin_matrix(m,n,h,matrix)
  dpRow = getDpRow(m,n,k,1,new_mat)
  dpCol = getDpCol(m,n,k,1,new_mat)
  preSum = preproces(m,n,k,1,new_mat)
  dp = [[[0 for x in range(k+1)] for j in range(m+1)] for i in range(n+1)]
  res = 0

  for i in range(1,m+1):
      for j in range(1,n+1):
        possibleSides = []
        for item in dpRow[i][j-1]:
          possibleSides.append(item)
        for item in dpCol[i-1][j]:
          possibleSides.append(item)
        for item in dp[i-1][j-1]:
          possibleSides.append(item)
        
        for side in possibleSides:
          if(isValid(side,i,j)):
            totalSum = getSumMatrixSum(i-side+1,j-side+1,i,j,preSum)
            if(totalSum <=k):
              dp[i][j][totalSum] = max(dp[i][j][totalSum],side)
              if(side > res):
                res = side
                result = [res,i,j]
  
  output = [i-res+1,j-res+1,i,j]
  return output

if __name__ == "__main__":
  # Invoking tasks

  if sys.argv[1] == "ALG1":
      output = ALG1()
  elif sys.argv[1] == "ALG2":
      output = ALG2()
  elif sys.argv[1] == "ALG3":
      output = ALG3()
  elif sys.argv[1] == "ALG4":
      output = ALG4()
  elif sys.argv[1] == "ALG5A":
      output = ALG5A()
  elif sys.argv[1] == "ALG5B":
      output = ALG5B()
  elif sys.argv[1] == "ALG6":
      output = ALG6()
  elif sys.argv[1] == "ALG7A":
      output = ALG7A()
  
  print(" ".join(str(element) for element in output))