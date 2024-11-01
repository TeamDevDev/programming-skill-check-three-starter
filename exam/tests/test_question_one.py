"""Confirm the correctness of functions in question_one."""

import pytest

# ruff: noqa: PLR2004
from questions.question_one import (
    CoverageItem,
    Mutant,
    compute_coverage_difference,
    compute_coverage_intersection,
    compute_mutation_score,
    generate_fuzzer_values,
)


@pytest.mark.question_one_part_a
def test_compute_coverage_difference():
    """Confirm correctness of question part."""
    item1 = CoverageItem(1, "line1", True)
    item2 = CoverageItem(2, "line2", True)
    item3 = CoverageItem(3, "line3", True)
    item4 = CoverageItem(4, "line4", True)
    item5 = CoverageItem(5, "line5", True)
    item6 = CoverageItem(6, "line6", True)
    item7 = CoverageItem(1, "line1", False)
    item8 = CoverageItem(2, "line2", False)
    item9 = CoverageItem(3, "line3", False)
    assert compute_coverage_intersection(
        [item1, item2, item3], [item1, item2, item3]
    ) == [
        item1,
        item2,
        item3,
    ], "Failed on case with identical coverage reports"
    assert (
        compute_coverage_intersection([item1, item2, item3], [item4, item5, item6])
        == []
    ), "Failed on case with no common coverage"
    assert compute_coverage_intersection(
        [item1, item2, item3], [item2, item3, item4]
    ) == [
        item2,
        item3,
    ], "Failed on case with partial overlap"
    assert compute_coverage_intersection(
        [item1, item2, item3], [item3, item2, item1]
    ) == [
        item1,
        item2,
        item3,
    ], "Failed on case with identical coverage reports in different order"
    assert (
        compute_coverage_intersection([], []) == []
    ), "Failed on case with empty coverage reports"
    assert (
        compute_coverage_intersection([item1, item2, item3], [item7, item8, item9])
        == []
    ), "Failed on case with same ids but not covered"
    assert (
        compute_coverage_difference([item1, item2, item3], [item1, item2, item3]) == []
    ), "Failed on case with identical coverage reports"
    assert compute_coverage_difference(
        [item1, item2, item3], [item4, item5, item6]
    ) == [
        item1,
        item2,
        item3,
    ], "Failed on case with no common coverage"
    assert compute_coverage_difference(
        [item1, item2, item3], [item2, item3, item4]
    ) == [item1], "Failed on case with partial overlap"
    assert (
        compute_coverage_difference([item1, item2, item3], [item3, item2, item1]) == []
    ), "Failed on case with identical coverage reports in different order"
    assert (
        compute_coverage_difference([], []) == []
    ), "Failed on case with empty coverage reports"
    assert compute_coverage_difference(
        [item1, item2, item3], [item7, item8, item9]
    ) == [
        item1,
        item2,
        item3,
    ], "Failed on case with same ids but different coverage status"


@pytest.mark.question_one_part_b
def test_generate_fuzzer_values():
    """Confirm correctness of question part."""
    max_length = 10
    result = generate_fuzzer_values(max_length)
    assert len(result) <= max_length, "Generated string is too long"
    char_start = 65
    char_range = 26
    result = generate_fuzzer_values(100, char_start, char_range)
    for char in result:
        assert (
            char_start <= ord(char) < char_start + char_range
        ), "Character is not in range"
    result = generate_fuzzer_values(0)
    assert result == "", "Empty string not generated"


@pytest.mark.question_one_part_c
def test_compute_mutation_score():
    """Confirm correctness of question part."""
    # summary of the checks:
    # check 1: Empty list of mutants
    # check 2: Empty
    # check 3: Partially detected
    # check 4: Fully detected
    # check 1: Empty list of mutants
    assert compute_mutation_score([]) == 0.0
    # check 2: All undetected mutants
    assert (
        compute_mutation_score([Mutant(1, "line1", False), Mutant(2, "line2", False)])
        == 0.0
    )
    # check 3: Partially detected mutants
    assert (
        compute_mutation_score([Mutant(1, "line1", True), Mutant(2, "line2", False)])
        == 0.5
    )
    # check 4: All detected mutants
    assert (
        compute_mutation_score([Mutant(1, "line1", True), Mutant(2, "line2", True)])
        == 1.0
    )
