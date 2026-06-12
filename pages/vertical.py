
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

    def trading_options_click(self):
        for i in self.trading_list:
            self.vertical.hover()
            i.hover()
            i.click()
            self.page.wait_for_timeout(3000)
            self.page.go_back()
            self.page.wait_for_timeout(1000)

    # def retail_and_ecommerce_options_click(self):
    #     for i in self.retail_options:
    #         self.vertical.hover()
    #         i.hover()
    #         i.click()
    #         self.page.wait_for_timeout(3000)
    #         self.page.go_back()
    #         self.page.wait_for_timeout(1000)