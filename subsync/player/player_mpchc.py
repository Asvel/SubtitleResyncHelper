# -*- coding: utf-8 -*-

import subprocess
from uuid import uuid4 as uuid

from subsync import config, win
from subsync.retry import retry
from subsync.time import Time
from subsync.player.player_win import PlayerWin as Player


class CMD:
    CONNECT            = 0x50000000
    STATE              = 0x50000001
    PLAYMODE           = 0x50000002
    NOWPLAYING         = 0x50000003
    LISTSUBTITLETRACKS = 0x50000004
    LISTAUDIOTRACKS    = 0x50000005
    CURRENTPOSITION    = 0x50000007
    NOTIFYSEEK         = 0x50000008
    NOTIFYENDOFSTREAM  = 0x50000009
    VERSION            = 0x5000000A
    PLAYLIST           = 0x50000006
    DISCONNECT         = 0x5000000B
    OPENFILE           = 0xA0000000
    STOP               = 0xA0000001
    CLOSEFILE          = 0xA0000002
    PLAYPAUSE          = 0xA0000003
    PLAY               = 0xA0000004
    PAUSE              = 0xA0000005
    ADDTOPLAYLIST      = 0xA0001000
    CLEARPLAYLIST      = 0xA0001001
    STARTPLAYLIST      = 0xA0001002
    REMOVEFROMPLAYLIST = 0xA0001003
    SETPOSITION        = 0xA0002000
    SETAUDIODELAY      = 0xA0002001
    SETSUBTITLEDELAY   = 0xA0002002
    SETINDEXPLAYLIST   = 0xA0002003
    SETAUDIOTRACK      = 0xA0002004
    SETSUBTITLETRACK   = 0xA0002005
    GETSUBTITLETRACKS  = 0xA0003000
    GETCURRENTPOSITION = 0xA0003004
    JUMPOFNSECONDS     = 0xA0003005
    GETVERSION         = 0xA0003006
    GETAUDIOTRACKS     = 0xA0003001
    GETNOWPLAYING      = 0xA0003002
    GETPLAYLIST        = 0xA0003003
    TOGGLEFULLSCREEN   = 0xA0004000
    JUMPFORWARDMED     = 0xA0004001
    JUMPBACKWARDMED    = 0xA0004002
    INCREASEVOLUME     = 0xA0004003
    DECREASEVOLUME     = 0xA0004004
    SHADER_TOGGLE      = 0xA0004005
    CLOSEAPP           = 0xA0004006
    SETSPEED           = 0xA0004008
    OSDSHOWMESSAGE     = 0xA0005000


class PlayerMPCHC(Player):

    def _open(self):
        wnd = win.WNDCLASS()
        wnd.lpfnWndProc = {win.WM_COPYDATA:self._on_copy_data}
        wnd.lpszClassName = str(uuid())
        wnd.hInstance = win.GetModuleHandle(None)
        self._hwnd_listener = win.CreateWindow(win.RegisterClass(wnd),
            "srhListener",0, 0, 0, 0, 0, 0, 0, wnd.hInstance, None)

        self._player = subprocess.Popen(self._generate_args())

        self._hwnd = None
        self._pump_message_until(lambda: self._hwnd is not None)

        win.MaximumWindow(self._hwnd)

    def _generate_args(self):
        return [config.playerpath,
                "/open", "/new", self._filepath,
                "/slave", str(self._hwnd_listener)]

    def _send_message(self, command, message=""):
        win.CopyData_SendString(self._hwnd, command, message)

    def _on_copy_data(self, hwnd, msg, wparam, lparam):
        command, message = win.CopyData_ParseString(lparam)
        self._parse_message(command, message)

    def _parse_message(self, command, message):
        if command == CMD.CONNECT:
            self._hwnd = int(message)
        elif command == CMD.CURRENTPOSITION:
            self.__time = float(message)

    def _pump_message_until(self, condition):
        def pump_message():
            win.PumpWaitingMessages()
            return condition()
        retry(pump_message)

    def _close(self):
        self._send_message(CMD.CLOSEAPP)
        win.SendMessage(self._hwnd_listener, win.WM_CLOSE, 0, 0)

    def _gettime(self):
        self.__time = None
        self._send_message(CMD.GETCURRENTPOSITION)
        self._pump_message_until(lambda: self.__time is not None)
        time = Time(s=self.__time) if self.__time is not None else None
        return time

    def _settime(self, time):
        self._send_message(CMD.SETPOSITION, str(time.ms_time/1000))

