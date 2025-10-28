// There is a task management system that allows users to manage their tasks, each associated with a priority. The system should efficiently handle adding, modifying, executing, and removing tasks.

// Implement the TaskManager class:

// TaskManager(vector<vector<int>>& tasks) initializes the task manager with a list of user-task-priority triples. Each element in the input list is of the form [userId, taskId, priority], which adds a task to the specified user with the given priority.

// void add(int userId, int taskId, int priority) adds a task with the specified taskId and priority to the user with userId. It is guaranteed that taskId does not exist in the system.

// void edit(int taskId, int newPriority) updates the priority of the existing taskId to newPriority. It is guaranteed that taskId exists in the system.

// void rmv(int taskId) removes the task identified by taskId from the system. It is guaranteed that taskId exists in the system.

// int execTop() executes the task with the highest priority across all users. If there are multiple tasks with the same highest priority, execute the one with the highest taskId. After executing, the taskId is removed from the system. Return the userId associated with the executed task. If no tasks are available, return -1.

// Note that a user may be assigned multiple tasks.


use std::collections::BinaryHeap;
use std::cmp::Ordering;
use std::collections::HashMap;

#[derive(Eq, PartialEq)]
struct Task {
    user: i32,
    id: i32,
    priority: i32,
}
impl Task {
    fn new(values: Vec<i32>) -> Self {
         Self {
                user: values[0],
                id: values[1],
                priority: values[2],
            }       
        }
}

impl Ord for Task{
    fn cmp(&self, other: &Self) -> Ordering {
        self.priority.cmp(&other.priority)
            .then(self.id.cmp(&other.id))
            .then(self.user.cmp(&other.user))
    }
}
impl PartialOrd for Task{
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(&other))
    }
}
struct TaskManager {
    tasks: BinaryHeap<Task>,
    actions: HashMap<i32, i32>,
    id_to_usr: HashMap<i32, i32>,
}


impl TaskManager {
    fn new(tasks: Vec<Vec<i32>>) -> Self {
        let mut heap = BinaryHeap::new();
        let mut actions = HashMap::new();
        let mut id_to_usr = HashMap::new();
        
        for task in tasks {
            heap.push(Task::new(task.clone()));
            actions.insert(task[1], task[2]);
            id_to_usr.insert(task[1], task[0]);
        }
        
        Self { tasks: heap, actions, id_to_usr }
    }
    
    fn add(&mut self, user_id: i32, task_id: i32, priority: i32) {
        self.tasks.push(Task::new(vec![user_id, task_id, priority]));
        self.actions.insert(task_id, priority);
        self.id_to_usr.insert(task_id, user_id);
    }
    
    fn edit(&mut self, task_id: i32, new_priority: i32) {
        // println!("{}, {}, {}",self.id_to_usr[&task_id], task_id, new_priority);
        self.tasks.push(Task::new(vec![self.id_to_usr[&task_id], task_id, new_priority]));
        self.actions.insert(task_id, new_priority);
    }
    
    fn rmv(&mut self, task_id: i32) {
        self.actions.insert(task_id, -1);
        self.id_to_usr.insert(task_id, -1);
    }
    fn exec_top(&mut self) -> i32 {
        // println!("new!");
        while let Some(mut task) = self.tasks.pop(){
            // println!("{},{},{}", task.user, task.id, task.priority);
            if self.id_to_usr[&task.id] == task.user && self.actions[&task.id] == task.priority{
                self.actions.insert(task.id,-1);
                return task.user
            }
        }
        -1
    }
        
}
