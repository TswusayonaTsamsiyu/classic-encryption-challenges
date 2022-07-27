from typing import Callable
from inspect import getmodule
from flask import Blueprint, Flask

_CHALLENGES = []


def _get_url_prefix():
    return f"/{len(_CHALLENGES) + 1}"


def _create_blueprint(module: str) -> Blueprint:
    return Blueprint(module.split(".")[-1], module, url_prefix=_get_url_prefix())


def _register_urls(blueprint: Blueprint, encryption: Callable, hint: str) -> Blueprint:
    blueprint.add_url_rule("/encrypt/<plain>", view_func=encryption)
    blueprint.add_url_rule("/hint", view_func=lambda: hint)
    return blueprint


def register_challenge(encryption: Callable, hint: str):
    _CHALLENGES.append(_register_urls(_create_blueprint(getmodule(encryption).__name__), encryption, hint))


def register_blueprints(app: Flask):
    for challenge in _CHALLENGES:
        app.register_blueprint(challenge)
