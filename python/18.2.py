#!/usr/bin/python
# -*- coding: utf-8 -*-

# PROBLEM
#
# As you congratulate yourself for a job well done, you notice that the
# documentation has been on the back of the tablet this entire time. While you
# actually got most of the instructions correct, there are a few key
# differences. This assembly code isn't about sound at all - it's meant to be
# run twice at the same time.
#
# Each running copy of the program has its own set of registers and follows the
# code independently - in fact, the programs don't even necessarily run at the
# same speed. To coordinate, they use the send (snd) and receive (rcv)
# instructions:
#
#   - snd X sends the value of X to the other program. These values wait in a
#     queue until that program is ready to receive them. Each program has its
#     own message queue, so a program can never receive a message it sent.
#   - rcv X receives the next value and stores it in register X. If no values
#     are in the queue, the program waits for a value to be sent to it.
#     Programs do not continue to the next instruction until they have received
#     a value. Values are received in the order they are sent.
#
# Each program also has its own program ID (one 0 and the other 1); the
# register p should begin with this value.
#
# For example:
#
# snd 1
# snd 2
# snd p
# rcv a
# rcv b
# rcv c
# rcv d
#
# Both programs begin by sending three values to the other. Program 0 sends 1,
# 2, 0; program 1 sends 1, 2, 1. Then, each program receives a value (both 1)
# and stores it in a, receives another value (both 2) and stores it in b, and
# then each receives the program ID of the other program (program 0 receives 1;
# program 1 receives 0) and stores it in c. Each program now sees a different
# value in its own copy of register c.
#
# Finally, both programs try to rcv a fourth time, but no data is waiting for
# either of them, and they reach a deadlock. When this happens, both programs
# terminate.
#
# It should be noted that it would be equally valid for the programs to run at
# different speeds; for example, program 0 might have sent all three values and
# then stopped at the first rcv before program 1 executed even its first
# instruction.
#
# Once both of your programs have terminated (regardless of what caused them to
# do so), how many times did program 1 send a value?

import collections


TASK_RUNNABLE = 0
TASK_BLOCKING = 1


class RecvError(RuntimeError):
    pass


class SchedulingError(RuntimeError):
    pass


# Helper function that retuns a register value or and immediate
def read(registers, operand):
    try:
        return int(operand)
    except ValueError:
        return registers[operand]


# All tasks have a thread context representing their state which is
# peristent across context switches
class Context(object):
    def __init__(self, pid):
        self.pid = pid
        self.state = TASK_RUNNABLE
        self.pc = 0
        self.regs = collections.defaultdict(int)
        self.regs['p'] = pid
        self.sends = 0


# Our operating system manages scheduling and RPC
class OperatingSystem(object):
    def __init__(self):
        self.tasks = []
        self.queues = []
        self.pid = None

    # Execute a new thread
    def execve(self, context):
        self.tasks.append(context)
        self.queues.append([])

    # Schedule a new task to run raising SchedulingError if none is found
    def schedule(self):
        # Find a task to run
        for pid in range(0, len(self.tasks)):
            if self.tasks[pid].state == TASK_RUNNABLE:
                self.pid = pid
                break
        else:
            raise SchedulingError

    # Send a message to a specific PID's queue
    def send(self, pid, value):
        self.queues[pid].append(value)
        self.tasks[pid].state = TASK_RUNNABLE
        self.tasks[self.pid].sends += 1

    # Recieve a message from my queue
    def recv(self):
        try:
            return self.queues[self.pid].pop(0)
        except IndexError:
            self.tasks[self.pid].state = TASK_BLOCKING
            raise RecvError

    # Run the OS main loop
    def run(self, memory):
        while True:
            self.schedule()
            Interpreter.run(self, memory)


# Interpreter runs the currently scheduled task
class Interpreter(object):
    @staticmethod
    def run(os, memory):
        context = os.tasks[os.pid]
        try:
            while True:
                fields = memory[context.pc].split()
                opcode = fields[0]
                if opcode == 'set':
                    context.regs[fields[1]] = read(context.regs, fields[2])
                elif opcode == 'mul':
                    context.regs[fields[1]] = context.regs[fields[1]] * read(context.regs, fields[2])
                elif opcode == 'add':
                    context.regs[fields[1]] = context.regs[fields[1]] + read(context.regs, fields[2])
                elif opcode == 'mod':
                    context.regs[fields[1]] = context.regs[fields[1]] % read(context.regs, fields[2])
                elif opcode == 'jgz':
                    if read(context.regs, fields[1]) > 0:
                        context.pc += read(context.regs, fields[2])
                        continue
                elif opcode == 'snd':
                    os.send(os.pid ^ 1, read(context.regs, fields[1]))
                elif opcode == 'rcv':
                    context.regs[fields[1]] = os.recv()
                else:
                    raise RuntimeError
                context.pc += 1
        except RecvError:
            pass


def main():
    memory = [x.strip() for x in open('18.in').readlines()]

    # Treat this like a cooperative multitasking operating system...
    os = OperatingSystem()
    os.execve(Context(0))
    os.execve(Context(1))

    try:
        os.run(memory)
    except SchedulingError:
        pass

    print os.tasks[1].sends

if __name__ == '__main__':
    main()

# vi: ts=4 et:
