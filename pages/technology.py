from conftest import page


class technology:
    def __init__(self,page):
        self.page = page       

        # all the options under Technologies tab
        self.Technologies = page.locator('(//a[text()="Technologies"])[1]')

        #different options under ecommerce development
        self.eCommerce_Development = page.locator('//strong[text()="eCommerce Development"]')
        self.Magento_Development = page.locator('//a[text()="Magento Development"]')
        self.Opencart_Development = page.locator('(//a[normalize-space(.)="Opencart Development"])[1]')
        self.Codeigniter_Development = page.locator('(//a[normalize-space(.)="Codeigniter Development"])[1]')
        self.WordPress_Development = page.locator('(//a[normalize-space(.)="WordPress Development"])[1]')
        self.Big_Commerce = page.locator('(//a[normalize-space(.)="Big Commerce"])[1]')
        self.Shopify_Development = page.locator('(//a[normalize-space(.)="Shopify Development"])[1]')
        self.CS_Cart_Development = page.locator('(//a[normalize-space(.)="CS-Cart Development"])[1]')
        self.Node_JS_Development = page.locator('(//a[normalize-space(.)="Node JS Development"])[1]')
        self.Nop_Commerce = page.locator('(//a[normalize-space(.)="Nop Commerce"])[1]')
        self.Woo_Commerce = page.locator('(//a[normalize-space(.)="Woo Commerce"])[1]')
        self.Laravel_Development = page.locator('(//a[normalize-space(.)="Laravel Development"])[1]')
        self.Prestashop_Development = page.locator('(//a[normalize-space(.)="Prestashop Development"])[1]')
        self.Drupal_Development = page.locator('(//a[normalize-space(.)="Drupal Development"])[1]')
        self.Wix_Development = page.locator('(//a[normalize-space(.)="Wix Development"])[1]')
        self.Joomla_Development = page.locator('(//a[normalize-space(.)="Joomla Development"])[1]')
        self.React_JS_Development = page.locator('(//a[normalize-space(.)="React JS Development"])[1]')
        self.Express_JS_Development = page.locator('(//a[normalize-space(.)="Express JS Development"])[1]')
        self.ecom_options=[self.Magento_Development,self.Opencart_Development,self.Codeigniter_Development,self.WordPress_Development,self.Big_Commerce,self.Shopify_Development,
                    self.CS_Cart_Development,self.Node_JS_Development,self.Nop_Commerce,self.Woo_Commerce,self.Laravel_Development,self.Prestashop_Development,self.Drupal_Development,self.Wix_Development,
                    self.Joomla_Development,self.React_JS_Development,self.Express_JS_Development]
        
         # #different options under Mobile App Development
        self.Mobile_App_Development = page.locator('//strong[text()="Mobile App Development"]')
        self.React_Native_Mobile_App_Development = page.locator('(//a[normalize-space(.)="React Native Mobile App Development"])[1]')
        self.Enterprise_Mobile_App_Development = page.locator('(//a[normalize-space(.)="Enterprise Mobile App Development"])[1]')
        self.Xamarin_Mobile_App_Development = page.locator('(//a[normalize-space(.)="Xamarin Mobile App Development"])[1]')
        self.Kotlin_Mobile_App_Development = page.locator('(//a[normalize-space(.)="Kotlin Mobile App Development"])[1]')
        self.Flutter_Mobile_App_Development = page.locator('(//a[normalize-space(.)="Flutter Mobile App Development"])[1]')
        self.Ionic_App_Development = page.locator('(//a[normalize-space(.)="Ionic App Development"])[1]')
        self.Swift_App_Development = page.locator('(//a[normalize-space(.)="Swift App Development"])[1]')
        self.Appointment_Booking_Development = page.locator('(//a[normalize-space(.)="Appointment Booking Development"])[1]')

        self.mobile_app_options=[self.React_Native_Mobile_App_Development,self.Enterprise_Mobile_App_Development,self.Xamarin_Mobile_App_Development,self.Kotlin_Mobile_App_Development,
                            self.Flutter_Mobile_App_Development,self.Ionic_App_Development,self.Swift_App_Development,self.Appointment_Booking_Development]
        
         # #different options under Artificial Intelligence
        self.Artificial_Intelligence = page.locator('//a[strong[text()="Artificial Intelligence"]]')
        
        
    def ecom_options_click(self):
        for i in self.ecom_options:
            self.Technologies.hover()
            self.eCommerce_Development.hover()
            i.click()
            self.page.wait_for_timeout(3000)
            self.page.go_back()
            self.page.wait_for_timeout(1000)

    def mobile_app_options_click(self):
        for i in self.mobile_app_options:
            self.Technologies.hover()
            self.Mobile_App_Development.hover()
            i.click()
            self.page.wait_for_timeout(3000)
            self.page.go_back()
            self.page.wait_for_timeout(1000)

    def artificial_intelligence_click(self):
        self.Technologies.hover()
        self.Artificial_Intelligence.hover()
        self.Artificial_Intelligence.click()
        self.page.wait_for_timeout(3000)
        
        
