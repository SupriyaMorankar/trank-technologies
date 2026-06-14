class contact_us:
    def __init__(self,page):
        self.page = page

        self.Contact_us = page.locator('(//a[text()="Contact us"])[1]')

        #fill up free consultation form
        self.name = page.locator('(//input[@placeholder="Your Name"])[2]') 
        self.email = page.locator('(//input[@placeholder="Your Mail"])[2]')
        self.company = page.locator('(//input[@placeholder="Your Company"])[2]')
        self.choose_service = page.locator('(//select[@name="service"])[2]')
        self.mobile_no = page.locator('(//input[@placeholder="Your Phone"])[2]')
        self.message = page.locator('(//textarea[@placeholder="Message"])[2]')


    def contact_us_click(self):
        self.Contact_us.click()
        self.page.wait_for_timeout(1000)

    def fill_free_consultation_form(self,name,email,company,choose_service,mobile_no,message):
        self.name.fill(name)
        self.email.fill(email)
        self.company.fill(company)
        self.choose_service.select_option(choose_service)
        self.mobile_no.fill(mobile_no)
        self.message.fill(message)