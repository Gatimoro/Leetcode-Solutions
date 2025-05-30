impl Solution {
    pub fn closest_meeting_node(edges: Vec<i32>, node1: i32, node2: i32) -> i32 {
        if node1 == node2{
            return node1;
        }
        let mut distances = vec![-1; edges.len()];
        let mut i = node1;
        let mut step = 0;
        while i != -1 && distances[i as usize] == -1{
            distances[i as usize] = step;
            step += 1;
            i = edges[i as usize];
        }
        //println!("{:?}", distances);
        let mut i = node2;
        step = 0;
        let (mut ret, mut shortest_d) = (-1, i32::MAX);
        while i != -1 && distances[i as usize] != -2{
            let cur = step.max(distances[i as usize]);
            //println!("i {}, shortest_d {}, ret {}, cur {}", i, shortest_d, ret, cur);
            
            if distances[i as usize] != -1 && cur < shortest_d{
                (shortest_d, ret) = (cur, i);
            } else if distances[i as usize] != -1 && cur == shortest_d{
                ret = i.min(ret);
            }
            distances[i as usize] = -2;
            step += 1;
            i = edges[i as usize];
        }
        ret
    }
}
