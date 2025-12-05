func countPartitions(nums []int) int {
    guess := 1.0
    x:= 2.0
	for prev_guess :=0.0; guess != prev_guess; guess = guess - (guess*guess - x) / (2*guess){
		prev_guess = guess;
		fmt.Println(guess, prev_guess)
	}
    is_odd := 0
    for _, n := range nums {
        is_odd ^= n % 2
    }
    if is_odd == 1 { return 0 } else { return len(nums) - 1 }
}
