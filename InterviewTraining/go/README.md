Go port of the InterviewTraining runner and helpers.

Usage:
- Register your solution(s) by calling `registry.Register("moduleName", value)` from an init() in your solution file.
- From the repository root run: `cd go && go run testrun.go <moduleName>`

Notes:
- This is an initial port of the JS `testrun.js` and `AlgoHelper` utilities. It supports loading test JSON files from `../tests` and basic list/tree/graph builders.
