# ComfyUI-TextOverlay

A custom node for ComfyUI that adds text overlay to images, with options for text and background color, opacity, vertical positioning, and custom font selection.

![shapes](./Example%20Images/sample.png)

## Features
- Add customizable text overlays to images
- Choose from predefined text and background colors
- Adjust background opacity
- Control vertical positioning of the text
- Use custom fonts by specifying the font file path

## Installation
1. Clone this repository into your ComfyUI custom_nodes folder:

   ```bash
   git clone https://github.com/neeltheninja/ComfyUI-TextOverlay.git
   ```
2. Restart ComfyUI or reload custom nodes

## Usage
1. In ComfyUI, add the "Add Text Overlay" node to your workflow
2. Connect an image input to the node
3. Set your desired text, colors, positioning options, and font path
4. Run your workflow to see the result!

## Parameters
- `image`: Input image
- `text`: Text to overlay on the image
- `vertical_position`: Vertical position of the text (-1 to 1)
- `text_color_option`: Color of the text (White, Black, Red, Green, Blue)
- `bg_color_option`: Color of the background (Black, White, Red, Green, Blue)
- `bg_opacity`: Opacity of the background (0 to 1)
- `font_path`: Path to the TTF font file

## License
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.