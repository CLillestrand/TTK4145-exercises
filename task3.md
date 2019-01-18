# Reasons for concurrency and parallelism


To complete this exercise you will have to use git. Create one or several commits that adds answers to the following questions and push it to your groups repository to complete the task.

When answering the questions, remember to use all the resources at your disposal. Asking the internet isn't a form of "cheating", it's a way of learning.

 ### What is concurrency? What is parallelism? What's the difference?
 > *Concurrency is when multiple tasks are running in overlapping time periods but not at the exact same time.
 Parallellism is when tasks are running at the exact same time due to several processors*
 
 ### Why have machines become increasingly multicore in the past decade?
 > *Because it allows you to run tasks in parallel when the relevant. Wash, dry and fold example.
 Two processors if cooperating can do tasks faster than a single processor with
 the same specifications*
 
 ### What kinds of problems motivates the need for concurrent execution?
 (Or phrased differently: What problems do concurrency help in solving?)
 > *It helps solving problems where we have multiple tasks, and it helps intuition.
 Lets say you want to play a composition containing a piano and a violin, if
 you do it yourself by reading a sheet with the notes in chronological order it
 gets hard really fast. But if you are able to split yourself in two it will be easier.
 The violin half of you only need the violin notes and piano you only needs the piano notes.
 Its easier doing and understanding one thing than a combination of two* 
 
 ### Does creating concurrent programs make the programmer's life easier? Harder? Maybe both?
 (Come back to this after you have worked on part 4 of this exercise)
 > *It can make it harder when it comes to the use of recourses, like if two treads try
 to access the same variable. Easier because it divides bigger tasks into understandable
 parts*
 
 ### What are the differences between processes, threads, green threads, and coroutines?
 > *Process: the program being executed, it can contain multiple threads
 Threads: a way to implement concurrency, can share memory
 Green threads: a way to use threads when the OS don't originally support it, can be
 scheduled by a virtual machine.
 Coroutine: Like fibers but not OS managed, fibers are like threads but they use cooperative
multitasking *
 
 ### Which one of these do `pthread_create()` (C/POSIX), `threading.Thread()` (Python), `go` (Go) create?
 > *Thread, thread, goroutine*
 
 ### How does pythons Global Interpreter Lock (GIL) influence the way a python Thread behaves?
 > *The GIL is a mutex, allowing only one thread at a time, not ideal if you have multiple processors*
 
 ### With this in mind: What is the workaround for the GIL (Hint: it's another module)?
 > *By cooperative multitasking*
 
 ### What does `func GOMAXPROCS(n int) int` change? 
 > *Indicates how many CPUs the process can use*