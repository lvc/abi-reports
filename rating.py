#!/usr/bin/env python3

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA  02110-1301 USA

import json
import os
import statistics

print("| BC rate (%) | Library |")
print("|-------------|---------|")

for d in sorted(os.listdir("report")):
    with open("report/%s" % (d)) as f:
        j = json.load(f)

    reports = j['Reports']
    change_perc = []
    release_count = 0
    imperfect_releases = 0
    for r in reports:
        if r['ChangedSoname'] == 0:
            release_count += 1
            perc_text = r['BC']
            perc = float(perc_text[:-1])
            if perc < 100.0:
                imperfect_releases += 1

            change_perc.append(perc)

    if len(change_perc) > 0:
        # Mean average stability per release where there wasn't an SO name change.
        mean = statistics.mean(change_perc)

        # Percentage of releases that were perfect
        perfect_percentage = 100.0-100.0*imperfect_releases/release_count

        # Our rating
        rating = mean * perfect_percentage / 100.0;

        print("| %5.1f       | %s |" % (rating, j['Title']))
