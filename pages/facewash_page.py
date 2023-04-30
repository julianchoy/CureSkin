from pages.base_page import Page


class FaceWashPage(Page):

    def verify_facewash_opened(self, verify_pageopened):
        self.verify_url_contains_query(verify_pageopened)