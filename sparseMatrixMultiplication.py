from typing import List

class Solution:
    # TC : O(m * k + k * n)
    # SC : O(m*n)
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        
        def create_sparse_matrix(matrix: List[List[int]]) -> List[List[tuple]]:
            
            sparse_matrix = [[] for _ in range(len(matrix))]
            for row_index, row in enumerate(matrix):
                for col_index, value in enumerate(row):
                    if value:
                        # Append a tuple containing the column index and the value if non-zero
                        sparse_matrix[row_index].append((col_index, value))
            return sparse_matrix
      
        # Create the sparse matrix representations for both input matrices
        sparse_mat1 = create_sparse_matrix(mat1)
        sparse_mat2 = create_sparse_matrix(mat2)
      
        # Get the dimensions for the resulting matrix
        m, n = len(mat1), len(mat2[0])
      
        # Initialize the resulting matrix with zeros
        result_matrix = [[0] * n for _ in range(m)]
      
        # Iterate through each row of mat1
        for i in range(m):
            # Iterate through the sparse representation of the row from mat1
            for col_index_mat1, value_mat1 in sparse_mat1[i]:
                # For non-zero elements in mat1's row, iterate through the corresponding row in mat2
                for col_index_mat2, value_mat2 in sparse_mat2[col_index_mat1]:
                    # Multiply and add to the resulting matrix
                    result_matrix[i][col_index_mat2] += value_mat1 * value_mat2
                  
        # Return the resulting matrix after multiplication
        return result_matrix