from PIL import Image, ImageDraw, ImageFont

from card import Card


def create_card_image(card: Card) -> Image:
    image_width = 600
    image_height = 900
    light_grey = (240, 240, 240)
    dark_grey = (30, 30, 20)
    dark_red = (220, 30, 20)
    suit_colour = dark_grey if card.suit in "♣♠" else dark_red

    card_image = Image.new("RGB", (image_width, image_height), color=light_grey)

    font = ImageFont.truetype("Apple Symbols.ttf", size=120)

    for i in range(2):  # range(2) for vertical reflection
        draw = ImageDraw.Draw(card_image)
        # Draw rank and suit
        draw.text((60, 60), f"{card.rank}{card.suit}", fill=suit_colour, font=font)

        # Draw symbols
        symbols_this_rotation = int(card) / 2 + 0.5 * (1 - i)
        text = card.suit * int(symbols_this_rotation)
        h_text, v_text = draw.textsize(text, font)
        h_offset = h_text // 2
        v_offset = (int(card) != 1) * 0.1 * image_height + v_text // 2
        text_position = (image_width // 2 - h_offset, image_height // 2 - v_offset)
        draw.text(text_position, text, fill=suit_colour, font=font)

        card_image = card_image.rotate(180)

    # Draw border
    margin = 20
    rectangle_dimensions = (margin, margin, image_width - margin, image_height - margin)
    draw = ImageDraw.Draw(card_image)
    draw.rectangle(rectangle_dimensions, fill=None, outline=dark_grey, width=10)
    draw.rectangle(rectangle_dimensions, fill=None, outline=dark_red, width=6)
    draw.rectangle(rectangle_dimensions, fill=None, outline=dark_grey, width=4)

    return card_image


if __name__ == "__main__":
    """"Example Usage"""
    jack_of_spades = Card("J", "♠")
    two_of_hearts = Card("2", "♥")
    image = create_card_image(jack_of_spades)
    image.show()
    image = create_card_image(two_of_hearts)
    image.show()
    image = create_card_image(Card("A", "Heart"))
    image.show()
    image = create_card_image(Card.random())
    image.show()
    for card in Card.all():
        image = create_card_image(card)
        image.save(f"Card Images/{card}.png")
