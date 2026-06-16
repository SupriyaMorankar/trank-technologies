class footers:
    def __init__(self, page):
        self.page = page   

        #different footer options
        #web development options
        self.Web_Development = page.get_by_role("link", name="Web Development")
        self.CMS_Website_Development = page.get_by_role("link", name="CMS Website Development")
        self.ECommerce_Development = page.get_by_role("link", name="ECommerce Development")
        self.Custom_Web_Portal_Development = page.get_by_role("link", name="Custom Web Portal Development")
        self.web_dev_options = [self.Web_Development,self.CMS_Website_Development,self.ECommerce_Development,self.Custom_Web_Portal_Development]

         #UI UX Design Options
        self.UI_UX_Design = page.get_by_role("link", name="UI UX Design", exact=True)
        self.Mobile_App_Design = page.get_by_role("link", name="Mobile App Design")
        self.Responsive_Web_Design = page.get_by_role("link", name="Responsive Web Design")
        self.Brand_Identity_Design = page.get_by_role("link", name="Brand Identity Design")
        self.ui_ux_options = [self.UI_UX_Design,self.Mobile_App_Design,self.Responsive_Web_Design,self.Brand_Identity_Design]

        #App development options
        self.App_Development = page.get_by_role("link", name="App Development", exact=True)
        self.iOS_App_Development = page.get_by_role("link", name="iOS App Development")
        self.Android_App_Development = page.get_by_role("link", name="Android App Development")
        self.Hybrid_Mobile_App_Development = page.get_by_role("link", name="Hybrid Mobile App Development")
        self.Cross_Platform_App_Development = page.get_by_role("link", name="Cross-Platform App Development")
        self.Progressive_Web_App_Development = page.get_by_role("link", name="Progressive Web App Development")
        self.app_development_opt = [self.App_Development,self.iOS_App_Development,self.Android_App_Development,self.Hybrid_Mobile_App_Development,self.Cross_Platform_App_Development,
                           self.Progressive_Web_App_Development]

         #graphics design options
        self.Graphic_Design = page.get_by_role("link", name="Graphic Design", exact=True)
        self.Logo_Design = page.get_by_role("link", name="Logo Design")
        self.Banner_Design = page.get_by_role("link", name="Banner Design")
        self.Packaging_Design = page.get_by_role("link", name="Packaging Design")
        self.Business_cards_Design = page.get_by_role("link", name="Business Cards Design")
        self.geaphics_options = [self.Graphic_Design,self.Logo_Design,self.Banner_Design,self.Packaging_Design,self.Packaging_Design,self.Business_cards_Design]


    


    def footer_options_click(self):
        for i in self.web_dev_options:
            i.click()
            self.page.wait_for_timeout(3000)
            self.page.go_back()
        self.page.wait_for_timeout(1000)

    def ui_ux_options_click(self):
        for i in self.ui_ux_options:
            i.click()
            self.page.wait_for_timeout(3000)
            self.page.go_back()
        self.page.wait_for_timeout(1000)

    def app_development_options_click(self):
        for i in self.app_development_opt:
            i.click()
            self.page.wait_for_timeout(3000)
            self.page.go_back()
        self.page.wait_for_timeout(1000)

    def graphics_design_options_click(self):
        for i in self.geaphics_options:
            i.click()
            self.page.wait_for_timeout(3000)
            self.page.go_back()
        self.page.wait_for_timeout(1000)