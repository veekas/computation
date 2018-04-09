# instead of memory, we have
  # a tape that is infinite in both directions
  # and a head that reads the tape

# X_B machine
  # changes B -> X and vice versa
  # also need a state symbol s1..s4 to ensure one state per instruction
  # example
    # B, s1 -> X and move head to the right     , s2
    # B, s2 -> B and move head back to the left , s3
    # X, s3 -> B and move head to the right     , s4
    # B, s4 -> B and move head back to the left , s1

X_B = {
    ("B", "s1"): ("X", "R", "s2"),
    ("B", "s2"): ("B", "L", "s3"),
    ("X", "s3"): ("B", "R", "s4"),
    ("B", "s4"): ("B", "L", "s1")
}

def simulate(instructions):
  # set up initial state (ideally not hardcoded like below)
  # tape
  tape = ["B", "B"]
  # head
  head = 0
  # state
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
