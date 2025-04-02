impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack = Vec::new();
        for ch in s.chars(){
            match ch{
                ')' => {
                    let pair = stack.pop();
                    match pair{
                        Some(pair) => {
                            if pair != '(' {return false}
                        }
                        None => return false
                    }
                } 
                '}' => {
                    let pair = stack.pop();
                    match pair{
                        Some(pair) => {
                            if pair != '{'{return false}
                        }
                        None => return false
                    }
                } 
                ']' => {
                    let pair = stack.pop();
                    match pair{
                        Some(pair) => {
                            if pair != '[' {return false}
                        }
                        None => return false
                    }
                } 
                '(' | '[' | '{' => stack.push(ch),
                
                _ => {}

            }
        }
        stack.is_empty()

        
        
    }
}



"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type."""
