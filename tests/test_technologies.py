import pytest 

from pages.technology import technology

@pytest.mark.smoke
def test_ecom_options_click(page):
    technologies = technology(page)
    technologies.ecom_options_click()

def test_mobile_app_options_click(page):
    technologies = technology(page)
    technologies.mobile_app_options_click()

def test_artificial_intelligence_click(page):
    technologies = technology(page)
    technologies.artificial_intelligence_click()