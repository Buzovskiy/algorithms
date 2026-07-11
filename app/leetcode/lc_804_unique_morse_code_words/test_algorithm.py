from algorithm import Solution


def test_solution():
    s = Solution()
    
    # Example 1
    assert s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]) == 2
    
    # Example 2
    assert s.uniqueMorseRepresentations(["a"]) == 1
    
    # Extra case: empty list (though constraints say 1 <= words.length)
    # assert s.uniqueMorseRepresentations([]) == 0
    
    # Multiple same words
    assert s.uniqueMorseRepresentations(["a", "a", "a"]) == 1

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
