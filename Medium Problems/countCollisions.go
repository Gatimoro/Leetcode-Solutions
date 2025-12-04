// There are n cars on an infinitely long road. The cars are numbered from 0 to n - 1 from left to right and each car is present at a unique point.

// You are given a 0-indexed string directions of length n. directions[i] can be either 'L', 'R', or 'S' denoting whether the ith car is moving towards the left, towards the right, or staying at its current point respectively. Each moving car has the same speed.

// The number of collisions can be calculated as follows:

// When two cars moving in opposite directions collide with each other, the number of collisions increases by 2.
// When a moving car collides with a stationary car, the number of collisions increases by 1.
// After a collision, the cars involved can no longer move and will stay at the point where they collided. Other than that, cars cannot change their state or direction of motion.

// Return the total number of collisions that will happen on the road.
func countCollisions(directions string) int {
    first_valid := 0
    last_valid := len(directions)-1
    var d = []rune(directions)
    for first_valid <= last_valid{
        if d[first_valid] == 'L'{
            first_valid++
        }else if d[last_valid] == 'R'{
            last_valid--
        }else{
            break
        }
    }
    total := 0
    m := map[bool]int{true: 1, false: 0}
    for i := first_valid; i <= last_valid; i, total = i+1, total+m[d[i] != 'S'] {}
    return total
}
