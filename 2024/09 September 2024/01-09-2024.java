/*
Author : Shuvam Kumar Singh
Date : 01/09/2024
Problem : 2022. Convert 1D Array Into 2D Array
Difficulty : Easy
*/
  
class Solution {
    public int[][] construct2DArray(int[] original, int m, int n) {
        if (m * n != original.length) return new int[0][0];
        int[][] ans = new int[m][n];
        
        for (int i = 0; i < original.length; i++) {
            ans[i / n][i % n] = original[i];
        }
        
        return ans;
    }
}
