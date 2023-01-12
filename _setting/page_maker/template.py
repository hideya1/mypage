import os, sys
sys.path.append(os.path.dirname(__file__))
from conf import *
import conf_ja
from myapp.htmlmanager import *
from myapp.jsonmanager import JsonManager


class Template(Composite):
    def __init__(self, tab_title, base_link, active_menu, art) -> None:
        self.head = head_template(tab_title, base_link, css_link=MY_STYLE_PATH)
        header = header_logo_title(
                        logo_path=LOGO_IMG_PATH,
                        title="Hideya Watanabe",
                        link=base_link
                    )
        header.children[0].children[0].set_attr("class", "header_inner flexContainer__spaceBetween")
        header.children[0].children[0].append_child(
            Nav(attrs={"class": "menu"}, children=[
                Ul(children=[
                    Li(children=[
                        A(attrs={"class": "is_active noBorder"}, children=["English"])
                    ]),
                    Li(children=[
                        A(attrs={"class": "noBorder", "href": conf_ja.MENU[active_menu]["url"]}, children=["日本語"])
                    ])
                ])
            ])
        )
        header.append_child(menu(menu_data=MENU, active_menu=active_menu))
        self.node = Page(
            root = Root(
                lang="en",
                head = self.head,
                body=Page_Body(
                    header=header,
                    main=main([
                        art
                    ]),
                    footer=footer(["contact: watanabehideya [at] gmail.com"])
                ).node
            ).node
        ).node

