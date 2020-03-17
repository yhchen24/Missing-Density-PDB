import getdata


def test_getSamples():
    assert getdata.get_samples() == 'All files exist.', 'Download failed.'
    return
