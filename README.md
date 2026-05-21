# Coding Projects

This repository is a cleaned and classified version of the files from `Coding/Projects`.

The original folder was left unchanged. Duplicate files were combined into one canonical copy in this repo.

## Categories

- `applications-and-mini-projects/` — larger beginner projects that combine multiple concepts.
- `assembly-and-low-level/` — Pep/assembly-style programs.
- `algorithms-and-games/` — grid/game-style algorithms.
- `basics-and-arithmetic/` — introductory input/output, calculators, grade logic, and simple arithmetic.
- `dictionaries-and-maps/` — dictionary/map exercises.
- `graphics-and-games/` — Pygame or visual/game experiments.
- `lists-and-statistics/` — list processing, sorting, averages, medians, and mark counting.
- `math-and-number-theory/` — Fibonacci, prime numbers, Pascal triangle, leap years, formulas, and numerical demos.
- `matrices-and-linear-algebra/` — matrices, vectors, and norms.
- `strings-and-text/` — string conversion, character shifting, and vowel counting.
- `setup-and-tools/` — setup commands and tooling scripts.
- `word-game/` — Wordle-style dictionary validation and feedback logic.
- `needs-fix/` — code that is incomplete, has syntax errors, or has clear runtime/logic issues.

## Combined duplicate files

| Combined file | Original files | Reason |
|---|---|---|
| `basics-and-arithmetic/hello_world.cpp` | `Cpp first 1.cpp`, `hello world.cpp` | Exact same Hello World program. |
| `word-game/wordle_feedback.py` | `PArt 4.py`, `PArt 4 (1).py` | Exact same Wordle-style feedback program. |
| `matrices-and-linear-algebra/sparse_matrix_builder.cpp` | `SUB 3 ma.cpp`, `SUB 3 ma (1).cpp` | Exact same sparse matrix builder. |
| `lists-and-statistics/second_largest_until_minus_one.py` | `Untitled-1.py`, `Untitled-43.py` | Same behaviour: read numbers until `-1`, sort descending, print the second largest. |
| `strings-and-text/uppercase_words.cpp` | `upper.cpp`, related to `SUB11.cpp` | Same uppercase-conversion goal. `upper.cpp` was kept as the cleaner version; `SUB11.cpp` is kept in `needs-fix/` because it has an off-by-one input issue. |

## Code catalogue

The original `Coding/Projects` cleanup is catalogued below. The later uploaded files are catalogued in `UPLOADED_CODE_CATALOGUE.md`.

