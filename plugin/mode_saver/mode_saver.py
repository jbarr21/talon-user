import logging, os
from talon import Module, app, registry, scope

mode_filename = "talon.mode"
current_mode = ""
mod = Module()

setting_enable = mod.setting(
    "mode_saver_enable",
    bool,
    desc="If true the mode saver is enabled",
    default=True,
)

setting_paths = {
    s.path
    for s in [
        setting_enable,
    ]
}


def save_mode(mode):
    if setting_enable.get():
        mode_path = os.path.join(os.path.expanduser('~'), '.talon', mode_filename)
        with open(mode_path, 'w') as f:
            f.write(mode)


def on_update_contexts():
    global current_mode
    modes = scope.get("mode")

    if "sleep" in modes:
        mode = "sleep"
    elif "dictation" in modes:
        if "command" in modes:
            mode = "mixed"
        else:
            mode = "dictation"
    elif "command" in modes:
        mode = "command"
    else:
        mode = "other"

    if current_mode != mode:
        current_mode = mode
        save_mode(mode)


def on_ready():
    logging.debug("JRB on_ready")
    registry.register("update_contexts", on_update_contexts)


app.register("ready", on_ready)
