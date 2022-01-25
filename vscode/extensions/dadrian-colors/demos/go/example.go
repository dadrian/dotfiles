package main

import (
	"fmt"
	"time"
)

type MyStruct struct {
	String   string
	Value    interface{}
	Number   int
	Unsigned uint64
}

func myFunction() string {
	return "Hello, world!\n"
}

func main() {
	fmt.Println(myFunction())
	s := MyStruct{
		String:   "a string",
		Value:    time.Now(),
		Number:   -678,
		Unsigned: 0x345,
	}
	fmt.Printf("%v\n", s)
}
