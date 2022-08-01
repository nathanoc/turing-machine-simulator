import time

class TuringMachine:
    def __init__(self, initialState, instructionTable, tape, initialPointerPosition):
        self.stateRegister = initialState
        self.instructionTable = instructionTable
        self.tape = tape
        self.pointerPosition = initialPointerPosition
        
    
    def run(self):
        halt = False

        startTime = time.time()
        steps = 0
        while halt == False:
            currentInstructions = self.instructionTable[self.stateRegister - 1][self.tape[self.pointerPosition]]

            writeInstruction = currentInstructions[0]
            movementInstruction = currentInstructions[1]
            stateInstruction = currentInstructions[2]

            self.tape[self.pointerPosition] = writeInstruction

            if movementInstruction == "L": # pointer left
                self.pointerPosition -= 1
            elif movementInstruction == "R": # pointer right
                self.pointerPosition += 1
            # else stay

            self.stateRegister = stateInstruction
            if stateInstruction == 0:
                halt = True

            steps += 1
        return [time.time() - startTime, steps]

def generateTape(leadingZeroes, centreConfig, trailingZeroes):
    return ([0] * leadingZeroes) + centreConfig + ([0] * trailingZeroes)
        

def main():
    # 5-state busy beaver contender
    instructionTable = [
        [   # State A
            [1, "R", 2],    # 0
            [1, "L", 3]     # 1
        ],
        [   # State B
            [1, "R", 3],    # 0
            [1, "R", 2],    # 1
        ],
        [   # State C
            [1, "R", 4],    # 0
            [0, "L", 5]     # 1
        ],
        [   # State D
            [1, "L", 1],    # 0
            [1, "L", 4]     # 1
        ],
        [   # State E
            [1, "R", 0],    # 0
            [0, "L", 1]     # 1
        ]
    ]

    tape = [0] * 25000

    turingMachine = TuringMachine(1, instructionTable, tape, 12500)
    runInfo = turingMachine.run()

    print(f"Time taken: {runInfo[0]} seconds")
    print(f"Total steps: {runInfo[1]}")
    print(f"Steps per second: {runInfo[1] / runInfo[0]}")

    # print(turingMachine.tape)
    print(turingMachine.tape.count(1))
    

if __name__ == "__main__":
    main()