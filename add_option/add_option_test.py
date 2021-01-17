
def test_check_url(site, url, code):
    print(site.status())
    assert site.status() == code