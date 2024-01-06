#!/usr/bin/env python3
# SPDX-License-Identifier: LGPL-2.1-or-later

#
# This file is part of libgpiod.
#
# Copyright (C) 2017-2018 Bartosz Golaszewski <bartekgola@gmail.com>
#

'''Simplified reimplementation of the gpioinfo tool in Python.'''

import gpiod

if __name__ == '__main__':
    for chip in gpiod.ChipIter():
        print('{} - {} lines:'.format(chip.name(), chip.num_lines()))

        for line in gpiod.LineIter(chip):
            offset = line.offset()
            name = line.name()
            consumer = line.consumer()
            direction = line.direction()
            active_state = line.active_state()

            print('\tline {:>3}: {:>18} {:>12} {:>8} {:>10}'.format(
                    offset,
                    'unnamed' if name is None else name,
                    'unused' if consumer is None else consumer,
                    'input' if direction == gpiod.Line.DIRECTION_INPUT else 'output',
                    'active-low' if active_state == gpiod.Line.ACTIVE_LOW else 'active-high'))

        chip.close()
