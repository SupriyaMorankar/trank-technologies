import pytest

from pages.social_links import links

@pytest.mark.smoke
def test_social_links_click(page):
    social_links = links(page)
    social_links.social_links_click()