#!/usr/bin/python3

from __future__ import print_function
import os
import sys
import subprocess
import time
import unittest
import shutil
from LingccUtils import runCmd

class TestGlobalFunc(unittest.TestCase):
  outfn = "runcmd_out.txt"
  errfn = "runcmd_err.txt"
  cmdlst1=["echo", "hello"]
  cmdlst2=["rm",
    "AN_DO_NOT_EXISTING_FILE_NAME_FOR_TESTING_ONLY_4084284039"]
  def removefile(self):
      try:
        os.remove(self.outfn)
      except OSError:
        pass

      try:
        os.remove(self.errfn)
      except OSError:
        pass
  def setUp(self):
    self.removefile()
  def tearDown(self):
    self.removefile()
  def testrunCmd1(self):
     runCmd(self.cmdlst1, self.outfn, self.errfn)
     outf = open(self.outfn, 'r')
     errf = open(self.errfn, 'r')
     outf_content = outf.readline()
     errf_content = errf.readline()
     outf.close()
     errf.close()
     self.assertEqual(outf_content, "hello\n")
     self.assertEqual(errf_content, "")
  def testrunCmd2(self):
     runCmd(self.cmdlst2, self.outfn, self.errfn)
     outf = open(self.outfn, 'r')
     errf = open(self.errfn, 'r')
     outf_content = outf.readline()
     errf_content = errf.readline()
     outf.close()
     errf.close()
     self.assertEqual(outf_content, "")
     self.assertTrue(errf_content.find("No such file or directory"))


if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestGlobalFunc)
  unittest.TextTestRunner(verbosity=2).run(suite)

