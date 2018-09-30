from base.base import Base
import page
class Page(Base):

    def page_click_sec(self):
        self.base_click(page.search_bth)
    def page_input_text(self,text):
        self.base_input_sc(page.input_search,text)
    def page_click_back(self):
        self.base_click(page.back_btn)