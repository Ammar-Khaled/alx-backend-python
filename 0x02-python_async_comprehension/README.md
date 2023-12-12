0x02. Python - Async Comprehension
==================================

This repo is included in Specializations - Back-end programming Course of **Holberton School** at **ALX**. We will cover the `Python - Async Comprehension` language


Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](https://intranet.hbtn.io/rltoken/JRP7eBbJ167jvXfjr3HafA "explain to anyone"), **without the help of Google**:

*   How to write an asynchronous generator
*   How to use async comprehensions
*   How to type-annotate generators

Files
-----

### 0\. Async Generator

Define a coroutine called `async_generator` that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the `random` module.

### 1\. Async Comprehensions

Import `async_generator` from the previous task and then define a coroutine called `async_comprehension` that takes no arguments.

The coroutine will collect 10 random numbers using an async comprehensing over `async_generator`, then return the 10 random numbers.

### 2\. Run time for four parallel comprehensions

Import `async_comprehension` from the previous file and define a `measure_runtime` coroutine that will execute `async_comprehension` four times in parallel using `asyncio.gather`.

`measure_runtime` should measure the total runtime and return it.
