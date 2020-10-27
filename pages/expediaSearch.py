import time
class ExpediaPackage():
    def __init__(self, driver):
        self.driver = driver

        # Web Element for More options for packages such as CARS+Flight+Stay
        self.more_option_dd_xpath = '//*[@id="gc-custom-header-tool-bar-shop-menu"]/button/div'
        self.packages_link = 'Packages'

        # Web Element for  "source and Detination Cities"
        self.sourceField_xpath_click = '//*[@id="location-field-origin-menu"]/div[1]/button'
        self.sourceField_id_text = 'location-field-origin'
        self.sourceField_xpath_firstresult = '//*[@id="location-field-origin-menu"]/div[2]/ul/li[1]/button/div/div[2]'
        self.destinationField_xpath_click = '//*[@id="location-field-destination-menu"]/div[1]/button'
        self.destinationField_id_text = 'location-field-destination'
        self.destinationField_xpath_firstresult = '//*[@id="location-field-destination-menu"]/div[2]/ul/li[1]/button'

        # Web Element for 'no of Travller setup'
        self.travellor_btn_link = '1 room, 2 travelers'
        self.adult_decrease_btn_xpath = '//*[@id="adaptive-menu"]/div/div/section/div[1]/div[1]/div/button[1]'
        self.child_increase_btn_xpath = '//*[@id="adaptive-menu"]/div/div/section/div[1]/div[2]/div/button[2]'
        self.child_age_xpath = '//*[@id="child-age-input-0-0"]'
        self.traveller_done_btn_xpath = '//*[@id="adaptive-menu"]/div/div/div[2]/button'

        # Web Element for 'Setting of dates'
        self.datepicker_id = 'd1-btn'
        self.next_month_xpath = '//*[@id="wizard-package-pwa-1"]/div[3]/div[2]/div/div/div/div[1]/div/div[2]/div/div[1]/div[1]/button[2]'
        self.month_parent_xpath = '//*[@id="wizard-package-pwa-1"]/div[3]/div[2]/div/div/div/div[1]/div/div[2]/div/div[1]/div[2]/div[1]/table'
        self.month_dates_class = 'uitk-new-date-picker-day-number'
        self.datepicker_done_xpath = '//*[@id="wizard-package-pwa-1"]/div[3]/div[2]/div/div/div/div[1]/div/div[2]/div/div[2]/button'

        #Web Element for Search Button
        self.search_btn_xpath = '//*[@id="wizard-package-pwa-1"]/div[4]/div/button'


        '''Web Element for -> On Search result page1 this shall be choose your destination which is a indication of user now on Results Page'''
        self.step1_search_results_page = '//*[@id="multiStepIndicatorContainer"]/div[1]/div[1]/h3/span[2]'

    '''Will direct to Package page where cars+Stay is set by default'''
    def direct_package_page(self):
        self.driver.find_element_by_xpath(self.more_option_dd_xpath).click()
        self.driver.find_element_by_link_text(self.packages_link).click()

    '''to set source City, Travelling From'''
    def set_source_city(self, city):
        self.driver.find_element_by_xpath(self.sourceField_xpath_click).click()  # to focus on text field
        self.driver.find_element_by_id(self.sourceField_id_text).send_keys(
            ' ' + city)  # extra space as first letter was getting lost
        time.sleep(3)  # as lookup takes time to populate properly
        self.driver.find_element_by_xpath(self.sourceField_xpath_firstresult).click()

    ''' to Set Travelling to City'''
    def set_destination_city(self, city):
        self.driver.find_element_by_xpath(self.destinationField_xpath_click).click()  # to focus on text field
        self.driver.find_element_by_id(self.destinationField_id_text).send_keys(
            ' ' + city)  # extra space as first letter was getting lost
        time.sleep(3)  # as lookup takes time to populate properly
        self.driver.find_element_by_xpath(self.destinationField_xpath_firstresult).click()

    '''to set 1 Adult and 1 kid of age 3'''
    def set_travellers(self):
        self.driver.find_element_by_link_text(self.travellor_btn_link).click()
        time.sleep(2)  #sometimes following steps goes too fast and fails to interact as view is loading
        self.driver.find_element_by_xpath(self.adult_decrease_btn_xpath).click()
        self.driver.find_element_by_xpath(self.child_increase_btn_xpath).click()
        self.driver.find_element_by_xpath(self.child_age_xpath+'/option[2]').click()  #Age 3 is option 2 of DD
        self.driver.find_element_by_xpath(self.traveller_done_btn_xpath).click()

    '''Set of dates one month later, 12->24'''
    def set_dates(self):
        self.driver.find_element_by_id(self.datepicker_id).click()
        time.sleep(2)  #sometimes process goes too fast and calendar don't load properly
        self.driver.find_element_by_xpath(self.next_month_xpath).click()
        self.driver.find_element_by_xpath(self.month_parent_xpath).find_elements_by_class_name(self.month_dates_class)[
            12].click()   #leaving Date
        self.driver.find_element_by_xpath(self.month_parent_xpath).find_elements_by_class_name(self.month_dates_class)[
            24].click()  #return Date
        self.driver.find_element_by_xpath(self.datepicker_done_xpath).click()

    '''Click on Search Button'''
    def click_search_button(self):
        self.driver.find_element_by_xpath(self.search_btn_xpath).click()

    ''' To get Steps 1 from Search result page, expected Step1 choose your hotel'''
    def get_step1_search_results_page(self):
        step1_value =self.driver.find_element_by_xpath('//*[@id="multiStepIndicatorContainer"]/div[1]/div[1]/h3/span[2]').text
        return step1_value
