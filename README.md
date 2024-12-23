# flet_mobile_preview

`flet_mobile_preview` is a Python package that provides a preview of an iPhone 13 interface using the Flet framework. This package allows you to simulate the appearance of an iPhone 13 on your desktop, making it easier to design and test mobile interfaces.

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
    phone = iPhone13(page)
    phone.screen.appbar = ft.AppBar(
        bgcolor="bleu",
        title=ft.Text("Hello App", color="white"),
    )
    phone.screen.content = ft.Container(
        content=ft.Text("Hello, World!", size=20),
    )
    phone.run()

ft.app(target=main)
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

## Author

This package is developed by [Victoire243](https://github.com/Victoire243).

## Acknowledgements

Special thanks to @Salakhddinov for giving the idea to create this package.
