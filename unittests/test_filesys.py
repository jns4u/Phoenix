import imp_unittest, unittest
import wtc
import wx
import os
from cStringIO import StringIO


pngFile = os.path.join(os.path.dirname(__file__), 'toucan.png')

#---------------------------------------------------------------------------

class filesys_Tests(wtc.WidgetTestCase):

    def test_filesysClasses(self):
        # For now just test that the expected classes exist.  
        wx.FileSystem
        wx.FSFile
        wx.FileSystemHandler
        wx.MemoryFSHandler
        wx.ArchiveFSHandler
        wx.FilterFSHandler
        wx.InternetFSHandler
        wx.ZipFSHandler

    # TODO: Add more tests.
        
#---------------------------------------------------------------------------


if __name__ == '__main__':
    unittest.main()