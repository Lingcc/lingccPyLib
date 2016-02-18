from __future__ import print_function
import os
import sys
import subprocess
import time

CUR_TIME_STR=time.strftime("%Y%m%d-%H%M%S")
CUR_SCRIPT_DIR=os.path.dirname(os.path.realpath(__file__))



def removeIfExists(filepath):
  """Remove file only if it exists.
  
    This is done by catching the OSError exception.

    Args:
        filepath: The path of the file to be removed.
       
    Returns:
        no return value:

    Raises:
        No exception raises.
    """
  try:
    os.remove(filepath)
  except OSError:
    pass

def runCmd(cmdlst, outfn=None, errfn=None, runasShell=False,
           logfile=None, cwd=None):
  """Run unix command by create a new process.
  
  This is done by subprocess.Popen.
  
  Args:
      cmdlst: all the args and names of the cmd.
      outfn: filename for stdout of the process
      errfn: filename for stderr of the process
      runasShell: currently unused
      logfile: log file for runCmd to put the logs when trying to run the cmdlst
      cwd: specify the directory for the cmd to run
     
  Returns:
      no return value:
  
  Raises:
      No exception raises.
  """
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