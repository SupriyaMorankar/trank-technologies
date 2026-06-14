import pytest
from pages.about_us import AboutUs


@pytest.mark.smoke
def test_about_us_click(page):
    about_us_page = AboutUs(page)
    about_us_page.about_us_click()