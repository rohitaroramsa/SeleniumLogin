class googleSearch():
    def __init__(self, driver):
        self.driver = driver
        self.agree_frame = '//*[@id="cnsw"]/iframe'
        self.agree_btn_xpath = '//*[@id="introAgreeButton"]/span/span'
        self.search_text_xpath = '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input'
        self.google_logo_id = 'hplogo'
        self.search_btn_xpath = '//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]'

    def accept_agreement(self):
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(self.agree_frame))
        self.driver.find_element_by_xpath(self.agree_btn_xpath).click()

    def search_box(self, cityname):
        self.driver.find_element_by_xpath(self.search_text_xpath).send_keys(cityname)
        self.driver.find_element_by_id(
            self.google_logo_id).click()  # To get rid of lookup which makes clicking on Search button difficult

    def search_click(self):
        self.driver.find_element_by_xpath(self.search_btn_xpath).click()
