import getdata


def test_getSamples():
    assert getdata.getSamples() == 'All files exist.', 'Download failed.'
    return
