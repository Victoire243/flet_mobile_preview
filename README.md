# flet_mobile_preview

`flet_mobile_preview` is a Python package that provides a preview of an iPhone 13 interface using the Flet framework. This package allows you to simulate the appearance of an iPhone 13 on your desktop, making it easier to design and test mobile interfaces.

Don't  use this package on production !

## Installation

You can install the package using pip:

```bash
pip install flet-mobile-preview
```

## Usage

Here is an example of how to use the `flet_mobile_preview` package:

```python
import flet as ft
from flet_mobile_preview.iPhone import iPhone13

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


ft.app(main)
```

## Features

- Simulate the appearance of an iPhone 13 on your desktop.
- Zoom in and out to adjust the preview size.
- Minimize, update, and close the preview window.
- Customize the title bar and phone bar colors.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.
[Flet-Mobile-Preview](https://github.com/Victoire243/flet_mobile_preview)

## Author

This package is developed by [Victoire243](https://github.com/Victoire243).

## Acknowledgements

Special thanks to @Salakhddinov for giving the idea to create this package.
