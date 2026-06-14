import pytest

from pages.contact_us import contact_us

@pytest.mark.smoke
def test_contact_us_click(page):
    contact_us_page = contact_us(page)
    contact_us_page.contact_us_click()

def test_contact_us_options_click(page):
    contact_us_page = contact_us(page)
    contact_us_page.fill_free_consultation_form("Supriya", "supriya@example.com", "Example Company", "Web Development", "7777799999", "Looking for CRM application development")
