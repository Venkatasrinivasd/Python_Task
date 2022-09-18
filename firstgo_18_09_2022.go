package main

import ("fmt")
func main() {
	fmt.Println("Hello World!")
	var student1 string = "John" //type is string
	var student2 = "Jane"        //type is inferred
	x := 2                       //type is inferred
	y := 4

	fmt.Println(student1)
	fmt.Println(student2)
	fmt.Println(x + y) // addition
	fmt.Println(x - y) // sub
	fmt.Println(x * y) // mul
	fmt.Println(x / y) // div
	fmt.Println(x % y) // mod
	x++                // unary operator
	fmt.Println(x)
	y--
	fmt.Println(y)

}
