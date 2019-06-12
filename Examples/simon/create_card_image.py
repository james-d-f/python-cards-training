from PIL import Image, ImageDraw, ImageFont
from card import Card


def create_card_image(card) -> Image:
    image_width = 600
    image_height = 900
    light_grey = (240, 240, 240)
    dark_grey = (30, 30, 20)
    dark_red = (220, 30, 20)
    suit_colour = dark_grey if card.suit in "♣♠" else dark_red
    font = ImageFont.truetype("Apple Symbols.ttf", size=120)

    card_image = Image.new("RGB", (image_width, image_height), color=light_grey)
    inputImage = Image.open("src/images/varys.png")
    inputImage = inputImage.convert("RGB")
    inputImage = inputImage.resize((image_width, image_height), Image.ANTIALIAS)
    blendedImage = Image.blend(card_image, inputImage, 0.9)
    draw = ImageDraw.Draw(blendedImage)
    draw.text((60, 60), f"{card.rank}{card.suit}", fill=suit_colour, font=font)

    return blendedImage


if __name__ == "__main__":
    image = create_card_image(Card.random())
    image.show()
