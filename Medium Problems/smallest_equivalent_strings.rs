// You are given two strings of the same length s1 and s2 and a string baseStr.

// We say s1[i] and s2[i] are equivalent characters.

// For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.
// Equivalent characters follow the usual rules of any equivalence relation:

// Reflexivity: 'a' == 'a'.
// Symmetry: 'a' == 'b' implies 'b' == 'a'.
// Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
// For example, given the equivalency information from s1 = "abc" and s2 = "cde", "acd" and "aab" are equivalent strings of baseStr = "eed", and "aab" is the lexicographically smallest equivalent string of baseStr.

// Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2.


impl Solution {
    pub fn smallest_equivalent_string(s1: String, s2: String, base_str: String) -> String {
        let mut parent: Vec<usize> = (0..26).collect();
        fn get_dad(letter: usize, parent: &mut Vec<usize>) -> usize{
            if parent[letter] != parent[parent[letter]]{
                parent[letter] = get_dad(parent[letter], parent);
            }
            parent[letter]
        }
        fn union(u1: usize, u2: usize, parent: &mut Vec<usize>) {
            let p1 = get_dad(u1, parent);
            let p2 = get_dad(u2, parent);
            if p1 <= p2{
                parent[p2] = p1;
            }else{
                parent[p1] = p2;
            }
        }
        for (l1, l2) in s1.bytes().zip(s2.bytes()){
            let(letter1, letter2) = ((l1 - b'a') as usize, (l2 - b'a') as usize);
            union(letter1, letter2, &mut parent);
        }       
        base_str.bytes().map(|x| (b'a' + get_dad((x - b'a') as usize, &mut parent) as u8) as char).collect()
    }
}
