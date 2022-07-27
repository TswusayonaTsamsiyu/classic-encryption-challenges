import requests


def _get_verse_data(chapter: int, verse: int) -> dict:
    return requests.get(f"https://api.quran.com/api/v4/verses/by_key/{chapter}:{verse}?words=true").json()["verse"]


def _is_word(word: dict) -> bool:
    return word["char_type_name"] == "word"


def get_verse_words(chapter: int, verse: int) -> filter:
    return filter(_is_word, _get_verse_data(chapter, verse)["words"])
