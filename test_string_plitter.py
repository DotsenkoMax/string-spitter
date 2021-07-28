from string_plitter import TagManipulator

def test_split_empty_string_result_empty_array():
    # arrange
    stringToSplit = ""
    regex = ""
    expResult = []
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)

    # assert
    assert result == expResult


def test_split_string_with_comma_result_empty_array():
    # arrange
    stringToSplit = ","
    regex = ""
    expResult = []
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)

    # assert
    assert result == expResult