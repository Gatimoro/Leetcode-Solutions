// There is an undirected tree with n nodes labeled from 0 to n - 1. You are given the integer n and a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

// You are also given a 0-indexed integer array values of length n, where values[i] is the value associated with the ith node, and an integer k.

// A valid split of the tree is obtained by removing any set of edges, possibly empty, from the tree such that the resulting components all have values that are divisible by k, where the value of a connected component is the sum of the values of its nodes.

// Return the maximum number of components in any valid split.

func maxKDivisibleComponents(n int, edges [][]int, values []int, k int) int {
    graph := make([][]int, n)
    for i := range graph {
        graph[i] = []int{}
    }
    visited := make([]bool, n)
    
    for _, ft := range edges{
        graph[ft[0]] = append(graph[ft[0]], ft[1])
        graph[ft[1]] = append(graph[ft[1]], ft[0])
    }
    var dfs func(edge int) int
    splits := 0
    dfs = func(edge int) int{
        visited[edge] = true
        for _, nei := range graph[edge]{
            if visited[nei]{continue}
            values[edge] += dfs(nei)
        }
        values[edge] %= k
        if values[edge] == 0{
            splits += 1
        }
        return values[edge]
    }
    dfs(0)
    return splits
}
