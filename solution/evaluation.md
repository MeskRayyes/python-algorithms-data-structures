
# Algorithm Evaluation: Find First Duplicate

## 1. Problem
Find the first number that appears more than once
when scanning a list from left to right.

## 2. Evaluation Results
Both implementations passed all 8 automated tests.

## 3. Solution A: Nested Loops
- Time Complexity: O(n^2)
- Space Complexity: O(1)
- Strength: Low memory usage.
- Weakness: Slower for large inputs.

## 4. Solution B: Python Set
- Average Time Complexity: O(n)
- Space Complexity: O(n)
- Strength: Faster lookup and better scalability.
- Weakness: Requires additional memory.

## 5. Test Results
- Total tests: 8
- Passed: 8
- Failed: 0

## 6. Final Recommendation
Solution B is preferred for general use because
it provides better average time performance.
Solution A may be useful when minimizing extra
memory is more important.

## 7. Conclusion
Both implementations produce correct results
for the tested scenarios. Solution B offers
better scalability for larger lists.
