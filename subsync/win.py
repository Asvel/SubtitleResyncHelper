# -*- coding: utf-8 -*-

from ctypes import *
from ctypes.wintypes import *

from win32api import *
from win32con import *
from win32event import *
from win32gui import *
from win32process import *
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt


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


def GetWindowTextX(hwnd):
    buffer = create_unicode_buffer(100)
    SendMessage(hwnd, WM_GETTEXT, len(buffer), buffer)
    return buffer.value


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


def FindWindows(class_=None, title=None, parent=None, process=None,
                top_level=True, visible_only=True, enabled_only=False):
    def try_(func):
        try:
            return func()
        except Exception:
            return False

    if top_level:
        windows = GetTopLevelWindows()
        if parent is not None:
            windows = [x for x in windows
                       if try_(lambda:GetParent(x) == parent)]
    else:
        if parent is None:
            parent = GetDesktopWindow()
        windows = GetChildWindows(parent)
    if class_ is not None:
        windows = [x for x in windows
                   if try_(lambda:class_ == GetClassName(x))]
    if title is not None:
        windows = [x for x in windows
                   if try_(title == GetWindowTextX(x))]
    if process is not None:
        windows = [x for x in windows
                   if try_(lambda:GetWindowThreadProcessId(x)[1] == process)]
    if visible_only:
        windows = [x for x in windows if try_(lambda:IsWindowVisible(x))]
    if enabled_only:
        windows = [x for x in windows if try_(lambda:IsWindowEnabled(x))]
    return windows


class COPYDATASTRUCT(Structure):
    _fields_ = [
        ('dwData', LPARAM),
        ('cbData', DWORD),
        ('lpData', c_void_p)
    ]
PCOPYDATASTRUCT = ctypes.POINTER(COPYDATASTRUCT)
def CopyData_SendString(hwnd, dwData, lpData=""):
    data = create_unicode_buffer(lpData)
    CDS = COPYDATASTRUCT(dwData, sizeof(data), cast(data, c_void_p))
    SendMessage(hwnd, WM_COPYDATA, 0, addressof(CDS))
def CopyData_ParseString(lParam):
    pCDS = cast(lParam, PCOPYDATASTRUCT)
    dwData = pCDS.contents.dwData
    lpData = wstring_at(pCDS.contents.lpData)
    return dwData, lpData
