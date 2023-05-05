# Playfair Evolutionary Solver

Written in **Python 3.9**, but other versions may also work.

This is an evolutionary algorithm implementation of a Playfair cipher solver.
The grid is represented as a string of characters A-Z (excluding J) and will
iterate through generations combining solutions and mutating them until the
known plain text is discovered. This does not guarantee a correct solution, but
will eventually find a valid solution that can produce the plain text given.

A design decision not to use any additional libraries such as numpy was made
to make the program easier to run without having to set up a virtual environment
a language such as and install the libraries.

## Setup

There are no dependencies other than Python 3. Just clone the repo and get
cracking!

```
git clone https://github.com/GTBebbo/PlayfairEvolutionarySolver.git
```

## Usage

Place the cipher text in a `cipher.text` file in the same directory as
`main.py`.

Place the known plain text in a `plain.text` file in the same directory as
`main.py`.

To run the solver run:

```
python main.py
```

__If you need to change the Playfair algorithm itself, you can modify the
`ALPHABET` parameter in the `settings.py` file for example to change the
excluded `J` to another letter.__

## How to solve

This does not guarantee a solution, this is purely an evolutionary algorithm
to find a solution that fits or nearly fits the plaintext. It works best with
longer (50+ character) ciphers and plain texts. Smaller ciphers can produce
valid but incorrect tables too easily.

You may need to modify the settings in `settings.py` to achieve better results.

Often when using a small amount of plaintext, the a valid table may be found
that doesn't decrypt the entire ciphertext. This is an iterative process and you
should use the found solution to guess at some previously unknown plaintext.
By expanding the plaintext, you will have a better chance of finding the correct
solution.

For example, given the following:

```
# Ciphertext
YL NR EX RQ AT QB ML NG OV LO OI DY
# Plaintext
WOULD YOU LIKE TO
```

You may find a result like this:

```
WOULD YOU LIKE TO PLAYAGOMEOFNSEOLATYD
```

We can now guess at some of the previously unknown ciphertext and update our
plaintext file.

```
WOULD YOU LIKE TO PLAY A GAME
```

Running the algorithm again with this new plaintext gives us the correct result:

```
WOULD YOU LIKE TO PLAY A GAME OF MONOPOLY X
```

__This is the table to decrypt the above if you were interested:__

```
ALGOR
ITHMS
BCDEF
KNPQU
VWXYZ
```

## Furture Improvements

**Mutations**: Currently the mutation step swaps random letters in the table,
an improvement could swap entire rows and columns.

**Playfair Semantics**: The current algorithm ignores the sematics of Playfair,
for example the fact characters should form rectangles or lines.

**Language**: There is a possibility to speed the algorithm up by a lot by
re-implementing the program in a language such as C++.

**Automatic Plaintext Recognition**: By using a dictionary of words, we can
compare the decrypted plaintext result to try to automatically expand the known
plaintext to prevent the user from manually doing so.

**Plaintext Anywhere**: Currently the algorithm only accepts known plaintext for
the first part of the cipher, a future update could allow for known plaintext
to be used anywhere in the cipher.

