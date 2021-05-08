#
# Touch sensor driver
#
# Copyright (c) 2013,2014 Fingerprint Cards AB <tech@fingerprints.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License Version 2
# as published by the Free Software Foundation.
#

touch.deviceType = touchScreen

keyboard.layout = fingerprint
keyboard.builtIn = 1
keyboard.orientationAware = 1


# Touch Size
touch.touchSize.calibration = pressure

# Tool Size
# Driver reports tool size as an area measurement.
#
# Based on empirical measurements, we estimate the size of the tool
# using size = sqrt(22 * rawToolArea + 0) * 6 + 0.
touch.toolSize.calibration = area
touch.toolSize.areaScale = 22
touch.toolSize.areaBias = 0
touch.toolSize.linearScale = 6
touch.toolSize.linearBias = 0
touch.toolSize.isSummed = 0

# Pressure
# Driver reports signal strength as pressure.
#
# A normal index finger touch typically registers about 80 signal strength
# units although we don't expect these values to be accurate.
touch.pressure.calibration = amplitude
touch.pressure.source = default
touch.pressure.scale = 0.0125

# Size
touch.size.calibration = normalized

# Orientation
touch.orientation.calibration = vector

