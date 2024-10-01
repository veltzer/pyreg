"""
The default group of operations that pyreg has
"""
import pylogconf.core
from pytconf import register_endpoint, register_main, config_arg_parse_and_launch
from pyreg.static import DESCRIPTION, APP_NAME, VERSION_STR


@register_endpoint(
    description="Match a collection of regexps against a file",
    configs=[],
)
def match() -> None:
    pass


@register_main(
    main_description=DESCRIPTION,
    app_name=APP_NAME,
    version=VERSION_STR,
)
def main():
    pylogconf.core.setup()
    config_arg_parse_and_launch()


if __name__ == "__main__":
    main()
