// You are given a string word, and an integer numFriends.

// Alice is organizing a game for her numFriends friends. There are multiple rounds in the game, where in each round:

// word is split into numFriends non-empty strings, such that no previous round has had the exact same split.
// All the split words are put into a box.
// Find the lexicographically largest string from the box after all the rounds are finished.

 
impl Solution {
    pub fn answer_string(word: String, num_friends: i32) -> String {
        if num_friends == 1 {
            return word;
        }

        let n = word.len();
        let k = num_friends as usize;
        let bytes = word.as_bytes();
        let mut max_char = b'a';
        let mut result = "";

        let max_window = n - k + 1;

        for i in 0..n {
            let ch = bytes[i];
            if ch >= max_char {
                max_char = ch;

                let end = (i + max_window).min(n);
                let candidate = &word[i..end];
                if candidate > result {
                    result = candidate;
                }
            }
        }

        result.to_string()
    }
}
