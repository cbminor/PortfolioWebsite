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

IMAGE_PLACEMENT = [
    ("left", "left"),
    ("right", "right")
]

IMAGE_COL_WIDTH = [
    ("col-3", "25%"),
    ("col-4", "33%"),
    ("col-6", "50%"),
    ("col-8", "66%"),
    ("col-9", "75%")
]

TEXT_COLORS = [
    ("white", "White"),
    ("black", "Black")
]

IMAGE_WIDTH = [
    ("w-50", "50%"),
    ("w-60", "60%"),
    ("w-70", "70%"),
    ("w-75", "75%"),
    ("w-80", "80%"),
    ("w-90", "90%"),
    ("w-100", "100%")
]

IMAGE_CORNERS = [
    ("rounded-0", "Sharp"),
    ("rounded-2", "Slightly Round"),
    ("rounded-4", "Medium Round"),
    ("rounded-5", "Very Round"),
    ("rounded-circle", "Circle")
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
    image_width = blocks.ChoiceBlock(choices=IMAGE_WIDTH, default="100%")
    image_corners = blocks.ChoiceBlock(choices=IMAGE_CORNERS, default="Sharp")

    class Meta:
        icon = "card-image"
        template = "home/blocks/image_block.html"


class InlineImageTextBlock(blocks.StructBlock):
    """ A block to display text inline with an image """
    
    image = ImageBlock()
    text = blocks.RichTextBlock()
    placement = blocks.ChoiceBlock(choices=IMAGE_PLACEMENT, default="left")
    image_col_width = blocks.ChoiceBlock(choices=IMAGE_COL_WIDTH, default="50%")
    image_corners = blocks.ChoiceBlock(choices=IMAGE_CORNERS, default="Sharp")
    photo_description = blocks.CharBlock(required=False, max_length=150)

    class Meta:
        icon = "card-image"
        template = "home/blocks/inline_image_text_block.html"

class TwoColumnTextBlock(blocks.StructBlock):
    """ Creates a block with two column content """

    text_block_left = blocks.RichTextBlock(features=['h2','h3','h4', 'bold', 'italic', 'underline', 'ol', 'ul', 'hr', 'link', 'document-link', 'embed'])
    text_block_right = blocks.RichTextBlock(features=['h2','h3','h4', 'bold', 'italic', 'underline', 'ol', 'ul', 'hr', 'link', 'document-link', 'embed'])

    class Meta:
        icon = "card-image"
        template = "home/blocks/two_column_text_block.html"
