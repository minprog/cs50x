# Sort

> Bij deze opdracht is het helemaal prima om samen te werken met één of twee medestudenten. Zorg dat je gezamenlijk op één scherm kunt kijken en echt samen het probleem probeert op te lossen. Heeft iemand een goed idee, dan moet die zorgen dat de anderen het ook begrijpen. De bedoeling is dat alle samenwerkers evenveel hebben bijgedragen aan de opdracht. Iedereen levert uiteindelijk een eigen versie in.

Analyze three sorting programs to determine which algorithms they use.


## Background

Recall from lecture that we saw a few algorithms for sorting a sequence of numbers: selection sort, bubble sort, and merge sort.

*   Selection sort iterates through the unsorted portions of a list, selecting the smallest element each time and moving it to its correct location.
*   Bubble sort compares pairs of adjacent values one at a time and swaps them if they are in the incorrect order. This continues until the list is sorted.
*   Merge sort recursively divides the list into two repeatedly and then merges the smaller lists back into a larger one in the correct order.


## Getting Started

1.  Log into [ide.cs50.io](https://ide.cs50.io/) using your GitHub account.
2.  In your terminal window, run `cd ~/problems` to switch to your `problems` directory.
2.  In your terminal window, run `wget https://github.com/minprog/cs50x/raw/2020/sort/sort.zip` to download a Zip file of the lab distribution code.
3.  In your terminal window, run `unzip sort.zip` to unzip (i.e., decompress) that Zip file.
4.  In your terminal window, run `cd lab3` to change directories into your `lab3` directory.


## Instructions

Provided to you are three already-compiled C programs, `sort1`, `sort2`, and `sort3`. Each of these programs implements a different sorting algorithm: selection sort, bubble sort, or merge sort (though not necessarily in that order!). Your task is to determine which sorting algorithm is used by each file.

*   `sort1`, `sort2`, and `sort3` are binary files, so you won't be able to view the C source code for each. To assess which sort implements which algorithm, run the sorts on different lists of values.
*   Multiple `.txt` files are provided to you. These files contain `n` lines of values, either reversed, shuffled, or sorted.
    *   For example, `reversed10000.txt` contains 10000 lines of numbers that are reversed from `10000`, while `random100000.txt` contains 100000 lines of numbers that are in random order.
*   To run the sorts on the text files, in the terminal, run `./[program_name] [text_file.txt]`.
    *   For example, to sort `reversed10000.txt` with `sort1`, run `./sort1 reversed10000.txt`.
*   You may find it helpful to time your sorts. To do so, run `time ./[sort_file] [text_file.txt]`.
    *   For example, you could run `time ./sort1 reversed10000.txt` to run `sort1` on 10,000 reversed numbers. At the end of your terminal's output, you can look at the `real` time to see how much time actually elapsed while running the program.
*   Record your answers in `answers.txt`, along with an explanation for each program, by filling in the blanks marked `TODO`.


## Walkthrough

<div markdown="1" class="extend">
[![](walkthrough.jpg)](https://video.cs50.io/-Bhxxw6JKKY)
</div>

[Open the problem walkthrough in the CS50 video player](https://video.cs50.io/-Bhxxw6JKKY)


## Hints

*   The different types of `.txt` files may help you determine which sort is which. Consider how each algorithm performs with an already sorted list. How about a reversed list? Or shuffled list? It may help to work through a smaller list of each type and walk through each sorting process.

<details markdown="1"><summary markdown="span">Not sure how to solve?</summary>

<div markdown="1" class="extend">
[![](walkthrough.jpg)](https://video.cs50.io/uOYhrBs37j0)
</div>

[Open the solution walkthrough in the CS50 video player](https://video.cs50.io/uOYhrBs37j0)
</details>


## How to Check Your Answers

Execute the below to evaluate the correctness of your answers using `check50`. But be sure to fill in your explanations as well, which `check50` won't check here!

    check50 -l minprog/cs50x/2020/sort


## How to submit

As soon as you're done, submit `answers.txt`, below! 

1. Toward CS50 IDE's top-left corner, within its "file browser" (not within a terminal window), control-click or right-click your `answers.txt` file (that's within your `problems/sort` directory) and then select **Download**. You should find that your browser has downloaded `answers.txt`.

2. Make sure you are signed in to **this** website!

3. Type the names of students that you've worked with on this problem: <input type="text" required>

4. In the form below, choose the file that you just downloaded.

Your program will then again be checked using `check50` and the result will be recorded on this website. Should the check fail unexpectedly, be sure to try if `check50` is still satisfied when you run it in your IDE's Terminal.
