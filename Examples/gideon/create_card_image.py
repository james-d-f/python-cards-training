from PIL import Image, ImageDraw, ImageFont
from card import Card


def create_card_image(card: Card) -> Image:
    image_width = 500
    image_height = 800
    dark_grey = (30, 30, 30)
    dark_red = (220, 30, 20)
    dark_blue = (89, 66, 244)
    green = (38, 173, 58)
    suit_colour = dark_grey if card.suit in "♣♠" else dark_red
    font = ImageFont.truetype("Apple Symbols.ttf", size=120)
    drawing_coords = {
        (80, 80): 'rank',
        (360, 80): 'suit',
        }

    card_image = Image.new("RGB", (image_width, image_height))
    d = ImageDraw.Draw(card_image)
    d.rectangle([(0, 0), (image_width, image_height)], fill=green)
    for coordinates, shape in drawing_coords.items():
        d.text(coordinates, f"{getattr(card, shape)}", fill=suit_colour, font=font)
    d.rectangle([(15, 15), (485, 785)], outline=dark_blue, width=7)
    flipped_card = card_image.rotate(180)
    f = ImageDraw.Draw(flipped_card)
    for coordinates, shape in drawing_coords.items():
        f.text(coordinates, f"{getattr(card, shape)}", fill=suit_colour, font=font)
    return flipped_card


if __name__ == "__main__":
    image = create_card_image(Card.random())
    image.show()