| Original file | Category | Clean repo file | Description | Status |
|---|---|---|---|---|
| `1st Task.cpp` | Algorithms and games | `algorithms-and-games/grid_move_selector.cpp` | Reads a grid, apple position, and snake/obstacle coordinates, then prints the valid move or moves that bring the head closest to the apple. | Works syntactically. |
| `Assembly C++ personal conversion.cpp` | Math and number theory | `math-and-number-theory/fibonacci_until_limit.cpp` | Prints a Fibonacci-style sequence starting at `1 1` until it reaches the user-provided limit. | Works syntactically. |
| `Calculator generated.py` | Basics and arithmetic | `basics-and-arithmetic/simple_calculator.py` | Command-line calculator supporting `+`, `-`, `*`, `/`, and `//`, with division-by-zero handling. | Works syntactically. |
| `Cpp first 1.cpp` | Basics and arithmetic | `basics-and-arithmetic/hello_world.cpp` | Prints `Hello, World!`. Combined with `hello world.cpp`. | Combined duplicate. |
| `Lab1 week 5.py` | Lists and statistics | `lists-and-statistics/reverse_lines_until_marker.py` | Reads lines until `###`, reverses their order, and prints them. | Works syntactically. |
| `Lab2 week 5.py` | Lists and statistics | `lists-and-statistics/median_calculator.py` | Reads a count and that many numbers, sorts them, and prints the median. | Works syntactically. |
| `Lab3submission3.py` | Math and number theory | `math-and-number-theory/leap_year_checker.py` | Checks whether a year is a leap year using divisibility rules. | Works syntactically. |
| `PArt 4 (1).py` | Word game | `word-game/wordle_feedback.py` | Wordle-style feedback generator. Combined with `PArt 4.py`. | Combined duplicate. |
| `PArt 4.py` | Word game | `word-game/wordle_feedback.py` | Compares two five-letter words and outputs uppercase exact matches, lowercase misplaced matches, and `.` for misses. | Canonical duplicate. |
| `Python 3.py` | Needs fix / Word game | `needs-fix/broken_wordle_feedback_attempt.py` | Earlier Wordle feedback attempt. It has an indentation error and will not run. | Needs fix. |
| `SC example.py` | Matrices and linear algebra | `matrices-and-linear-algebra/vector_2_norm.py` | Reads a vector and prints its Euclidean 2-norm to six decimal places. | Works syntactically. |
| `SUB 1 (1).py` | Matrices and linear algebra | `matrices-and-linear-algebra/matrix_norms_numpy.py` | Uses NumPy to calculate matrix 1-norm, infinity norm, and Frobenius norm. | Works syntactically; requires NumPy. |
| `SUB 1 (2).py` | Matrices and linear algebra | `matrices-and-linear-algebra/matrix_norms_manual.py` | Manually calculates matrix 1-norm, infinity norm, and Frobenius norm. | Works syntactically. |
| `SUB 1 .cpp` | Basics and arithmetic | `basics-and-arithmetic/double_integer.cpp` | Reads an integer and prints double its value. | Works syntactically. |
| `SUB 1.py` | Needs fix / Matrices | `needs-fix/matrix_vector_multiply_attempt.py` | Attempts manual matrix-vector multiplication, but input handling is broken and variables are not correctly defined. | Needs fix. |
| `SUB 2.cpp` | Basics and arithmetic | `basics-and-arithmetic/subtract_two_numbers.cpp` | Reads two numbers and prints the first minus the second. | Works syntactically. |
| `SUB 3 ma (1).cpp` | Matrices and linear algebra | `matrices-and-linear-algebra/sparse_matrix_builder.cpp` | Sparse matrix builder. Combined with `SUB 3 ma.cpp`. | Combined duplicate. |
| `SUB 3 ma.cpp` | Matrices and linear algebra | `matrices-and-linear-algebra/sparse_matrix_builder.cpp` | Reads dimensions and sparse coordinate/value entries, fills a matrix, and prints it. | Canonical duplicate. |
| `SUB 3.cpp` | Basics and arithmetic | `basics-and-arithmetic/grade_classifier.cpp` | Reads a mark and prints degree classification: First, Upper second, Lower second, Third, or Fail. | Works syntactically. |
| `SUB 4 (1).cpp` | Needs fix / Math | `needs-fix/broken_leap_year_checker.cpp` | Intended C++ leap-year checker, but it contains a syntax error in the second condition. | Needs fix. |
| `SUB 4.cpp` | Lists and statistics | `lists-and-statistics/average_until_minus_one.cpp` | Reads numbers until `-1`, then prints their average. | Works syntactically. |
| `SUB 8.cpp` | Strings and text | `strings-and-text/shift_characters_cpp.cpp` | Reads a string and shifts every character to the next ASCII character. | Works syntactically. |
| `SUB 9.cpp` | Strings and text | `strings-and-text/count_vowels_until_end.cpp` | Reads lines until `end` and prints the number of vowels in each line. | Works syntactically. |
| `SUB11.cpp` | Needs fix / Strings | `needs-fix/uppercase_lines_off_by_one.cpp` | Converts lines to uppercase, but the loop reads one extra line because it uses `i <= n`. | Needs fix. |
| `SUB13.cpp` | Lists and statistics | `lists-and-statistics/count_passing_marks.cpp` | Reads 10 marks and counts how many are at least 50. | Works syntactically; extra `n` input is unused. |
| `SUB4 W12.cpp` | Math and number theory | `math-and-number-theory/pascal_triangle_factorial.cpp` | Prints rows of Pascal’s triangle using factorial-based combinations. | Works syntactically. |
| `Schmerg  code 2.py` | Math and number theory | `math-and-number-theory/schmerg_formula.py` | Calculates a nested custom mathematical expression called `schmerg`; also defines an unused Pythagoras helper. | Works syntactically. |
| `Schmerg  code.py` | Needs fix / Math | `needs-fix/schmerg_formula_unreachable_main.py` | Earlier `schmerg` formula version where the input/output block is indented after `return`, making it unreachable. | Needs fix. |
| `Sub1 w12.cpp` | Dictionaries and maps | `dictionaries-and-maps/name_marks_map.cpp` | Reads names and marks into a `map`, then prints them sorted by name. | Works syntactically. |
| `Sub2 w12.cpp` | Dictionaries and maps | `dictionaries-and-maps/food_frequency_counter.cpp` | Counts food-name occurrences until `end`, then prints each food with its count. | Works syntactically. |
| `Sub3 w12.cpp` | Needs fix / Math | `needs-fix/gcd_uninitialised_variable.cpp` | Attempts to calculate the greatest common divisor by checking factors, but `gcd` is not initialised. | Needs fix. |
| `Untitled-1.cpp` | Lists and statistics | `lists-and-statistics/second_smallest_and_second_largest.cpp` | Reads `n` numbers, sorts them, and prints the second smallest and second largest values. | Works syntactically. |
| `Untitled-1.py` | Lists and statistics | `lists-and-statistics/second_largest_until_minus_one.py` | Reads integers until `-1`, sorts them descending, and prints the second largest. | Canonical duplicate. |
| `Untitled-43.py` | Lists and statistics | `lists-and-statistics/second_largest_until_minus_one.py` | Same behaviour as `Untitled-1.py`: second-largest number before `-1`. | Combined duplicate. |
| `W12 SUB4.cpp` | Math and number theory | `math-and-number-theory/pascal_value_recursive.cpp` | Uses recursion to calculate one Pascal-triangle value at a given row and column. | Works syntactically. |
| `fire.py` | Graphics and games | `graphics-and-games/pygame_fire_template.py` | Pygame fire-animation template. The current `draw_fire` implementation fills the screen with random fire-coloured pixels. | Works syntactically; requires Pygame and a display. |
| `hello world.cpp` | Basics and arithmetic | `basics-and-arithmetic/hello_world.cpp` | Prints `Hello, World!`. Combined with `Cpp first 1.cpp`. | Combined duplicate. |
| `import math.py` | Math and number theory | `math-and-number-theory/floating_point_math_demo.py` | Demonstrates `sqrt`, exponentiation, and floating-point precision using `0.1 + 0.2`. | Works syntactically. |
| `lab3 week5 haww.py` | Dictionaries and maps | `dictionaries-and-maps/sorted_name_scores.py` | Reads name/score pairs, sorts by name, and prints formatted lines. | Works syntactically. |
| `lab3 week5.py` | Dictionaries and maps | `dictionaries-and-maps/name_scores_dictionary.py` | Reads name/score pairs into a dictionary and prints the dictionary object. | Works syntactically. |
| `lab4sub3.py` | Strings and text | `strings-and-text/shift_characters_python.py` | Python version of character shifting: increments each character by one Unicode code point. | Works syntactically. |
| `matrix.cpp` | Matrices and linear algebra | `matrices-and-linear-algebra/matrix_echo.cpp` | Reads a matrix and prints it back row by row. | Works syntactically. |
| `player.py` | Needs fix / Word game | `needs-fix/player_guess_stub.py` | Stub for a word-guessing player function. It raises an error instead of making a guess. | Incomplete. |
| `primes.cpp` | Math and number theory | `math-and-number-theory/twin_prime_checker.cpp` | C++ twin-prime checker: prints `true` if each input number is prime and has a prime neighbour two away. | Works syntactically. |
| `primes.py` | Math and number theory | `math-and-number-theory/twin_prime_checker.py` | Python twin-prime checker with the same goal as `primes.cpp`. | Works syntactically. |
| `python sub 1.py` | Word game | `word-game/word_dictionary_validator.py` | Reads five-letter dictionary words until `###`, then checks whether a guessed word is valid. | Works syntactically; input loop is awkward. |
| `task_7_template.py` | Word game | `word-game/word_game_template.py` | Word-guessing game template with dictionary reading, guess validation, and Wordle-style response logic. | Works syntactically; gameplay input logic needs cleanup. |
| `upper.cpp` | Strings and text | `strings-and-text/uppercase_words.cpp` | Reads `N` words, converts each to uppercase, and prints it. | Canonical uppercase version. |

## Notes

- Files in `needs-fix/` were kept so the work is not lost, but they should be repaired before submission or serious reuse.
- C++ files can usually be compiled with `g++ -std=c++17 <file>.cpp -o program`.
- Python files can usually be run with `python3 <file>.py`.
