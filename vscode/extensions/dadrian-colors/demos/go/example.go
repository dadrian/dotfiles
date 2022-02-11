package main

import (
	"fmt"
	"time"
)

// MyStruct is a struct that does things.
type MyStruct struct {
	String        string
	Value         interface{}
	Number        int
	Unsigned      uint64 `json:"hello"`
	ErrorVariable TypeDoesNotExist
}

func MyFunction() string {
	return "Hello, world!\n"
}

func main() {
	fmt.Println(MyFunction())
	s := MyStruct{
		String:   "a string",
		Value:    time.Now(),
		Number:   -678,
		Unsigned: 0x345,
	}
	if len(s.String) > 10 {
		fmt.Println('c')
	}
	fmt.Printf("%v\n", s)
}
