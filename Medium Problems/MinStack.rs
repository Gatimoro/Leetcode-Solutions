struct MinStack {
    stack: Vec<i32>,
    minima: Vec<i32>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MinStack {

    fn new() -> Self {
        MinStack{
            stack : Vec::new(),
            minima : Vec::new(),
        }
    }
    
    fn push(&mut self, val: i32) {
        self.stack.push(val);
        if self.minima.is_empty() || self.minima[self.minima.len() - 1] >= val{
            self.minima.push(val);
        }
    }
    
    fn pop(&mut self) {
        if self.stack.pop().unwrap() == self.minima[self.minima.len() - 1]{
            self.minima.pop();
        }
    }
    
    fn top(&self) -> i32 {
        self.stack[self.stack.len() - 1]
    }
    
    fn get_min(&self) -> i32 {
        self.minima[self.minima.len() - 1]
    }
}
// Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

// Implement the MinStack class:

// MinStack() initializes the stack object.
// void push(int val) pushes the element val onto the stack.
// void pop() removes the element on the top of the stack.
// int top() gets the top element of the stack.
// int getMin() retrieves the minimum element in the stack.
// You must implement a solution with O(1) time complexity for each function.
