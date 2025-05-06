//The task was to design a linked list :)
struct Node {
    val: i32,
    next: Option<Box<Node>>,
}

impl Node {
    fn with_value(val: i32) -> Self {
        Node { val, next: None }
    }
}

struct MyLinkedList {
    length: i32,
    head: Option<Box<Node>>,
}

impl MyLinkedList {
    fn new() -> Self {
        MyLinkedList {
            length: 0,
            head: None,
        }
    }

    fn valid(&self, index: i32) -> bool {
        index >= 0 && index < self.length
    }

    fn get(&self, index: i32) -> i32 {
        if !self.valid(index) {
            return -1;
        }
        let mut node = self.head.as_ref();
        for _ in 0..index {
            node = node.unwrap().next.as_ref();
        }
        node.unwrap().val
    }

    fn add_at_head(&mut self, val: i32) {
        let mut news = Box::new(Node::with_value(val));
        news.next = self.head.take();
        self.head = Some(news);
        self.length += 1;
    }

    fn add_at_tail(&mut self, val: i32) {
        let mut new = Box::new(Node::with_value(val));
        if self.length == 0 {
            self.head = Some(new);
        } else {
            let mut cur = self.head.as_mut().unwrap();
            while let Some(ref mut next) = cur.next {
                cur = next;
            }
            cur.next = Some(new);
        }
        self.length += 1;
    }

    fn add_at_index(&mut self, index: i32, val: i32) {
        if index == 0 {
            self.add_at_head(val);
        } else if index == self.length{
            self.add_at_tail(val);
        }else if self.valid(index) {
            let mut cur = self.head.as_mut().unwrap();
            for _ in 1..index {
                cur = cur.next.as_mut().unwrap();
            }
            let mut new = Box::new(Node::with_value(val));
            new.next = cur.next.take();
            cur.next = Some(new);
            self.length += 1;
        }
    }

    fn delete_at_index(&mut self, index: i32) {
        if !self.valid(index) {
            return;
        }
        if index == 0 {
            self.head = self.head.take().and_then(|x| x.next);
        } else {
            let mut curr = self.head.as_mut().unwrap();
            for _ in 1..index {
                curr = curr.next.as_mut().unwrap();
            }
            let next_next = curr.next.as_mut().and_then(|x| x.next.take());
            curr.next = next_next;
        }
        self.length -= 1;
    }
}
