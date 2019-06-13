from PIL import Image, ImageDraw, ImageFont

from card import Card


def create_card_image(card):
    image_width = 600
    image_height = 900
    light_grey = (240, 240, 240)
    dark_grey = (30, 30, 20)
    dark_red = (220, 30, 20)
    suit_colour = dark_grey if card.suit in "♣♠" else dark_red
    font = ImageFont.truetype("Apple Symbols.ttf", size=150)
    font2 = ImageFont.truetype("Apple Symbols.ttf", size=320)

    card_image = Image.new("RGB", (image_width, image_height), color=light_grey)
    text_image = Image.new("RGB", (250, 150), color=light_grey)
    draw_text = ImageDraw.Draw(text_image)

    draw = ImageDraw.Draw(card_image)

    draw.text((60, 60), f"{card.rank}{card.suit}", fill=suit_colour, font=font)
    draw.text((190, 310), f"{card.suit}", fill=suit_colour, font=font2)
    draw_text.text((2, 2), f"{card.rank}{card.suit}", fill=suit_colour, font=font)
    x = text_image.rotate(180)
    card_image.paste(x, box=(300, 700))

    return card_image


if __name__ == "__main__":
    image = create_card_image(Card.random())
    image.show()
