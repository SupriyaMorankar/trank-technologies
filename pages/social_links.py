class links:
    def __init__(self,page):
        self.page = page

        #Social media options - Follow us options
        self.facebook = page.locator('//a[@href="https://www.facebook.com/TrankTechnologies"]')
        self.linkedin = page.locator('//a[@href="https://in.linkedin.com/company/trank-technologies-official"]')
        self.instagram = page.locator('//a[@href="https://www.instagram.com/tranktechnologies/"]')
        self.pinterest = page.locator('//a[@href="https://in.pinterest.com/tranktechnologies12/"]')
        self.twitter = page.locator('//a[@href="https://twitter.com/tranktechno"]')
        self.youtube = page.locator('//a[@href="https://www.youtube.com/channel/UCWu1Y-tfrXf-Utpaft830Cg"]')
        self.quora = page.locator('//a[@href="https://www.quora.com/profile/Trank-Technologies-1"]')
        self.social_media = [self.facebook, self.linkedin, self.instagram, self.pinterest, self.twitter, self.youtube, self.quora]
        
    def social_links_click(self):
        for social in self.social_media:
            with self.page.context.expect_page() as new_page_info:
                social.click()
            new_tab = new_page_info.value
            new_tab.wait_for_load_state()
            print("Opened:", new_tab.url)
        new_tab.close()
        self.page.bring_to_front()
        self.page.wait_for_timeout(1000)