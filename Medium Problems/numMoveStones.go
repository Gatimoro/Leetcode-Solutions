// There are three stones in different positions on the X-axis. You are given three integers a, b, and c, the positions of the stones.

// In one move, you pick up a stone at an endpoint (i.e., either the lowest or highest position stone), and move it to an unoccupied position between those endpoints. Formally, let's say the stones are currently at positions x, y, and z with x < y < z. You pick up the stone at either position x or position z, and move that stone to an integer position k, with x < k < z and k != y.

// The game ends when you cannot make any more moves (i.e., the stones are in three consecutive positions).

// Return an integer array answer of length 2 where:

// answer[0] is the minimum number of moves you can play, and
// answer[1] is the maximum number of moves you can play.
 
import "fmt"
func numMovesStones(a int, b int, c int) []int {
    ansa := make([]int, 2)
    //for min
	na := min(a,b,c)
	nc := max(a,b,c)
	nb := a + b + c - na - nc
	ab, bc := nb - na, nc - nb
    fmt.Println(na,nb,nc)

    if ab == bc && bc == 1{
		ansa[0] = 0
	}else if ab <= 2 || bc <= 2{
		ansa[0] = 1
	}else{
		ansa[0] = 2
	}

	ansa[1] = ab + bc - 2
	return ansa
}
