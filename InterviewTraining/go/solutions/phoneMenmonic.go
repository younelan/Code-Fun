//go:build problem

package main

var phoneMap = map[byte][]string{
    '0': {"0"},
    '1': {"1"},
    '2': {"A","B","C"},
    '3': {"D","E","F"},
    '4': {"G","H","I"},
    '5': {"J","K","L"},
    '6': {"M","N","O"},
    '7': {"P","Q","R","S"},
    '8': {"T","U","V"},
    '9': {"W","X","Y","Z"},
}

func Solution(phoneNumber string) []string {
    if phoneNumber == "" {
        return []string{}
    }
    res := []string{}
    var b []byte = make([]byte, len(phoneNumber))
    var dfs func(int)
    dfs = func(i int) {
        if i == len(phoneNumber) {
            res = append(res, string(b))
            return
        }
        ch := phoneNumber[i]
        opts := phoneMap[ch]
        for _, s := range opts {
            b[i] = s[0]
            dfs(i+1)
        }
    }
    dfs(0)
    return res
}
