// You are given a positive integer n, representing an n x n city. You are also given a 2D grid buildings, where buildings[i] = [x, y] denotes a unique building located at coordinates [x, y].

// A building is covered if there is at least one building in all four directions: left, right, above, and below.

// Return the number of covered buildings.
import "fmt"
func countCoveredBuildings(n int, buildings [][]int) int {
    min_col := make([]int,n + 1)
    for i := range min_col{min_col[i] = 6767676}
    max_col := make([]int,n + 1)
    max_row := make([]int,n + 1)
    min_row := make([]int,n + 1)
    for i := range min_row{min_row[i] = 6767676}

    ansa := 0
    for _, building := range buildings{
        a, b := building[0], building[1]
        min_col[b] = min(min_col[b], a)
        max_col[b] = max(max_col[b], a)
        min_row[a] = min(min_row[a], b)
        max_row[a] = max(max_row[a], b)
    } 
    for _, building := range buildings{
        a, b := building[0] , building[1]
        if min_row[a] < b && max_row[a] > b && max_col[b] > a && min_col[b] < a{
            // fmt.Println(a,b)
            ansa ++
        }
    }       
    // fmt.Println(mins,maxs)
    return ansa
}
