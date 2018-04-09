# instead of memory, we have
  # a tape that is infinite in both directions
  # and a head that reads the tape

# X_B machine
  # changes B -> X and vice versa
  # also need a state symbol s1..s4 to ensure one state per instruction

X_B = {
    ("B", "s1"): ("X", "R", "s2"),
    ("B", "s2"): ("B", "L", "s3"),
    ("X", "s3"): ("B", "R", "s4"),
    ("B", "s4"): ("B", "L", "s1")
}

def simulate(instructions):
  # set up initial state (ideally not hardcoded like below)
  tape = ["B", "B"]
  head = 0
  state = "s1"

  # loop:
  for _ in range(8):
    # print statements just show results in console, not necessary for machine
    print(state.rjust(2) + ": " + "".join(tape))
    print("    " + " " * head + "^")
  # look up instruction
    tape[head], head_dir, state = instructions[(tape[head], state)]
  # apply that instruction to the machine
    head += 1 if head_dir == "R" else - 1

simulate(X_B)
