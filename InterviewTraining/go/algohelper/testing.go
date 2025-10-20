package algohelper

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"path/filepath"
)

// LoadTests reads the JSON test file for moduleName from ../tests/<moduleName>.json
// It returns the raw unmarshalled slice of objects so callers can interpret fields.
func LoadTests(moduleName string) ([]map[string]interface{}, error) {
	// Try several likely relative locations for the tests directory so the
	// runner can be executed from `go/` or `go/problems/` and still find tests.
	candidates := []string{
		filepath.Join("tests", fmt.Sprintf("%s.json", moduleName)),
		filepath.Join("..", "tests", fmt.Sprintf("%s.json", moduleName)),
		filepath.Join("..", "..", "tests", fmt.Sprintf("%s.json", moduleName)),
		filepath.Join("..", "..", "..", "tests", fmt.Sprintf("%s.json", moduleName)),
	}
	var data []byte
	var err error
	for _, c := range candidates {
		data, err = ioutil.ReadFile(c)
		if err == nil {
			break
		}
	}
	if err != nil {
		return nil, err
	}
	var arr []map[string]interface{}
	if err := json.Unmarshal(data, &arr); err != nil {
		return nil, err
	}
	return arr, nil
}
