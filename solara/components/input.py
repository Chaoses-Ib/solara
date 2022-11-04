from typing import Callable

import solara
from solara.alias import rv as v


@solara.component
def InputText(
    label: str,
    value: str = "",
    on_value: Callable[[str], None] = None,
    disabled: bool = False,
    password: bool = False,
):
    """Free form text input.

    ## Arguments

    * `label`: Label to display next to the slider.
    * `value`: The currently entered value.
    * `on_value`: Callback to call when the value changes.
    * `disabled`: Whether the input is disabled.
    * `password`: Whether the input is a password input (typically shows input text obscured with an asterisk).
    """

    def set_value_cast(value):
        if on_value is None:
            return
        on_value(str(value))

    return v.TextField(v_model=value, on_v_model=set_value_cast, label=label, disabled=disabled, type="password" if password else None)
