from seleniumbase import BaseCase


class TestHomePage(BaseCase):
    def test_verify_page_title_and_url(self):
        # open home page
        self.open('https://practice-react.sdetunicorns.com/')

        # assert url and title contains SDET Unicorns
        self.assert_url_contains('sdetunicorns')
        self.assert_title_contains(' SDET Unicorns')

    def test_search_flow_with_css_selector(self):
        # open home page
        self.open('https://practice-react.sdetunicorns.com/')

        # click on the search input field
        self.click('.search-active')

        # type dell in the search input field
        self.type("[placeholder='Search']", text='Dell')

        # click on search button
        self.click('.button-search')

        # assert the text is visible
        self.assert_text_visible('Showing Results for Dell')

    def test_search_flow_with_xpath(self):
        # open home page
        self.open('https://practice-react.sdetunicorns.com/')

        # click on the search input field
        self.click("//button[@class='search-active']")

        # type dell in the search input field
        self.type("//input[@placeholder='Search']", text='Dell')

        # click on search button
        self.click("//button[@class='button-search']")

        # assert the text is visible
        self.assert_text_visible('Showing Results for Dell')

    def test_nav_links(self):
        # open home page
        self.open('https://practice-react.sdetunicorns.com/')

        # assert the text link 'Products'
        self.assert_text('Products', '.main-menu li:nth-child(2)')

        # link text collection of values
        expected_nav_text = ['Home', 'Products', 'About Us', 'Contact', 'Upload']

        # assert the link text from 1 to 5
        for i, text in enumerate(expected_nav_text, start=1):
            # print(i, text)
            self.assert_text(text, f'.main-menu li:nth-child({i})')

    def test_click_about_us_lick_and_verify_url(self):
        # open home page
        self.open('https://practice-react.sdetunicorns.com/')

        # click the "About Us" link
        self.click('.footer-list [href="/about"]')

        # assert the url contains about
        self.assert_url_contains('about')
