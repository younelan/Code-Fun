# JavaScript Interview Challenges

## Running Tests

### Single Challenge
```bash
node testrun.js <challengeName>
```

Example:
```bash
node testrun.js binarySearch
```

### All Challenges
```bash
chmod +x runall
./runall
```

## Available Challenges

### Array Manipulation
- **binarySearch**: Implement binary search in a sorted array [O(log n)]
- **3sum**: Find three numbers that sum to zero [O(n²)]
- **firstDuplicateValue**: Find first value that appears twice [O(n)]
- **isMonotonic**: Check if array is monotonically increasing/decreasing [O(n)]
- **largestRange**: Find largest range of consecutive integers [O(n)]
- **longestPeak**: Find longest peak sequence in array [O(n)]
- **mergeIntervals**: Merge overlapping intervals [O(n log n)]
- **productArray**: Array of products excluding current index [O(n)]
- **smallestDifference**: Find smallest difference between two arrays [O(n log n)]
- **spiralTraverse**: Print 2D array in spiral order [O(n)]
- **subarraySort**: Find smallest subarray to sort [O(n)]

### String Manipulation
- **caesarCipherEncryptor**: Implement Caesar cipher [O(n)]
- **generateDocument**: Can you make this document from given characters? [O(n)]
- **generateIPAddresses**: Generate all valid IP addresses from string [O(1)]
- **matrix_str_search**: Search string in 2D matrix [O(n*m)]
- **minCharsForWords**: Minimum chars needed to form words [O(n*k)]
- **phoneMnemonic**: Generate letter combinations from phone number [O(4^n)]
- **runLengthEncoding**: Basic string compression [O(n)]

### Trees & Graphs
- **binarySearchTreeHeight**: Get height of BST [O(n)]
- **branchSums**: Sum of all root-to-leaf paths [O(n)]
- **bstInsertRemove**: Basic BST operations [O(log n)]
- **depthFirstSearch**: Implement DFS for graph [O(v + e)]
- **minHeightBst**: Create minimum height BST [O(n)]
- **validateBst**: Check if tree is valid BST [O(n)]

### Linked Lists
- **linkedListCycle**: Detect cycle in linked list [O(n)]
- **linkedListDupe**: Remove duplicates from sorted list [O(n)]

### Dynamic Programming & Others
- **classPhotos**: Arrange students in two rows [O(n log n)]
- **minWaitTime**: Minimize query waiting time [O(n log n)]
- **ransomNote**: Can you create note from magazine? [O(n)]
- **tandemBicycle**: Optimize bicycle pair speeds [O(n log n)]

## Writing Custom Tests

Tests are defined in JSON files under `../tests/`. Example format:
```json
[
    {
        "testType": "function",
        "functionName": "binarySearch",
        "input": [[1, 2, 3, 4], 3],
        "expect": 2
    }
]
```

## Test Types
- `function`: Standard function test
- `tree`: Binary tree operations
- `list`: Linked list operations
- `graph`: Graph operations
