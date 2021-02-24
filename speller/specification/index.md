# Speller: Specification

Alright, the challenge now before you is to implement `load`, `check`, `size`, and `unload` as efficiently as possible, in such a way that `TIME IN load`, `TIME IN check`, `TIME IN size`, and `TIME IN unload` are all minimized. To be sure, it's not obvious what it even means to be minimized, inasmuch as these benchmarks will certainly vary as you feed `speller` different values for `dictionary` and for `text`. But therein lies the challenge, if not the fun, of this problem. This problem is your chance to design. Although we invite you to minimize space, your ultimate enemy is time. But before you dive in, some specifications from us.

* You may not alter `speller.c`.
* You may alter `dictionary.c` (and, in fact, must in order to complete the implementations of `load`, `check`, `size`, and `unload`), but you may not alter the declarations of `load`, `check`, `size`, or `unload`.
* You may alter `dictionary.h`, but you may not alter the declarations of `load`, `check`, `size`, or `unload`.
* You may alter `Makefile`.
* You may add functions to `dictionary.c` or to files of your own creation so long as all of your code compiles via `make`.
* Your implementation of `check` must be case-insensitive. In other words, if `foo` is in dictionary, then `check` should return true given any capitalization thereof; none of `foo`, `foO`, `fOo`, `fOO`, `fOO`, `Foo`, `FoO`, `FOo`, and `FOO` should be considered misspelled.
* Capitalization aside, your implementation of `check` should only return `true` for words actually in `dictionary`. Beware hard-coding common words (e.g., `the`), lest we pass your implementation a `dictionary` without those same words. Moreover, the only possessives allowed are those actually in `dictionary`. In other words, even if `foo` is in `dictionary`, `check` should return `false` given `foo's` if `foo's` is not also in `dictionary`.
* You may assume that `check` will only be passed strings with alphabetical characters and/or apostrophes.
* You may assume that any `dictionary` passed to your program will be structured exactly like ours, lexicographically sorted from top to bottom with one word per line, each of which ends with `\n`. You may also assume that `dictionary` will contain at least one word, that no word will be longer than `LENGTH` (a constant defined in `dictionary.h`) characters, that no word will appear more than once, and that each word will contain only lowercase alphabetical characters and possibly apostrophes.
* Your spell checker may only take `text` and, optionally, `dictionary` as input. Although you might be inclined (particularly if among those more comfortable) to "pre-process" our default dictionary in order to derive an "ideal hash function" for it, you may not save the output of any such pre-processing to disk in order to load it back into memory on subsequent runs of your spell checker in order to gain an advantage.
* Your spell checker may not leak any memory.
* You may search for (good) hash functions online, so long as you cite the origin of any hash function you integrate into your own code.

Alright, ready to go?

1. Implement `load`.
1. Implement `check`.
1. Implement `size`.
1. Implement `unload`.

## Walkthrough

Note that the following embed is a playlist of multiple videos that you should all watch!

[role="embed-responsive embed-responsive-21by9"]
video::u9-1U1Rgo1o[youtube,list=PLhQjrBD2T382vvokQIExRCKZq-q8PzSVz]

## Hints

Be sure to `free` in `unload` any memory that you allocated in `load`! Recall that `valgrind` is your newest best friend. Know that `valgrind` watches for leaks while your program is actually running, so be sure to provide command-line arguments if you want `valgrind` to analyze `speller` while you use a particular `dictionary` and/or text, as in the below. Best to use a small text, though, else `valgrind` could take quite a while to run.

    valgrind ./speller texts/ralph.txt

If you run `valgrind` without specifying a `text` for `speller`, your implementations of `load` and `unload` won't actually get called (and thus analyzed).

If unsure how to interpret the output of `valgrind`, do just ask `help50` for help:

    help50 valgrind ./speller texts/ralph.txt

## Testing

How to check whether your program is outting the right misspelled words? Well, you're welcome to consult the "answer keys" that are inside of the `keys` directory that's inside of your `speller` directory. For instance, inside of `keys/lalaland.txt` are all of the words that your program _should_ think are misspelled.

You could therefore run your program on some text in one window, as with the below.

    ./speller texts/lalaland.txt

And you could then run the staff's solution on the same text in another window, as with the below.

    ~cs50/2020/fall/pset5/speller texts/lalaland.txt

And you could then compare the windows visually side by side. That could get tedious quickly, though. So you might instead want to "redirect" your program's output to a file, as with the below.

    ./speller texts/lalaland.txt > student.txt
    ~cs50/2020/fall/pset5/speller texts/lalaland.txt > staff.txt

You can then compare both files side by side in the same window with a program like `diff`, as with the below.

    diff -y student.txt staff.txt

Alternatively, to save time, you could just compare your program's output (assuming you redirected it to, e.g., `student.txt`) against one of the answer keys without running the staff's solution, as with the below.

    diff -y student.txt keys/lalaland.txt

If your program's output matches the staff's, `diff` will output two columns that should be identical except for, perhaps, the running times at the bottom. If the columns differ, though, you'll see a `>` or `|` where they differ. For instance, if you see

~~~
MISSPELLED WORDS                                                MISSPELLED WORDS

TECHNO                                                          TECHNO
L                                                               L
                                                              > Thelonious
Prius                                                           Prius
                                                              > MIA
L                                                               L
~~~

that means your program (whose output is on the left) does not think that `Thelonious` or `MIA` is misspelled, even though the staff's output (on the right) does, as is implied by the absence of, say, `Thelonious` in the lefthand column and the presence of `Thelonious` in the righthand column.

### `check50`

To test your code less manually (though still not exhaustively), you may also execute the below.

    check50 -l minprog/cs50x/2020/speller/check

Note that `check50` will also check for memory leaks, so be sure you've run `valgrind` as well.

## Big Board

If you'd like to put your code to the test against classmates' code (just for fun), upload your solution to our https://bigboard.quinner.nl/[Big Board] website before or after you submit!

## Submit

Just upload your `dictionary.{c|h}` and you're done!
