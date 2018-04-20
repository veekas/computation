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
  tape = ["B"] * 24
  head = 0
  state = "s1"

  # loop:
  for _ in range(24):
    # print statements just show results in console, not necessary for machine
    print(state.rjust(2) + ": " + "".join(tape))
    print("    " + " " * head + "^")
  # look up instruction
    tape[head], head_dir, state = instructions[(tape[head], state)]
  # apply that instruction to the machine
    head += 1 if head_dir == "R" else - 1

simulate(X_B)

# next step: show that we can do the following
# repetition, consitionals, compound nested data (DS in DS)

# use unary numbers (1 = 1, 2 = 11, 3 = 111, ...)
ADDER = {
  # (11+111)BBBBBBBBBBB
  #         ^

  ("B", "s1"): ("(", "R", "s2"),
  ("B", "s2"): ("1", "R", "s3"),
  ("B", "s3"): ("1", "R", "s4"),
  ("B", "s4"): ("+", "R", "s5"),
  ("B", "s5"): ("1", "R", "s6"),
  ("B", "s6"): ("1", "R", "s7"),

  # ("B", "s7"): ("1", "R", "s8"),
  ("B", "s7"): ("1", "R", "s7b"),
  ("B", "s7b"): ("1", "R", "s8"),

  ("B", "s8"): (")", "R", "s9"),

  ("B", "s9"): ("B", "L", "s9"),
  (")", "s9"): (")", "L", "s9"),
  ("1", "s9"): ("1", "L", "s9"),

  ("+", "s9"): ("1", "R", "s10"),
  ("1", "s10"): ("1", "R", "s10"),
  (")", "s10"): ("B", "L", "s11"),
  ("1", "s11"): (")", "R", "s12"),
  ("B", "s12"): ("B", "R", "s12"),
}

simulate(ADDER)
