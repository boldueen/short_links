from app.core.config import ALLOWED_SYMBOLS_IN_LINK


allowed_symbols = list(ALLOWED_SYMBOLS_IN_LINK)


def get_short_link(link_ordinal_number: int):
    short_link = ''
    new_number = []

    while link_ordinal_number != 0:
        short_link += allowed_symbols[(link_ordinal_number%len(allowed_symbols))-1]
        new_number.append(link_ordinal_number%len(allowed_symbols))
        link_ordinal_number//=len(allowed_symbols)

    new_number = new_number[::-1]

    return short_link[::-1]
