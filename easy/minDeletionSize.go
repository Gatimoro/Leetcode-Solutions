// You are given an array of n strings strs, all of the same length.

// The strings can be arranged such that there is one on each line, making a grid.

// For example, strs = ["abc", "bce", "cae"] can be arranged as follows:
// abc
// bce
// cae
// You want to delete the columns that are not sorted lexicographically. In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted, while column 1 ('b', 'c', 'a') is not, so you would delete column 1.

// Return the number of columns that you will delete.
func minDeletionSize(strs []string) int {
    invalid := make([]bool, len(strs[0]))
    last_word := strs[0]
    for c, word := range strs{
        for i := range word{
            if c > 0 && word[i] < last_word[i] {invalid[i] = true}
        }
        last_word = word
    }
    ansa := 0
    for _, v := range invalid{
        if v{ansa++}
    }
    return ansa
}
