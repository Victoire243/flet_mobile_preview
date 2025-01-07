# flet-phone-preview

`flet-phone-preview` is a Python package that provides a preview of an iPhone 13 interface using the Flet framework. This package allows you to simulate the appearance of an iPhone 13 on your desktop, making it easier to design and test mobile interfaces.

## Installation

You can install the package using pip:

```bash
pip install flet-phone-preview
```

## Usage

Here is an example of how to use the `flet-phone-preview` package:

```python
import flet as ft
from flet_phone_preview.iPhone import iPhone13

def main(page: ft.Page):
    def change_text_color(e):
        text.color = ft.Colors.random(exclude=["white"])
        text.update()

    phone = iPhone13(page=page, zoom=1)

    text = ft.Text("Hello Flet Devs", weight="bold", size=18, color="black")

    phone.body = ft.Column(
        controls=[text],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
        width=float("inf"),
    )

    phone.appBar = ft.AppBar(
        title=ft.Text("Flet App", size=16, color="white", weight="bold"),
        bgcolor="blue",
        leading=ft.Icon(ft.Icons.MENU, color="white"),
        actions=[
            ft.Icon(
                ft.Icons.NOTIFICATIONS,
                color="white",
                offset=ft.Offset(-0.5, 0),
            )
        ],
    )

    phone.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.CHANGE_CIRCLE,
        bgcolor="blue",
        shape=ft.CircleBorder(),
        tooltip="Click to change text color",
        on_click=change_text_color,
    )

    phone.run()

ft.app(target=main)
```

### Changing the Title Bar and Phone Bar Colors

You can customize the colors of the title bar and phone bar by setting the `bg_color_title_bar` and `color_title_bar` attributes of the `iPhone13` class. Here is an example:

```python
import flet as ft
from flet_phone_preview.iPhone import iPhone13

def main(page: ft.Page):
    phone = iPhone13(page=page, zoom=1)

    phone.bg_color_title_bar = "green"
    phone.color_title_bar = "yellow"

    phone.run()

ft.app(target=main)
```

### Customizing the Frame Color and Buttons of Frame Color

You can also customize the frame color and the buttons of the frame color by setting the `color_frame` and `color_buttons_frame` attributes. Here is an example:

```python
import flet as ft
from flet_phone_preview.iPhone import iPhone13

def main(page: ft.Page):
    phone = iPhone13(page=page, zoom=1)

    phone.color_frame = "purple"
    phone.color_buttons_frame = "orange"

    phone.run()

ft.app(target=main)
```

### Adding a Floating Action Button and App Bar

You can add a floating action button and an app bar to the iPhone preview. Here is an example:

```python
import flet as ft
from flet_phone_preview.iPhone import iPhone13

def main(page: ft.Page):
    def change_text_color(e):
        text.color = ft.Colors.random(exclude=["white"])
        text.update()

    phone = iPhone13(page=page, zoom=1)

    text = ft.Text("Hello Flet Devs", weight="bold", size=18, color="black")

    phone.body = ft.Column(
        controls=[text],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
        width=float("inf"),
    )

    phone.appBar = ft.AppBar(
        title=ft.Text("Flet App", size=16, color="white", weight="bold"),
        bgcolor="blue",
        leading=ft.Icon(ft.Icons.MENU, color="white"),
        actions=[
            ft.Icon(
                ft.Icons.NOTIFICATIONS,
                color="white",
                offset=ft.Offset(-0.5, 0),
            )
        ],
    )

    phone.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.CHANGE_CIRCLE,
        bgcolor="blue",
        shape=ft.CircleBorder(),
        tooltip="Click to change text color",
        on_click=change_text_color,
    )

    phone.run()

ft.app(target=main)
```

## Features

- Simulate the appearance of an iPhone 13 on your desktop.
- Minimize, update, and close the preview window.
- Customize the title bar and phone bar colors.
- Customize the frame color and buttons of frame color
- Add floating action button and app bar.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on [GitHub](https://github.com/Victoire243/flet_mobile_preview).

## Author

This package is developed by [Victoire243](https://github.com/Victoire243).

## Acknowledgements

Special thanks to @Salakhddinov for giving the idea to create this package.
