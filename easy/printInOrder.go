// Suppose we have a class:

// public class Foo {
//   public void first() { print("first"); }
//   public void second() { print("second"); }
//   public void third() { print("third"); }
// }
// The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().

// Note:

// We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seem to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.

 
type Foo struct {
    ch1 chan int
    ch2 chan int
}

func NewFoo() *Foo {
	return &Foo{
        ch1: make(chan int),
        ch2: make(chan int),
	}

}

func (f *Foo) First(printFirst func()) {
	// Do not change this line
	printFirst()
    f.ch1 <- 1
}

func (f *Foo) Second(printSecond func()) {
    <- f.ch1
	/// Do not change this line
	printSecond()
    f.ch2 <- 1
}

func (f *Foo) Third(printThird func()) {
	// Do not change this line
    <- f.ch2
	printThird()
}
