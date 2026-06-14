class blog:
    def __init__(self,page):
        self.page = page
        self.Blog = page.locator('(//a[text()="Blog"])[1]')


         #different options under blog
        self.App_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/app-development/"])[2]')
        self.Artificial_Intelligence = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/artificial-intelligence/"]')
        self.Content_Marketing = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/content-marketing/"]')
        self.CRM_Development =  page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/crm-development/"]')
        self.Digital_Marketing = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/digital-marketing/"]')
        self.ECommerce_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ecommerce-development/"])[5]')
        self.Email_Marketing = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/email-marketing/"]')
        self.Graphic_Design = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/graphic-design/"])[3]')
        self.Software_n_IT_Company = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/software-it-company/"]')
        self.Software_Development = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/software-development/"]')
        self.UI_UX_Design = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ui-ux-design/"])[5]')
        self.Web_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/web-development/"])[5]')
        self.blog_options = [self.App_Development,self.Artificial_Intelligence,self.Content_Marketing,self.CRM_Development,self.Digital_Marketing,self.ECommerce_Development,self.Email_Marketing,self.Graphic_Design,
                    self.Software_n_IT_Company,self.Software_Development,self.UI_UX_Design,self.Web_Development]


    def blog_click(self):
        self.Blog.click()
        self.page.wait_for_timeout(3000)

    def blog_options_click(self):
        for i in self.blog_options:
            self.Blog.hover()
            i.hover()
            i.click()
            self.page.wait_for_timeout(3000)
            self.page.go_back()
            self.page.wait_for_timeout(1000)