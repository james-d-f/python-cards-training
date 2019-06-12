from card import Card

from PIL import Image, ImageDraw, ImageFont


def create_card_image(card: Card) -> Image:
    image_width = 600
    image_height = 900
    light_grey = (240, 240, 240)
    dark_grey = (30, 30, 20)
    dark_red = (220, 30, 20)
    suit_colour = dark_grey if card.suit in "♣♠" else dark_red
    font = ImageFont.truetype("Apple Symbols.ttf", size=120)
    border = 20
    repr_size = 60

    card_image = Image.new("RGB", (image_width, image_height), color=light_grey)
    for i in range(2):
        draw = ImageDraw.Draw(card_image)
        draw.text(
            (repr_size, repr_size),
            f"{card.rank}{card.suit}",
            fill=suit_colour,
            font=font,
        )

        card_image = card_image.rotate(180)

    draw = ImageDraw.Draw(card_image)
    draw.rectangle(
        [(border, border), (image_width - border, image_height - border)],
        outline=suit_colour,
    )

    return card_image


if __name__ == "__main__":
    image = create_card_image(Card.random_card())
    image.show()
