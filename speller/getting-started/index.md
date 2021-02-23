# Speller

## tl;dr

Implement a program that spell-checks a file, per the below.

~~~
$ ./speller texts/lalaland.txt
MISSPELLED WORDS

[...]
AHHHHHHHHHHHHHHHHHHHHHHHHHHHT
[...]
Shangri
[...]
fianc
[...]
Sebastian's
[...]

WORDS MISSPELLED:
WORDS IN DICTIONARY:
WORDS IN TEXT:
TIME IN load:
TIME IN check:
TIME IN size:
TIME IN unload:
TIME IN TOTAL:
~~~

## Distribution

### Downloading

    $ wget https://github.com/minprog/cs50x/raw/2020/speller/speller.zip
    $ unzip speller.zip
    $ rm speller.zip
    $ cd speller
    $ ls
    dictionaries/  dictionary.c  dictionary.h  keys/  Makefile  answers.md  speller.c  texts/

### Understanding

Theoretically, on input of size _n_, an algorithm with a running time of _n_ is asymptotically equivalent, in terms of _O_, to an algorithm with a running time of pass:[2]_n_. In the real world, though, the fact of the matter is that the latter feels twice as slow as the former.

The challenge ahead of you is to implement the fastest spell checker you can! By "fastest," though, we're talking actual, real-world, noticeable time—none of that asymptotic stuff this time.

In `speller.c`, we've put together a program that's designed to spell-check a file after loading a dictionary of words from disk into memory. Unfortunately, we didn't quite get around to implementing the loading part. Or the checking part. Both (and a bit more) we leave to you! But first, a tour.

#### `dictionary.{c,h}`

Open up `dictionary.h`. Declared in that file are four functions; take note of what each should do. Now open up `dictionary.c`. Notice that we've implemented those four functions, but only barely, just enough for this code to compile. Your job, ultimately, is to re-implement those functions as cleverly as possible so that this spell checker works as advertised. And fast!

#### `Makefile`

Recall that make automates compilation of your code so that you don't have to execute clang manually along with a whole bunch of switches. However, as your programs grow in size, make won't be able to infer from context anymore how to compile your code; you'll need to start telling make how to compile your program, particularly when they involve multiple source (i.e., .c) files, as in the case of this problem. And so we'll utilize a Makefile, a configuration file that tells make exactly what to do. Open up Makefile, and you should see four lines:

1. The first line tells make to execute the subsequent lines whenever you yourself execute make speller (or just make).
2. The second line tells make how to compile speller.c into machine code (i.e., speller.o).
3. The third line tells make how to compile dictionary.c into machine code (i.e., dictionary.o).
4. The fourth line tells make to link speller.o and dictionary.o in a file called speller.

> Be sure to compile speller by executing `make speller` (or just `make`). Executing `make dictionary` won't work!

#### `speller.c`

Okay, next open up `speller.c` and spend some time looking over the code and comments therein. You won't need to change anything in this file, but you should understand it nonetheless. Notice how, by way of `getrusage`, we'll be "benchmarking" (i.e., timing the execution of) your implementations of `check`, `load`, `size`, and `unload`. Also notice how we go about passing `check`, word by word, the contents of some file to be spell-checked. Ultimately, we report each misspelling in that file along with a bunch of statistics.

Notice, incidentally, that we have defined the usage of `speller` to be

    Usage: speller [dictionary] text

where `dictionary` is assumed to be a file containing a list of lowercase words, one per line, and `text` is a file to be spell-checked. As the brackets suggest, provision of `dictionary` is optional; if this argument is omitted, `speller` will use `dictionaries/large` by default. In other words, running

    ./speller text

will be equivalent to running

    ./speller dictionaries/large text

where `text` is the file you wish to spell-check. Suffice it to say, the former is easier to type! (Of course, `speller` will not be able to load any dictionaries until you implement `load` in `dictionary.c`! Until then, you'll see *Could not load*.)

Within the default dictionary, mind you, are 143,091 words, all of which must be loaded into memory! In fact, take a peek at that file to get a sense of its structure and size. Notice that every word in that file appears in lowercase (even, for simplicity, proper nouns and acronyms). From top to bottom, the file is sorted lexicographically, with only one word per line (each of which ends with `\n`). No word is longer than 45 characters, and no word appears more than once. During development, you may find it helpful to provide `speller` with a `dictionary` of your own that contains far fewer words, lest you struggle to debug an otherwise enormous structure in memory. In `dictionaries/small` is one such dictionary. To use it, execute

    ./speller dictionaries/small text

where `text` is the file you wish to spell-check. Don't move on until you're sure you understand how `speller` itself works!

Odds are, you didn't spend enough time looking over `speller.c`. Go back one square and walk yourself through it again!

#### `texts/`

So that you can test your implementation of `speller`, we've also provided you with a whole bunch of texts, among them the script from _La La Land_, the text of the Affordable Care Act, three million bytes from Tolstoy, some excerpts from _The Federalist Papers_ and Shakespeare, the entirety of the King James V Bible and the Koran, and more. So that you know what to expect, open and skim each of those files, all of which are in a directory called `texts` within your `module5` directory.

Now, as you should know from having read over `speller.c` carefully, the output of `speller`, if executed with, say,

    ./speller texts/lalaland.txt

will eventually resemble the below. For now, try executing the staff's solution (using the default dictionary) with the below.

    ~cs50/2020/fall/pset5/speller texts/lalaland.txt

Below's some of the output you'll see. For information's sake, we've excerpted some examples of "misspellings." And lest we spoil the fun, we've omitted our own statistics for now.

~~~
MISSPELLED WORDS

[...]
AHHHHHHHHHHHHHHHHHHHHHHHHHHHT
[...]
Shangri
[...]
fianc
[...]
Sebastian's
[...]

WORDS MISSPELLED:
WORDS IN DICTIONARY:
WORDS IN TEXT:
TIME IN load:
TIME IN check:
TIME IN size:
TIME IN unload:
TIME IN TOTAL:
~~~

`TIME IN load` represents the number of seconds that `speller` spends executing your implementation of `load`. `TIME IN check` represents the number of seconds that `speller` spends, in total, executing your implementation of `check`. `TIME IN size` represents the number of seconds that `speller` spends executing your implementation of `size`. `TIME IN unload` represents the number of seconds that `speller` spends executing your implementation of `unload`. `TIME IN TOTAL` is the sum of those four measurements.

*Note that these times may vary somewhat across executions of `speller`, depending on what else CS50 IDE is doing, even if you don't change your code.*

Incidentally, to be clear, by "misspelled" we simply mean that some word is not in the `dictionary` provided.

## Questions

Open up `answers.md` and answer each of the questions therein. Then sumbit your answers, below.
