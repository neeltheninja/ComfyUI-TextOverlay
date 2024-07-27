import torch
import torchvision.transforms.functional as TF
from PIL import Image, ImageDraw, ImageFont
import numpy as np

class TextOverlay:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "text": ("STRING", {"multiline": True}),
                "vertical_position": ("FLOAT", {"default": 0, "min": -1, "max": 1, "step": 0.1}),
                "text_color_option": (["White", "Black", "Red", "Green", "Blue"],),
                "bg_color_option": (["Black", "White", "Red", "Green", "Blue"],),
                "bg_opacity": ("FLOAT", {"default": 0.5, "min": 0, "max": 1, "step": 0.1}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "apply_text_overlay"

    COLOR_OPTIONS = {
        "White": (255, 255, 255),
        "Black": (0, 0, 0),
        "Red": (255, 0, 0),
        "Green": (0, 255, 0),
        "Blue": (0, 0, 255)
    }

    def apply_text_overlay(self, image, text, vertical_position, text_color_option, bg_color_option, bg_opacity):
        # Convert torch tensor to numpy array
        image_np = image.squeeze().cpu().numpy()

        # Ensure the image is in the correct format (H, W, C)
        if image_np.shape[0] == 3:
            image_np = np.transpose(image_np, (1, 2, 0))

        # Convert to PIL Image
        image_pil = Image.fromarray((image_np * 255).astype(np.uint8))

        # Create a drawing object
        draw = ImageDraw.Draw(image_pil, 'RGBA')

        # Load a font
        font_size = image_pil.height // 20
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", font_size)

        # Calculate text position
        text_width, text_height = draw.textsize(text, font=font)
        x = (image_pil.width - text_width) // 2
        y = ((image_pil.height - text_height) // 2) + int(vertical_position * image_pil.height / 2)

        # Draw background
        bg_color = self.COLOR_OPTIONS[bg_color_option] + (int(bg_opacity * 255),)
        draw.rectangle([x-10, y-10, x+text_width+10, y+text_height+10], fill=bg_color)

        # Draw text
        draw.text((x, y), text, font=font, fill=self.COLOR_OPTIONS[text_color_option])

        # Convert back to torch tensor
        result = torch.from_numpy(np.array(image_pil).astype(np.float32) / 255.0)
        result = result.unsqueeze(0).permute(0, 3, 1, 2)

        return (result,)

NODE_CLASS_MAPPINGS = {"TextOverlay": TextOverlay}
NODE_DISPLAY_NAME_MAPPINGS = {"TextOverlay": "Add Text Overlay"}
