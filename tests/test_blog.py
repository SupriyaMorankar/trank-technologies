import pytest

from pages.blog import blog

@pytest.mark.smoke
def test_blog_click(page):
    blog_page = blog(page)
    blog_page.blog_click()

def test_blog_options_click(page):
    blog_page = blog(page)
    blog_page.blog_options_click()
    