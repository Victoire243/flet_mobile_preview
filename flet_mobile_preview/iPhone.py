import flet as ft


class iPhone13:
    """
    A class to simulate the appearance of an iPhone 13 using the Flet framework.
    """

    def __init__(self, page: ft.Page, zoom: int = 1) -> None:
        """
        Initialize the iPhone13 class.

        Args:
            page (ft.Page): The Flet page object.
            zoom (int): The zoom level (0 for small, 1 for large).
        """
        self.page = page
        self.__zoom = zoom

        # Set window properties
        self.page.window.always_on_top = True
        self.page.bgcolor = "transparent"
        self.page.window.bgcolor = "transparent"
        self.page.window.frameless = True
        self.page.window.title_bar_hidden = True
        self.page.padding = 0
        self.__initialize_zoom()

        # Set window dimensions
        self.page.window.height = self.__height
        self.page.window.width = self.__width
        self.bg_color_title_bar = "blue"
        self.color_title_bar = "white"
        self.page.fonts = {"iphone": "fonts/sf.otf"}
        self.page.theme = ft.Theme(font_family="iphone")

        # Initialize screen content
        self.screen = ft.Pagelet(content=ft.Container())

    def __initialize_zoom(self):
        """
        Initialize dimensions based on the zoom level.
        """
        if self.__zoom == 0:
            self.__width = 247.86
            self.__height = 488.43
            self.__phone_bar_top = 10
            self.__body_top = 27
            self.__body_width = 55
            self.__body_height = 95
            self.__title_bar_padding = 5
            self.__phone_bar_width = 55
            self.__phone_bar_padding = 15
            self.__phone_bar_height = 17
            self.__body_padding_left = 2
            self.__body_padding_right = 0
            self.__body_padding_bottom = 0
            self.page.window.width = self.__width
            self.page.window.height = self.__height
        else:
            self.__height = 670
            self.__width = 340
            self.__phone_bar_top = 15
            self.__body_top = 40
            self.__body_width = 60
            self.__body_height = 110
            self.__title_bar_padding = 20
            self.__phone_bar_width = 60
            self.__phone_bar_padding = 25
            self.__phone_bar_height = 25
            self.__body_padding_left = 7
            self.__body_padding_right = 2
            self.__body_padding_bottom = 2

    def __body(self):
        """
        Create the body of the phone.

        Returns:
            ft.Container: The body container.
        """
        return ft.Container(
            bgcolor="white",
            height=self.__height - self.__body_height,
            width=self.__width - self.__body_width,
            border_radius=ft.border_radius.only(bottom_left=20, bottom_right=20),
            top=self.__body_top,
            content=self.screen,
            padding=ft.padding.only(
                left=self.__body_padding_left,
                right=self.__body_padding_right,
                bottom=self.__body_padding_bottom,
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
                        ft.Row(
                            controls=[
                                ft.IconButton(
                                    icon=ft.Icons.ADD_CIRCLE,
                                    icon_color="blue",
                                    icon_size=25,
                                    tooltip="Zoom in",
                                    on_click=self.__zoom_in,
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.REMOVE_CIRCLE,
                                    icon_color="blue",
                                    icon_size=25,
                                    tooltip="Zoom out",
                                    on_click=self.__zoom_out,
                                ),
                            ],
                            spacing=3,
                            tight=True,
                            alignment="end",
                            expand=True,
                        ),
                    ],
                ),
            )
        )

    def __zoom_out(self, e):
        """
        Zoom out to smaller dimensions.

        Args:
            e: The event object.
        """
        self.__width = 247.86
        self.__height = 488.43
        self.__phone_bar_top = 10
        self.__body_top = 27
        self.__body_width = 55
        self.__body_height = 95
        self.__title_bar_padding = 5
        self.__phone_bar_width = 55
        self.__phone_bar_padding = 15
        self.__phone_bar_height = 17
        self.__body_padding_left = 2
        self.__body_padding_right = 0
        self.__body_padding_bottom = 0
        self.page.window.width = self.__width
        self.page.window.height = self.__height

        self.run()

    def __zoom_in(self, e):
        """
        Zoom in to larger dimensions.

        Args:
            e: The event object.
        """
        self.__height = 670
        self.__width = 340
        self.__phone_bar_top = 15
        self.__body_top = 40
        self.__body_width = 60
        self.__body_height = 110
        self.__title_bar_padding = 20
        self.__phone_bar_width = 60
        self.__phone_bar_padding = 25
        self.__phone_bar_height = 25
        self.__body_padding_left = 7
        self.__body_padding_right = 2
        self.__body_padding_bottom = 2
        self.page.window.width = self.__width
        self.page.window.height = self.__height

        self.run()

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
            height=self.__phone_bar_height,
            width=self.__width - self.__phone_bar_width,
            top=self.__phone_bar_top,
            border_radius=ft.border_radius.only(top_left=200, top_right=200),
            padding=ft.padding.symmetric(horizontal=self.__phone_bar_padding),
            content=ft.Row(
                controls=[
                    ft.Text("6:30", color=self.color_title_bar),
                    ft.Row(
                        controls=[
                            ft.Icon(ft.Icons.WIFI, color=self.color_title_bar, size=15),
                            ft.Icon(
                                ft.Icons.BATTERY_STD,
                                color=self.color_title_bar,
                                rotate=ft.Rotate(3.14 / 2),
                                size=15,
                            ),
                        ],
                        spacing=4,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
        )

    def __frame(self):
        """
        Create the frame with body and phone bar.

        Returns:
            ft.Stack: The frame stack.
        """
        return ft.Stack(
            controls=[
                self.__body(),
                self.__phone_bar(),
                ft.TransparentPointer(
                    content=ft.Image(
                        src="flet_mobile_preview/assets/images/iphone13.png",
                        height=self.__height - 60,
                        width=self.__width,
                    ),
                ),
            ],
            alignment=ft.alignment.top_center,
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
