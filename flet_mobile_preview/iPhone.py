import flet as ft


class iPhone13:
    """
    A class to simulate the appearance of an iPhone 13 using the Flet framework.
    """

    def __init__(self, page: ft.Page, zoom: float | int = 1) -> None:
        """
        Initialize the iPhone13 class.

        Args:
            page (ft.Page): The Flet page object.
            zoom (float | int): The zoom level (value between 0.5 and 3).
        """
        self.page = page
        self.__zoom = zoom

        # Set window properties
        self.page.window.always_on_top = True
        self.page.bgcolor = "transparent"
        self.page.window.bgcolor = "transparent"
        self.page.window.frameless = True
        self.page.window.title_bar_hidden = True
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.padding = ft.padding.all(0)
        self.__initialize_zoom()

        # Package Assets path
        self.__assets_src = (
            __file__.split("\\") if __file__.__contains__("\\") else __file__.split("/")
        )
        self.__assets_src = "/".join(self.__assets_src[:-1]) + "/assets/"

        # Set window dimensions
        self.page.window.width = self.__width * 1.05
        self.bg_color_title_bar: str = "blue"
        self.color_title_bar: str = "white"
        self.color_frame: str = "#4288B1"
        self.color_buttons_frame: str = "#A1C4D8"
        self.page.fonts = {"iphone": self.__assets_src + "fonts/sf.otf"}
        self.page.theme = ft.Theme(font_family="iphone")

        # Initialize app content
        self.body: ft.Control = ft.Container(
            alignment=ft.alignment.center,
            content=ft.Text(
                value="Hello Flet devs",
                size=18,
                weight=ft.FontWeight.BOLD,
            ),
        )

        # Others app Controls
        self.appBar: ft.AppBar = None
        self.floating_action_button: ft.FloatingActionButton = None

    def __initialize_zoom(self):
        """
        Initialize dimensions based on the zoom level.
        """
        if 0.5 < self.__zoom < 3:
            self.__height = 642.752 * self.__zoom
            self.__width = 311.3055 * self.__zoom
        else:
            self.__height = 642.752
            self.__width = 311.3055

        self.__title_bar_padding = 10
        self.__phone_bar_padding = 30
        self.__body_padding_left = 12
        self.__body_padding_right = 12
        self.__body_padding_bottom = 12

    def __body(self):
        """
        Create the body of the phone.

        Returns:
            ft.Container: The body container.
        """
        return ft.Pagelet(
            content=self.body,
            appbar=self.appBar if isinstance(self.appBar, ft.AppBar) else None,
            floating_action_button=(
                self.floating_action_button
                if isinstance(self.floating_action_button, ft.FloatingActionButton)
                else None
            ),
        )

    def __title_bar(self):
        """
        Create the title bar with control buttons.

        Returns:
            ft.WindowDragArea: The title bar area.
        """
        return ft.WindowDragArea(
            content=ft.Container(
                bgcolor="white",
                height=50,
                border_radius=10,
                width=self.__width * 1.05,
                padding=ft.padding.symmetric(horizontal=self.__title_bar_padding),
                content=ft.Row(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Container(
                                    height=20,
                                    width=20,
                                    bgcolor="orange",
                                    border_radius=100,
                                    tooltip="Minimize",
                                    on_click=self.__minimize,
                                ),
                                ft.Container(
                                    height=20,
                                    width=20,
                                    bgcolor="green",
                                    border_radius=100,
                                    tooltip="Update",
                                    on_click=lambda _: self.page.update(),
                                ),
                                ft.Container(
                                    height=20,
                                    width=20,
                                    bgcolor="red",
                                    border_radius=100,
                                    tooltip="Close",
                                    on_click=lambda _: self.page.window.close(),
                                ),
                            ],
                            spacing=5,
                        ),
                        ft.Column(
                            controls=[
                                ft.Text(
                                    "iPhone 13",
                                    weight="bold",
                                    color="black",
                                    size=16,
                                ),
                                ft.Text(
                                    "Preview",
                                    color="#868686",
                                    size=14,
                                ),
                            ],
                            spacing=0,
                            tight=True,
                            alignment="center",
                        ),
                    ],
                ),
            )
        )

    def __minimize(self, e):
        """
        Minimize the window.

        Args:
            e: The event object.
        """
        self.page.window.minimized = True
        self.page.update()

    def __phone_bar(self):
        """
        Create the phone bar with time and icons.

        Returns:
            ft.Container: The phone bar container.
        """
        return ft.Container(
            bgcolor=self.bg_color_title_bar,
            alignment=ft.alignment.center,
            padding=ft.padding.only(
                left=self.__phone_bar_padding, top=10, right=self.__phone_bar_padding
            ),
            height=35,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Text("6:30", color=self.color_title_bar, size=12),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Icon(
                                name=ft.Icons.WIFI,
                                color=self.color_title_bar,
                                size=14,
                            ),
                            ft.Icon(
                                name=ft.Icons.BATTERY_FULL,
                                color=self.color_title_bar,
                                size=14,
                                rotate=3.14 / 2,
                            ),
                        ],
                    ),
                ],
            ),
        )

    def __frame(self):
        """
        Create the frame with body and phone bar.

        Returns:
            ft.Stack: The frame stack.
        """
        return ft.Stack(
            alignment=ft.alignment.top_center,
            controls=[
                ft.Container(
                    height=self.__height,
                    width=self.__width,
                    bgcolor="white",
                    border_radius=ft.border_radius.all(40),
                    clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                    alignment=ft.alignment.center,
                    content=ft.Stack(
                        expand=True,
                        alignment=ft.alignment.top_center,
                        controls=[
                            ft.Container(
                                bgcolor="white",
                                height=self.__height - 35,
                                width=self.__width,
                                padding=ft.padding.only(
                                    left=self.__body_padding_left,
                                    right=self.__body_padding_right,
                                    bottom=self.__body_padding_bottom,
                                    top=0,
                                ),
                                bottom=0,
                                content=self.__body(),
                            ),
                            self.__phone_bar(),
                            ft.TransparentPointer(
                                ft.Container(
                                    bgcolor="transparent",
                                    border=ft.border.all(
                                        width=13,
                                        color="black",
                                    ),
                                    border_radius=ft.border_radius.all(40),
                                )
                            ),
                            ft.TransparentPointer(
                                ft.Container(
                                    width=self.__width * 0.35,
                                    height=35,
                                    bgcolor="black",
                                    expand=False,
                                    border_radius=ft.border_radius.only(
                                        bottom_left=15, bottom_right=15
                                    ),
                                    alignment=ft.alignment.center_left,
                                    padding=ft.padding.only(left=10),
                                    content=ft.Container(
                                        height=10,
                                        width=10,
                                        border_radius=ft.border_radius.all(20),
                                        margin=ft.margin.only(top=8),
                                        gradient=ft.RadialGradient(
                                            colors=["#FFFFFF", "#91AEFD", "#001A49"],
                                            focal=ft.alignment.center_left,
                                        ),
                                    ),
                                )
                            ),
                            ft.Container(
                                width=self.__width * 0.2,
                                height=2,
                                bgcolor="#292929",
                                border_radius=ft.border_radius.all(10),
                                top=7,
                            ),
                            ft.TransparentPointer(
                                ft.Container(
                                    bgcolor="transparent",
                                    border=ft.border.all(
                                        width=4,
                                        color=self.color_frame,
                                    ),
                                    border_radius=ft.border_radius.all(40),
                                )
                            ),
                        ],
                    ),
                ),
                ft.Container(
                    bgcolor=self.color_buttons_frame,
                    height=75,
                    width=3,
                    border_radius=ft.border_radius.only(top_right=50, bottom_right=50),
                    right=0,
                    top=self.__height * 0.31,
                    offset=ft.Offset(1, 0),
                ),
                ft.Container(
                    bgcolor=self.color_buttons_frame,
                    height=25,
                    width=3,
                    border_radius=ft.border_radius.only(top_left=50, bottom_left=50),
                    left=0,
                    top=self.__height * 0.19,
                    offset=ft.Offset(-1, 0),
                ),
                ft.Container(
                    bgcolor=self.color_buttons_frame,
                    height=50,
                    width=3,
                    border_radius=ft.border_radius.only(top_left=50, bottom_left=50),
                    left=0,
                    top=self.__height * 0.27,
                    offset=ft.Offset(-1, 0),
                ),
                ft.Container(
                    bgcolor=self.color_buttons_frame,
                    height=50,
                    width=3,
                    border_radius=ft.border_radius.only(top_left=50, bottom_left=50),
                    left=0,
                    top=self.__height * 0.37,
                    offset=ft.Offset(-1, 0),
                ),
            ],
        )

    def run(self):
        """
        Run the application.
        """
        body = self.__frame()
        title_bar = self.__title_bar()
        self.page.controls.clear()
        self.page.add(title_bar, body)
        self.page.update()
