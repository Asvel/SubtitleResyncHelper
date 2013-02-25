# -*- coding: utf-8 -*-

from ctypes import *
from ctypes.wintypes import *

from win32api import *
from win32con import *
from win32event import *
from win32gui import *
from win32process import *

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
