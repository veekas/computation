def halts(f):
  pass

# def halter():
#   return

def looper():
  while True:
    pass

# halts(halter)
# halts(looper)

def impossible():
  return halts(impossible) and looper()

# contradiction:
# if it returns True (halts), that means that it evaluated the infinite loop (which it could not have done)
# it must halt in order to return False (did not halt)
