from lambda_function import label_function


def test_label_function():
    bucket = "random-images-for-ml"
    name = "pheasant.jpg"

    expected = "grouse"
    result = label_function(bucket, name)
    print(result)

    assert result == expected
