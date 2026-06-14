
from conftest import page
class vertical:
    def __init__(self,page):
        self.page = page 
        self.vertical= page.locator('(//a[text()="Verticals"])[1]')
        self.trading = page.locator('//strong[text()="Trading"]')
        self.Stock_Trading = page.locator('(//a[text()="Stock Trading"])[1]')
        self.Algo_Trading = page.locator('//a[text()="Algo Trading"]')
        self.Paper_Trading = page.locator('//a[text()="Paper Trading"]')
        self.Custom_Trading = page.locator('(//a[normalize-space(.)="Custom Trading"])[1]')
        self.CFD_Trading = page.locator('(//a[normalize-space(.)="CFD Trading"])[1]')
        self.Web_Portal_Trading = page.locator('(//a[normalize-space(.)="Web Portal Trading"])[1]')
        self.Trading_App = page.locator('(//a[normalize-space(.)="Trading App Development in Massachusetts"])[1]')

        self.trading_list = [self.vertical,self.trading,self.Stock_Trading,self.Algo_Trading,self.Paper_Trading,self.Custom_Trading,self.CFD_Trading,self.Web_Portal_Trading,self.Trading_App]

        #different optopns under retail and ecommerce
        self.Retail_and_Ecommerce = page.locator('//strong[text()="Retail and Ecommerce"]')
        self.eCommerce_Website_Development = page.locator('(//a[normalize-space(.)="eCommerce Website Development"])[1]')
        self.eCommerce_App_Development = page.locator('//a[text()="eCommerce App Development"]')

        self.retail_options=[self.eCommerce_Website_Development,self.eCommerce_App_Development]

         #differnt options under Healthcare
        self.Healthcare = page.locator('//strong[text()="Healthcare"]')
        self.Diet_and_Nutritions = page.locator('(//a[normalize-space(.)="Diet & Nutritions"])[1]')
        self.Health_tracking_App = page.locator('(//a[normalize-space(.)="Health tracking App"])[1]')

        self.healthcare_options=[self.Diet_and_Nutritions,self.Health_tracking_App]

        #different options under Fintech
        self.Fintech = page.locator('//strong[text()="Fintech"]')
        self.Pos_Software_Development = page.locator('(//a[normalize-space(.)="Pos Software Development"])[1]')
        self.Crypto = page.locator('(//a[text()="Crypto"])[1]')
        self.fintech_options=[self.Pos_Software_Development,self.Crypto]

        #different options under custom app 
        self.Custom_App = page.locator('//strong[text()="Custom App"]')
        self.Desktop_App_Development =page.locator('(//a[normalize-space(.)="Desktop App Development"])[1]')
        self.CRM_Development = page.locator('(//a[normalize-space(.)="CRM Development"])[1]')
        self.HRM_Development = page.locator('(//a[normalize-space(.)="HRM Development"])[1]')
        self.ERP_App_Development = page.locator('(//a[normalize-space(.)="ERP App Development"])[1]')
        self.Travel = page.locator('(//a[normalize-space(.)="Travel"])[1]')
        self.E_Learning = page.locator('(//a[normalize-space(.)="E-Learning"])[1]')
        self.Dating_App_Development = page.locator('(//a[normalize-space(.)="Dating App Development"])[1]')
        self.Real_Estate = page.locator('(//a[normalize-space(.)="Real Estate"])[1]')
        self.CRM_Development_USA = page.locator('(//a[normalize-space(.)="CRM Development USA"])[1]')
        self.custom_options=[self.Desktop_App_Development,self.CRM_Development,self.HRM_Development,self.ERP_App_Development,self.Travel,self.E_Learning,self.Dating_App_Development,self.Real_Estate,self.CRM_Development_USA]

    def trading_options_click(self):
        for i in self.trading_list:
            self.vertical.hover()
            i.hover()
            i.click()
            self.page.wait_for_timeout(3000)
            self.page.go_back()
            self.page.wait_for_timeout(1000)

    def retail_and_ecommerce_options_click(self):
        for i in self.retail_options:
            self.vertical.hover()
            self.Retail_and_Ecommerce.hover()
            i.click()
            self.page.wait_for_timeout(3000)
            self.page.go_back()
            self.page.wait_for_timeout(1000)

    def healthcare_options_click(self):
        for i in self.healthcare_options:
            self.vertical.hover()
            self.Healthcare.hover()
            i.click()
            self.page.wait_for_timeout(3000)
            self.page.go_back()
            self.page.wait_for_timeout(1000)

    def fintech_options_click(self):
        for i in self.fintech_options:
            self.vertical.hover()
            self.Fintech.hover()
            i.click()
            self.page.wait_for_timeout(3000)
            self.page.go_back()
            self.page.wait_for_timeout(1000)

    def custom_app_options_click(self):
        for i in self.custom_options:
            self.vertical.hover()
            self.Custom_App.hover()
            i.click()
            self.page.wait_for_timeout(3000)
            self.page.go_back()
            self.page.wait_for_timeout(1000)

    