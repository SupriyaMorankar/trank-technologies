import pytest

from pages.footers import footers

@pytest.mark.smoke
def test_footer_options_click(page):
    footer = footers(page)
    footer.footer_options_click()

def test_ui_ux_options_click(page):
    footer = footers(page)
    footer.ui_ux_options_click()

def test_app_development_options_click(page):
    footer = footers(page)
    footer.app_development_options_click()

def test_graphics_design_options_click(page):
    footer = footers(page)
    footer.graphics_design_options_click()