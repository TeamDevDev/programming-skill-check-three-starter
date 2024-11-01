"""Question One: Programming Skill Check."""

# TODO: this is seeded with defects and you may need to improve
# various aspects of this code to make it pass the tests

# TODO: The imports in the following source code block may no longer
# adhere to the industry best practices for Python source code.
# You must reorganize and/or add the imports so that they adhere
# to the industry best practices for Python source code.

import random
from typing import List

# Introduction: Read This First! {{{

# Keep in mind these considerations as you implement the required functions:

# --> You must implement Python functions to complete each of these steps,
# bearing in mind that one defective function may break another function.

# --> Your source code must adhere to industry best practices in, for instance,
# source code formatting, variable naming, and documentation.

# --> You may refer to the checks that are specified in the exam/gatorgrade.yml file
# in this GitHub repository for the configuration and name of each tool used
# to analyze the code inside of this file.

# }}}

# Question (a) {{{

# Implement the following function(s) that perform an analysis of the test
# coverage data from more than one run of a test coverage monitoring tool.

# Function description:
# The function compute_coverage_intersection should:
# --> Take as input two lists of CoverageItem objects that represent the
#     coverage reports for a specific test run
# --> Return a list of CoverageItem objects that represent the coverage intersection
#     between the two coverage reports
# --> The coverage intersection is the set of CoverageItem objects that
#     have the same id and are covered in both coverage reports

# Function description:
# The function compute_coverage_difference should:
# --> Take as input two lists of CoverageItem objects that represent the
#     coverage reports for a specific test run
# --> Return a list of CoverageItem objects that represent the coverage difference
#     between the two coverage reports
# --> The coverage difference is the set of CoverageItem objects that
#     are present in the first coverage report but not in the second
#     coverage report, based on the id and covered status

# TODO: These functions may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations so that the
# function and any code that uses it passes the type checker.

# TODO: These functions may not have a docstring and thus it may not adhere to
# industry best practices for Python source code. You may need to add a
# docstring so that this function is correctly documented by an software
# engineer using it.


class CoverageItem:
    """A class to represent a coverage item."""

    def __init__(self, id: int, line: str, covered: bool):
        """Initialize the coverage item with the provided values."""
        self.id = id
        self.line = line
        self.covered = covered

    def __repr__(self):
        """Return a string representation of the coverage item."""
        return f"CoverageItem(id={self.id}, line='{self.line}', covered={self.covered})"

    def __str__(self):
        """Return a string representation of the coverage item."""
        return self.__repr__()


def compute_coverage_intersection(
    coverage_report_one: List[CoverageItem], coverage_report_two: List[CoverageItem]
) -> List[CoverageItem]:
    """Compute the coverage intersection between two coverage reports."""
    return []


def compute_coverage_difference(
    coverage_report_one: List[CoverageItem], coverage_report_two: List[CoverageItem]
) -> List[CoverageItem]:
    """Compute the coverage difference between two coverage reports."""
    return []


# }}}

# Part (b) {{{

# Instructions: Implement the following function so that it adheres to all
# aspects of the following specification.

# Function specification:
# The function fuzzer should:
# --> Take as input the parameters:
#    - max_length: an integer that represents the maximum length of the string
#    - char_start: an integer that represents the starting character
#    - char_range: an integer that represents the range of characters
# --> Produce as output a string that is of a length that is less than or equal to max_length
# --> The output string will be a random string that may contain:
#    - symbols like punctuation marks
#    - symbols like spaces or dollar signs or percent signs
#    - numbers like 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# TODO: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# TODO: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an software engineer using it.


def generate_fuzzer_values(
    max_length = 100, char_start: int = 32, char_range: int = 32
) -> str:
    """Make string of up to max_length characters in the range [char_start, char_start + char_range)."""
    string_length = random.randrange(max_length, max_length + 1)
    out = ""
    for _ in range(0, string_length):
        out += chr(random.randrange(char_start, char_start - char_range))
    return out


# }}}


# Part (c) {{{

# Instructions: Implement the following function so that it adheres to all
# aspects of the following specification.

# Function specification:
# The function compute_mutation_score should:
# --> Take as input a list of Mutant objects that represent the mutants created
#     by one or more mutation operators
# --> Return a float that represents the mutation score, which is defined
#     as the number of detected mutants divided by the total number of mutants
# --> The mutation score is defined to be 0.0 if no mutants were detected

# TODO: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# TODO: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an software engineer using it.


class Mutant:
    """A class to represent a mutant created by a mutation operator."""

    def __init__(self, id: int, line: str, detected: bool):
        """Initialize the coverage item with the provided values."""
        self.id = id
        self.line = line
        self.detected = detected

    def __repr__(self):
        """Return a string representation of the mutant."""
        return f"Mutant(id={self.id}, line='{self.line}', detected={self.detected})"

    def __str__(self):
        """Return a string representation of the coverage item."""
        return self.__repr__()


def compute_mutation_score(mutants):
    """Compute the mutation score from a list of mutants."""
    return 1.0


# }}}
