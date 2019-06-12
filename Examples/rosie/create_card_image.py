from __future__ import annotations
from PIL import Image, ImageDraw, ImageFont
import math

from card import Card


def create_card_image(card: Card) -> Image:
    """creates image of card"""
    image_width = 600
    image_height = 900
    light_grey = (240, 240, 240)
    dark_grey = (30, 30, 20)
    dark_red = (220, 30, 20)
    suit_colour = dark_grey if card.suit in "♣♠" else dark_red
    font = ImageFont.truetype("Apple Symbols.ttf", size=80)
    font_ace = ImageFont.truetype("Apple Symbols.ttf", size=300)

    card_image = Image.new("RGB", (image_width, image_height), color=light_grey)

    # create image of the text for corner of card, and image of this text rotated
    text_image = Image.new("RGB", (200, 100), color=light_grey)
    draw_text = ImageDraw.Draw(text_image)
    draw_text.text((2, 2), f"{card.rank}{card.suit}", fill=suit_colour, font=font)
    text_image_rotated = text_image.rotate(180)

    # put text onto card
    card_image.paste(text_image, (70, 70))
    card_image.paste(text_image_rotated, (330, 730))

    # add border
    draw = ImageDraw.Draw(card_image)
    draw.rectangle([(50, 50), (550, 850)], outline=suit_colour)

    # make one string for each line of suit pics in middle of card
    text_top = ""
    text_bottom = ""

    # convert rank to a number if needed
    rank = card.rank
    if rank in card.RANK_VALUES:
        rank = str(card.RANK_VALUES[rank])

    # if card is an ace put one big suit picture on
    if rank == 1:
        width_text, height_text = draw.textsize(card.suit, font=font_ace)
        horiz_pos = 300 - (width_text / 2)
        vert_pos = 450 - (height_text / 2)
        draw.text((horiz_pos, vert_pos), card.suit, fill=suit_colour, font=font_ace)
    else:
        # put half the symbols in one line and half in the other
        for i in range(0, int(rank)):
            if i >= math.ceil(int(rank) / 2):
                text_bottom += card.suit
            else:
                text_top += card.suit

        # draw the symbols on, rotate the card and draw the others on
        width_text, height_text = draw.textsize(text_top, font=font)
        horiz_pos = 300 - (width_text / 2)
        vert_pos = 450 - (height_text / 2)
        draw.text((horiz_pos, vert_pos), text_top, fill=suit_colour, font=font)

        card_image = card_image.rotate(180)

        # new draw object for the inverted card
        draw_inverted = ImageDraw.Draw(card_image)

        # recalculate position of text and put on card
        width_text, height_text = draw.textsize(text_bottom, font=font)
        horiz_pos = 300 - (width_text / 2)
        vert_pos = 450 + (height_text / 2)
        position = (horiz_pos, vert_pos)
        draw_inverted.text(position, text_bottom, fill=suit_colour, font=font)

    return card_image


if __name__ == "__main__":
    image = create_card_image(Card.random())
    image.show()
