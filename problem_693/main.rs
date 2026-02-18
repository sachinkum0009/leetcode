/// 693. Binary Number with Alternative Bits
/// 

struct Solution{}

impl Solution {
    pub fn has_alternating_bits(n: i32) -> bool {
        let x = n ^ (n >> 1);
        (x + 1) & (x) == 0
    }
}

fn main() {
    let n = 7;
    let res = Solution::has_alternating_bits(n);
    println!("res: {}", res);
}