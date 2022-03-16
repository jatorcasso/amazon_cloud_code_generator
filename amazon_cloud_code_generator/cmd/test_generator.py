import pytest

import amazon_cloud_code_generator.cmd.generator as g


def test_Description_normalize():
    assert g.Description.normalize(["a", "b"]) == ["a", "b"]
    assert g.Description.normalize([""]) == [""]
    assert g.Description.normalize(["CloudWatch"]) == ["CloudWatch"]
    assert g.Description.normalize(["The Amazon Resource Name (ARN) of the Amazon SQS queue to which Amazon S3 publishes a message."]) == ["The Amazon Resource Name (ARN) of the Amazon SQS queue to which Amazon S3 publishes a message."]
    assert g.Description.normalize(["Setting this element to TRUE causes Amazon S3 to reject calls to PUT Bucket policy."]) == ["Setting this element to C(True) causes Amazon S3 to reject calls to PUT Bucket policy."]
    assert g.Description.normalize(
        ['Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, and 3653.']
    ) == ['Possible values are: C(1), C(3), C(5), C(7), C(14), C(30), C(60), C(90), C(120), C(150), C(180), C(365), C(400), C(545), C(731), C(1827), and C(3653).']
    assert g.Description.normalize([
        'Container for the transition rule that describes when noncurrent objects transition to the STANDARD_IA, ONEZONE_IA, INTELLIGENT_TIERING, GLACIER_IR, C(GLACIER), or DEEP_ARCHIVE storage class.'
        ]) == [
        'Container for the transition rule that describes when noncurrent objects transition to the C(STANDARD_IA), C(ONEZONE_IA), C(INTELLIGENT_TIERING), C(GLACIER_IR), C(GLACIER), or C(DEEP_ARCHIVE) storage class.'
    ]
    assert g.Description.normalize([
        'You must specify at least one of Option, OptionOne and AnotherSecondOption.'
        ]) == [
        'You must specify at least one of I(option), I(option_one) and I(another_second_option).'
    ]


def test_generate_documentation():
     
    