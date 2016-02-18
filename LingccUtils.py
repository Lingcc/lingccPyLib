from __future__ import print_function
import os
import sys
import subprocess
import time

CUR_TIME_STR=time.strftime("%Y%m%d-%H%M%S")
CUR_SCRIPT_DIR=os.path.dirname(os.path.realpath(__file__))

def removeIfExists(filepath):
  try:
    os.remove(filepath)
  except OSError:
    pass

def runCmd(cmdlst, outfn=None, errfn=None, runasShell=False,
           logfile=None, cwd=None):
  assert type(cmdlst) == type([])
  if logfile != None:
    with open(logfilename, 'a') as outfile:
      outfile.write("RUN CMD:"+" ".join(cmdlst))
  print(" ".join(cmdlst))

  #if runasShell:


    #return

  ## Run use subprocess
  closeoutf = False
  closeerrf = False
  outf = None
  if outfn != None:
    outf = open(outfn, "a")
    closeoutf = True

  errf = None
  if errfn != None:
    errf = open(errfn, "a")
    closeerrf = True

  if outf != None and errf != None:
    p=subprocess.Popen(cmdlst, stdout=outf, stderr=errf, cwd=cwd)
  elif outf != None and errf == None:
    p=subprocess.Popen(cmdlst, stdout=outf, stderr=outf, cwd=cwd)
  else:
    p=subprocess.call(cmdlst, cwd=cwd)

  p.wait()
  if closeoutf:
    outf.close()
  if closeerrf:
    errf.close()
