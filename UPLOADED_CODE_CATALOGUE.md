# Uploaded Code Catalogue

This catalogue covers the extra uploaded code files added after the first `Coding/Projects` cleanup.

## Added categories

- `applications-and-mini-projects/` — larger beginner projects that combine multiple concepts.
- `assembly-and-low-level/` — Pep/assembly-style programs.
- `setup-and-tools/` — setup commands and tooling scripts.

## Combined duplicate or same-purpose files

| Combined file | Uploaded files | Reason |
|---|---|---|
| `applications-and-mini-projects/fifa_attribute_rating.py` | `Fifa attribute rating project-aed06c28152c.py`, `Shooting rating project-95afca323acd.py` | Both calculate FIFA-style player attribute ratings. The `Fifa attribute rating` version is cleaner because it stores each player in a dictionary and calculates an overall rating. |
| `strings-and-text/shift_characters_python.py` | `lab4sub3-1d7cff70e0ad.py`, existing `lab4sub3.py` | Exact same goal: read a string and shift every character to the next Unicode code point. The existing canonical file was kept. |
| `lists-and-statistics/second_largest_until_minus_one.py` | `Q5 of Triangular numbers lab test 1-d912c338cc8b.py`, existing second-largest exercise | Same intended task: read numbers until `-1` and print the second largest. The uploaded version was also stored in `needs-fix/` because it ignores the first input and can include the sentinel in the list. |

## Code descriptions

| Uploaded file | Category | Clean repo file | Description | Status |
|---|---|---|---|---|
| `FIRST-93378e91a710.pep` | Assembly and low-level | `assembly-and-low-level/sum_n_numbers.pep` | Pep/assembly-style program that reads `N`, then reads `N` numbers, accumulates their sum, and outputs the total. | Kept as source. |
| `lab4sub1-cc124007600b.py` | Lists and statistics | `lists-and-statistics/minimum_until_minus_one.py` | Reads integers until `-1` and prints the smallest value entered. | Works syntactically. |
| `lab4sub2-11fcfa7b5f9b.py` | Lists and statistics | `lists-and-statistics/average_until_minus_one.py` | Reads floating-point numbers until `-1`, then prints the average if at least one value was entered. | Works syntactically. |
| `lab4sub3-1d7cff70e0ad.py` | Strings and text | `strings-and-text/shift_characters_python.py` | Reads a string and shifts every character forward by one Unicode code point. | Combined duplicate. |
| `lab4sub4-65872f9698e1.py` | Strings and text | `strings-and-text/count_vowels_until_end.py` | Reads words until `end` and prints the number of vowels in each word. | Works syntactically. |
| `Q5 of Triangular numbers lab test 1-d912c338cc8b.py` | Needs fix / Lists and statistics | `needs-fix/broken_second_largest_until_minus_one.py` | Intended to print the second largest number before `-1`, but it discards the first input and appends the sentinel before sorting. | Needs fix; intended duplicate of canonical second-largest exercise. |
| `Shooting rating project-95afca323acd.py` | Applications and mini-projects | `applications-and-mini-projects/fifa_attribute_rating.py` | Earlier FIFA-style player rating project that calculates shooting, passing, pace, dribbling, defending, and physical scores. | Combined into the cleaner FIFA attribute project. |
| `students_marks-397e7c757be3.py` | Setup and tools | `setup-and-tools/install_visual_studio_build_tools.bat` | Windows `winget` command for installing Visual Studio 2022 Build Tools and C++ toolchain components. | Reclassified from `.py` because it is not Python code. |
| `vibes-9815e99ed5b6.py` | Basics and arithmetic | `basics-and-arithmetic/postgraduate_eligibility_checker.py` | Checks eligibility using average mark, years of work experience, and honours-degree status. | Works syntactically. |
| `#Question 1-bfe126567dcb.py` | Basics and arithmetic | `basics-and-arithmetic/celsius_to_fahrenheit.py` | Converts a Celsius temperature to Fahrenheit. | Works syntactically. |
| `#Question 2-968ad7cbc69d.py` | Strings and text | `strings-and-text/count_uppercase_letters.py` | Counts uppercase English letters in an input string. | Works syntactically. |
| `Fifa attribute rating project-aed06c28152c.py` | Applications and mini-projects | `applications-and-mini-projects/fifa_attribute_rating.py` | Calculates FIFA-style player attribute scores across shooting, passing, pace, dribbling, defending, physical, and overall rating. | Canonical combined version. |
| `import math SC class 31 March-4cbe63752f88.py` | Needs fix / Math and number theory | `needs-fix/broken_polynomial_formula.py` | Attempts to evaluate a polynomial at `4.71`, but uses `^` instead of `**`, which causes a runtime error with floats. | Needs fix. |
| `Lab_test_1 coding practise-494315641d87.py` | Strings and text | `strings-and-text/palindrome_batch_checker.py` | Reads a number of words and prints `True` or `False` depending on whether each word is a palindrome. | Works syntactically. |
