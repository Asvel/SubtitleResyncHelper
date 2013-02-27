# -*- coding: utf-8 -*-

from ctypes import *
from ctypes.wintypes import *

from win32api import *
from win32con import *
from win32event import *
from win32gui import *
from win32process import *
from PyQt4.QtGui import QKeySequence
from PyQt4.QtCore import Qt

def GetProcessHandleByProcessId(pid):
    return OpenProcess(PROCESS_QUERY_INFORMATION, False, pid)


def MaximumWindow(hwnd):
    #ShowWindow(hwnd, SW_MAXIMIZE)
    SendMessage(hwnd, WM_SYSCOMMAND, SC_MAXIMIZE, 0)


_GetGUIThreadInfo = windll.user32.GetGUIThreadInfo
class _GUITHREADINFO(Structure):
    _pack_ = 2
    _fields_ = [
        ('cbSize', DWORD),
        ('flags', DWORD),
        ('hwndActive', HWND),
        ('hwndFocus', HWND),
        ('hwndCapture', HWND),
        ('hwndMenuOwner', HWND),
        ('hwndMoveSize', HWND),
        ('hwndCaret', HWND),
        ('rcCaret', RECT),
    ]
def GetGUIThreadInfo(idThread):
    gui_info = _GUITHREADINFO(cbSize=sizeof(_GUITHREADINFO))
    if _GetGUIThreadInfo(idThread, byref(gui_info)):
        return gui_info
    else:
        return None


def GetWindowTextByHwnd(hwnd):
    buffer = create_unicode_buffer(100)
    SendMessage(hwnd, WM_GETTEXT, len(buffer), buffer)
    return buffer.value


