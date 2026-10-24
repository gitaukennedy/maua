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
             mock.patch.dict(os.environ, {'FFMPEG_PATH': 'C:/tools/ffmpeg.exe'}, clear=False):
            self.assertEqual(mod.resolve_ffmpeg_executable(), 'C:/tools/ffmpeg.exe')

    def test_raises_helpful_error_when_ffmpeg_missing(self):
        with mock.patch.object(mod.shutil, 'which', return_value=None), \
             mock.patch.dict(os.environ, {}, clear=True):
            with self.assertRaises(FileNotFoundError):
                mod.resolve_ffmpeg_executable()


if __name__ == '__main__':
    unittest.main()
