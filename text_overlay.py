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
        # TODO: Implement text overlay functionality
        return (image,)
