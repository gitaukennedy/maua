import os
import unittest
from unittest import mock
import importlib.util

MODULE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'generate_lily_animation.py')
spec = importlib.util.spec_from_file_location('generate_lily_animation', MODULE_PATH)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class TestFFmpegLookup(unittest.TestCase):
    def test_uses_explicit_ffmpeg_path(self):
        with mock.patch.object(mod.shutil, 'which', return_value=None), \
             mock.patch.object(mod.os.path, 'isfile', return_value=True), \
             mock.patch.dict(os.environ, {'FFMPEG_PATH': 'C:/tools/ffmpeg.exe'}, clear=False):
            self.assertEqual(mod.resolve_ffmpeg_executable(), 'C:/tools/ffmpeg.exe')

    def test_finds_winget_install(self):
        ffmpeg_path = 'C:/Users/test/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg/ffmpeg-9.0.2-full_build/bin/ffmpeg.exe'
        with mock.patch.object(mod.shutil, 'which', return_value=None), \
             mock.patch.object(mod.os.path, 'isfile', return_value=False), \
             mock.patch.object(mod.glob, 'glob', return_value=[ffmpeg_path]), \
             mock.patch.dict(os.environ, {'LOCALAPPDATA': 'C:/Users/test/AppData/Local'}, clear=True):
            self.assertEqual(mod.resolve_ffmpeg_executable(), ffmpeg_path)

    def test_raises_helpful_error_when_ffmpeg_missing(self):
        with mock.patch.object(mod.shutil, 'which', return_value=None), \
             mock.patch.object(mod.os.path, 'isfile', return_value=False), \
             mock.patch.object(mod.glob, 'glob', return_value=[]), \
             mock.patch.dict(os.environ, {}, clear=True):
            with self.assertRaises(FileNotFoundError):
                mod.resolve_ffmpeg_executable()


if __name__ == '__main__':
    unittest.main()
