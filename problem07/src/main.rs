struct Solution;

impl Solution {
    pub fn reverse(x: i32) -> i32 {
        let mut output: i32 = 0;
        let mut x: i32 = x;
        let mut sign: bool = false;
        if (x < 0)
        {
            sign = true;
            x = -x;
        }
        while (x > 0)
        {
            let digit: i32 = x % 10;
            if let Some(new_output) = output.checked_mul(10).and_then(|o| o.checked_add(digit)) {
                output = new_output;
            } else {
                return 0;
            }
            println!("output: {}", output);
            x = x / 10;
        }

        if (output < i32::MIN || output > i32::MAX)
        {
            return 0;
        }

        // print the value of i32::MIN 
        println!("i32::MIN: {}", i32::MAX);

        return if !sign { output } else { -output };
    }
}

fn main() {
    println!("Leet Code Problem 07: Reverse Integer");
    let x: i32 = 1534236469 as i32;
    println!("Input: {}", x);
    let output: i32 = Solution::reverse(x);
    println!("Output: {}", output);
}
