# -*- coding: UTF-8 -*-
# reportOnce: report object position information only once per group of
# objects that share the same hierarchical position.

import addonHandler
import config
import globalPluginHandler
import speech.speech
import wx
from gui import guiHelper, settingsDialogs
from logHandler import log

try:
    from controlTypes import OutputReason
except ImportError:  # very old/new layouts
    from speech.types import OutputReason

addonHandler.initTranslation()

config.conf.spec["reportOnce"] = {
    "enabled": "boolean(default=False)",
}

_POSITION_OPTION = "reportObjectPositionInformation"

# Hierarchical key of the last object whose position info was handled.
_lastKey = None

_origGetObjectSpeech = None
_origMakeSettings = None


def _isActive():
    try:
        return (
            config.conf["reportOnce"]["enabled"]
            and config.conf["presentation"][_POSITION_OPTION]
        )
    except Exception:
        return False


def _getKey(obj):
    """Identify the object's place in the hierarchy: same parent, same role, same level."""
    try:
        info = obj.positionInfo or {}
    except Exception:
        info = {}
    return (obj.parent, obj.role, info.get("level"))


def _sameKey(a, b):
    if a is None or b is None:
        return False
    try:
        return a == b
    except Exception:
        return False


def _patchedGetObjectSpeech(obj, *args, **kwargs):
    global _lastKey
    if not _isActive():
        return _origGetObjectSpeech(obj, *args, **kwargs)

    reason = kwargs.get("reason", args[0] if args else OutputReason.QUERY)
    # An explicit query (NVDA+tab) must always report everything.
    if reason == OutputReason.QUERY:
        return _origGetObjectSpeech(obj, *args, **kwargs)

    try:
        key = _getKey(obj)
    except Exception:
        log.debugWarning("reportOnce: could not compute key", exc_info=True)
        return _origGetObjectSpeech(obj, *args, **kwargs)

    repeated = _sameKey(key, _lastKey)
    _lastKey = key
    if not repeated:
        return _origGetObjectSpeech(obj, *args, **kwargs)

    # Same group as the previous object: speak it without position info.
    presentation = config.conf["presentation"]
    presentation[_POSITION_OPTION] = False
    try:
        return _origGetObjectSpeech(obj, *args, **kwargs)
    finally:
        presentation[_POSITION_OPTION] = True


def _patchedMakeSettings(self, settingsSizer):
    _origMakeSettings(self, settingsSizer)

    anchor = getattr(self, "positionInfoCheckBox", None)
    if anchor is None:
        return

    idx = None
    for i in range(settingsSizer.GetItemCount()):
        if settingsSizer.GetItem(i).GetWindow() == anchor:
            idx = i
            break
    if idx is None:
        return

    # Translators: Label of a checkbox in the Object Presentation settings panel.
    checkBox = wx.CheckBox(self, label=_("Report position information only &once"))
    checkBox.SetValue(config.conf["reportOnce"]["enabled"])
    self._reportOnceCheckBox = checkBox

    settingsSizer.Insert(
        idx + 1,
        checkBox,
        flag=wx.TOP,
        border=getattr(guiHelper, "SPACE_BETWEEN_VERTICAL_DIALOG_ITEMS", 10),
    )
    # Make Tab go to the new checkbox right after the position info checkbox.
    checkBox.MoveAfterInTabOrder(anchor)

    def _updateVisibility(show):
        checkBox.Show(show)
        self.Layout()

    _updateVisibility(anchor.GetValue())

    def _onPositionInfoChecked(evt):
        _updateVisibility(evt.IsChecked())
        evt.Skip()

    anchor.Bind(wx.EVT_CHECKBOX, _onPositionInfoChecked)

    origSave = self.onSave

    def _newSave():
        origSave()
        config.conf["reportOnce"]["enabled"] = checkBox.GetValue()

    self.onSave = _newSave


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

    def __init__(self):
        super().__init__()
        global _origGetObjectSpeech, _origMakeSettings
        _origGetObjectSpeech = speech.speech.getObjectSpeech
        speech.speech.getObjectSpeech = _patchedGetObjectSpeech
        _origMakeSettings = settingsDialogs.ObjectPresentationPanel.makeSettings
        settingsDialogs.ObjectPresentationPanel.makeSettings = _patchedMakeSettings

    def terminate(self):
        global _origGetObjectSpeech, _origMakeSettings, _lastKey
        if _origGetObjectSpeech is not None:
            speech.speech.getObjectSpeech = _origGetObjectSpeech
            _origGetObjectSpeech = None
        if _origMakeSettings is not None:
            settingsDialogs.ObjectPresentationPanel.makeSettings = _origMakeSettings
            _origMakeSettings = None
        _lastKey = None
        super().terminate()