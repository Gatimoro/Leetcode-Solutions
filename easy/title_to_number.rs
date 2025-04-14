impl Solution {
    pub fn title_to_number(column_title: String) -> i32{
        
        column_title.chars().fold(0, | acc, x | acc * 26 + (x as i32 - 'A' as i32 + 1))
    }
}
// Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

// For example:

// A -> 1
// B -> 2
// C -> 3
// ...
// Z -> 26
// AA -> 27
// AB -> 28 
// ...
 