_qtkeycodemap = {
    int(Qt.Key_Escape): VK_ESCAPE,
    int(Qt.Key_Tab): VK_TAB,
    int(Qt.Key_Backtab): VK_TAB,
    int(Qt.Key_Backspace): VK_BACK,
    int(Qt.Key_Return): VK_RETURN,
    int(Qt.Key_Enter): VK_RETURN,
    int(Qt.Key_Insert): VK_INSERT,
    int(Qt.Key_Delete): VK_DELETE,
    int(Qt.Key_Pause): VK_PAUSE,
    int(Qt.Key_Print): VK_PRINT,
    int(Qt.Key_Clear): VK_CLEAR,
    int(Qt.Key_Home): VK_HOME,
    int(Qt.Key_End): VK_END,
    int(Qt.Key_Left): VK_LEFT,
    int(Qt.Key_Up): VK_UP,
    int(Qt.Key_Right): VK_RIGHT,
    int(Qt.Key_Down): VK_DOWN,
    int(Qt.Key_PageUp): VK_PRIOR,
    int(Qt.Key_PageDown): VK_NEXT,
    int(Qt.Key_F1): VK_F1,
    int(Qt.Key_F2): VK_F2,
    int(Qt.Key_F3): VK_F3,
    int(Qt.Key_F4): VK_F4,
    int(Qt.Key_F5): VK_F5,
    int(Qt.Key_F6): VK_F6,
    int(Qt.Key_F7): VK_F7,
    int(Qt.Key_F8): VK_F8,
    int(Qt.Key_F9): VK_F9,
    int(Qt.Key_F10): VK_F10,
    int(Qt.Key_F11): VK_F11,
    int(Qt.Key_F12): VK_F12,
    int(Qt.Key_F13): VK_F13,
    int(Qt.Key_F14): VK_F14,
    int(Qt.Key_F15): VK_F15,
    int(Qt.Key_F16): VK_F16,
    int(Qt.Key_F17): VK_F17,
    int(Qt.Key_F18): VK_F18,
    int(Qt.Key_F19): VK_F19,
    int(Qt.Key_F20): VK_F20,
    int(Qt.Key_F21): VK_F21,
    int(Qt.Key_F22): VK_F22,
    int(Qt.Key_F23): VK_F23,
    int(Qt.Key_F24): VK_F24,
    int(Qt.Key_Space): VK_SPACE,
    int(Qt.Key_Asterisk): VK_MULTIPLY,
    int(Qt.Key_Plus): VK_ADD,
    int(Qt.Key_Comma): VK_SEPARATOR,
    int(Qt.Key_Minus): VK_SUBTRACT,
    int(Qt.Key_Slash): VK_DIVIDE,
    int(Qt.Key_MediaNext): VK_MEDIA_NEXT_TRACK,
    int(Qt.Key_MediaPrevious): VK_MEDIA_PREV_TRACK,
    int(Qt.Key_MediaPlay): VK_MEDIA_PLAY_PAUSE,
    int(Qt.Key_MediaStop): 0xB2, # VK_MEDIA_STOP,
    int(Qt.Key_VolumeDown): VK_VOLUME_DOWN,
    int(Qt.Key_VolumeUp): VK_VOLUME_UP,
    int(Qt.Key_VolumeMute): VK_VOLUME_MUTE,
    int(Qt.Key_0): int(Qt.Key_0),
    int(Qt.Key_1): int(Qt.Key_1),
    int(Qt.Key_2): int(Qt.Key_2),
    int(Qt.Key_3): int(Qt.Key_3),
    int(Qt.Key_4): int(Qt.Key_4),
    int(Qt.Key_5): int(Qt.Key_5),
    int(Qt.Key_6): int(Qt.Key_6),
    int(Qt.Key_7): int(Qt.Key_7),
    int(Qt.Key_8): int(Qt.Key_8),
    int(Qt.Key_9): int(Qt.Key_9),
    int(Qt.Key_A): int(Qt.Key_A),
    int(Qt.Key_B): int(Qt.Key_B),
    int(Qt.Key_C): int(Qt.Key_C),
    int(Qt.Key_D): int(Qt.Key_D),
    int(Qt.Key_E): int(Qt.Key_E),
    int(Qt.Key_F): int(Qt.Key_F),
    int(Qt.Key_G): int(Qt.Key_G),
    int(Qt.Key_H): int(Qt.Key_H),
    int(Qt.Key_I): int(Qt.Key_I),
    int(Qt.Key_J): int(Qt.Key_J),
    int(Qt.Key_K): int(Qt.Key_K),
    int(Qt.Key_L): int(Qt.Key_L),
    int(Qt.Key_M): int(Qt.Key_M),
    int(Qt.Key_N): int(Qt.Key_N),
    int(Qt.Key_O): int(Qt.Key_O),
    int(Qt.Key_P): int(Qt.Key_P),
    int(Qt.Key_Q): int(Qt.Key_Q),
    int(Qt.Key_R): int(Qt.Key_R),
    int(Qt.Key_S): int(Qt.Key_S),
    int(Qt.Key_T): int(Qt.Key_T),
    int(Qt.Key_U): int(Qt.Key_U),
    int(Qt.Key_V): int(Qt.Key_V),
    int(Qt.Key_W): int(Qt.Key_W),
    int(Qt.Key_X): int(Qt.Key_X),
    int(Qt.Key_Y): int(Qt.Key_Y),
    int(Qt.Key_Z): int(Qt.Key_Z),
}
def SendKey(hwnd, key):
    key = QKeySequence(key)[0]
    ctrl = bool(key & 0x04000000)
    alt = bool(key & 0x08000000)
    shift = bool(key & 0x02000000)
    win = bool(key & 0x10000000)
    key &= 0x1FFFFFF
    if ctrl: keybd_event(VK_CONTROL, 0, 0, 0)
    if alt: keybd_event(VK_MENU, 0, 0, 0)
    if shift: keybd_event(VK_SHIFT, 0, 0, 0)
    if win: keybd_event(VK_LWIN, 0, 0, 0)
    PostMessage(hwnd, WM_KEYDOWN, _qtkeycodemap[key], 0)
    if ctrl: keybd_event(VK_CONTROL, 0, KEYEVENTF_KEYUP, 0)
    if alt: keybd_event(VK_MENU, 0, KEYEVENTF_KEYUP, 0)
    if shift: keybd_event(VK_SHIFT, 0, KEYEVENTF_KEYUP, 0)
    if win: keybd_event(VK_LWIN, 0, KEYEVENTF_KEYUP, 0)


def GetTopLevelWindows():
    windows = []
    def EnumWindowProc(hwnd, lparam):
        windows.append(hwnd)
        return True
    EnumWindows(EnumWindowProc, None)
    return windows


def GetChildWindows(hwnd):
    windows = []
    def EnumChildProc(hwnd, lparam):
        windows.append(hwnd)
        return True
    EnumChildWindows(hwnd, EnumChildProc, None)
    return windows


def FindWindows(class_ = None, title = None, parent = None, process = None,
                top_level = True, visible_only = True, enabled_only = False):
    if top_level:
        windows = GetTopLevelWindows()
        if parent is not None:
            windows = [x for x in windows if GetParent(x) == parent]
    else:
        if parent is None:
            parent = GetDesktopWindow()
        windows = GetChildWindows(parent)
    if class_ is not None:
        windows = [x for x in windows if class_ == GetClassName(x)]
    if title is not None:
        windows = [x for x in windows if title == GetWindowTextByHwnd(x)]
    if process is not None:
        windows = [x for x in windows
                   if GetWindowThreadProcessId(x)[1] == process]
    if visible_only:
        windows = [x for x in windows if IsWindowVisible(x)]
    if enabled_only:
        windows = [x for x in windows if IsWindowEnabled(x)]
    return windows
