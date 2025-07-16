from wagtail import blocks
from django.db import models
from wagtail.images.blocks import ImageBlock

CARD_COLORS = [
    ("#ac5625", "Orange"),
    ("#b48351", "Beige"),
    ("#b5aba6", "Tan"),
    ("#483a2b", "Brown"),
    ("#666666", "Gray")
]

IMAGE_ALIGNMENT = [
    ("text-center", "center"),
    ("text-start", "left"),
    ("text-end", "right")
]

TEXT_COLORS = [
    ("white", "White"),
    ("black", "Black")
]

class ThreeCardDisplayBlock(blocks.StructBlock):
    """ A StructBlock for rendering a Three Card Home page display """

    # Left Image Card
    left_card_image  = ImageBlock(required=False)
    left_card_color = blocks.ChoiceBlock(choices=CARD_COLORS)
    left_card_text = blocks.CharBlock(required=False, max_length=20)

    # Center Image Card
    center_card_image  = ImageBlock(required=False)
    center_card_color = blocks.ChoiceBlock(choices=CARD_COLORS)
    center_card_text = blocks.CharBlock(required=False, max_length=25)

    # Right Image Card
    right_card_image  = ImageBlock(required=False)
    right_card_color = blocks.ChoiceBlock(choices=CARD_COLORS)
    right_card_text = blocks.CharBlock(required=False, max_length=20)

    class Meta:
        icon = "tablet-alt"
        template = "home/blocks/three_card_display.html"


class CustomImageBlock(blocks.StructBlock):
    """ Expands the image block to allow the user to choose the image alignment """

    image = ImageBlock(required=True)
    alignment = blocks.ChoiceBlock(choices=IMAGE_ALIGNMENT, default="center")
    photo_description = blocks.CharBlock(required=False, max_length=150)

    class Meta:
        icon = "card-image"
        template = "home/blocks/image_block.html"
