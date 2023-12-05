#!/usr/bin/env python3

import sys
import re


seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []


def map_source_to_dest(source, m):
    for r in m:
        if source in range(r.get("source"), r.get("source") + r.get("length")):
            return r.get("destination") + source - r.get("source")
    return source


def map_range(rang, mapp):
    res_range = []
    start = rang.get("start")
    length = rang.get("length")
    for r in mapp:
        map_start = r.get("source")
        map_length = r.get("length")
        map_end = map_start + map_length - 1
        if start in range(map_start, map_end):
            if start + length <= map_end:
                res_range.append(dict(start=r.get("destination") - map_start + start, length=length))
            else:
                res_range.append(dict(start=r.get("destination") - map_start + start, length=map_end - start + 1))
                new_range = dict(start=map_end + 1, length=length - (map_end - start + 1))
                for results in map_range(new_range, mapp):
                    res_range.append(results)
    if len(res_range) == 0:
        res_range.append(rang)
    for res in res_range:
        if res.get("length") == 0:
            res_range.remove(res)
    return res_range


if __name__ == '__main__':
    data = [line.strip('\n') for line in open(sys.argv[1])]
    res1, res2 = 0, 0

    seeds = [int(n) for n in re.findall(r"\d+", data[0])]
    soil_start = data.index("seed-to-soil map:")
    fert_start = data.index("soil-to-fertilizer map:")
    wate_start = data.index("fertilizer-to-water map:")
    ligh_start = data.index("water-to-light map:")
    temp_start = data.index("light-to-temperature map:")
    humi_start = data.index("temperature-to-humidity map:")
    loca_start = data.index("humidity-to-location map:")
    locations = []

    for i in range(soil_start + 1, fert_start - 1):
        nums = [int(n) for n in re.findall(r"\d+", data[i])]
        r = dict(destination=nums[0], source=nums[1], length=nums[2])
        seed_to_soil.append(r)
    for i in range(fert_start + 1, wate_start - 1):
        nums = [int(n) for n in re.findall(r"\d+", data[i])]
        r = dict(destination=nums[0], source=nums[1], length=nums[2])
        soil_to_fertilizer.append(r)
    for i in range(wate_start + 1, ligh_start - 1):
        nums = [int(n) for n in re.findall(r"\d+", data[i])]
        r = dict(destination=nums[0], source=nums[1], length=nums[2])
        fertilizer_to_water.append(r)
    for i in range(ligh_start + 1, temp_start - 1):
        nums = [int(n) for n in re.findall(r"\d+", data[i])]
        r = dict(destination=nums[0], source=nums[1], length=nums[2])
        water_to_light.append(r)
    for i in range(temp_start + 1, humi_start - 1):
        nums = [int(n) for n in re.findall(r"\d+", data[i])]
        r = dict(destination=nums[0], source=nums[1], length=nums[2])
        light_to_temperature.append(r)
    for i in range(humi_start + 1, loca_start - 1):
        nums = [int(n) for n in re.findall(r"\d+", data[i])]
        r = dict(destination=nums[0], source=nums[1], length=nums[2])
        temperature_to_humidity.append(r)
    for i in range(loca_start + 1, len(data)):
        nums = [int(n) for n in re.findall(r"\d+", data[i])]
        r = dict(destination=nums[0], source=nums[1], length=nums[2])
        humidity_to_location.append(r)

    for seed in seeds:
        soil = map_source_to_dest(seed, seed_to_soil)
        fertilizer = map_source_to_dest(soil, soil_to_fertilizer)
        water = map_source_to_dest(fertilizer, fertilizer_to_water)
        light = map_source_to_dest(water, water_to_light)
        temperature = map_source_to_dest(light, light_to_temperature)
        humidity = map_source_to_dest(temperature, temperature_to_humidity)
        location = map_source_to_dest(humidity, humidity_to_location)
        locations.append(location)

    res1 = min(locations)

    print("Result Challenge 1: " + str(res1))

    seed_ranges = []
    soil_ranges = []
    fert_ranges = []
    wate_ranges = []
    ligh_ranges = []
    temp_ranges = []
    humi_ranges = []
    loca_ranges = []
    for i in range(len(seeds)):
        if i % 2 == 1:
            continue
        r = dict(start=seeds[i], length=seeds[i+1])
        seed_ranges.append(r)

    print(seed_ranges)
    for r in seed_ranges:
        soil_ranges += map_range(r, seed_to_soil)
    print(soil_ranges)
    for r in soil_ranges:
        fert_ranges += map_range(r, soil_to_fertilizer)
    print(fert_ranges)
    for r in fert_ranges:
        wate_ranges += map_range(r, fertilizer_to_water)
    print(wate_ranges)
    for r in wate_ranges:
        ligh_ranges += map_range(r, water_to_light)
    print(ligh_ranges)
    for r in ligh_ranges:
        temp_ranges += map_range(r, light_to_temperature)
    print(temp_ranges)
    for r in temp_ranges:
        humi_ranges += map_range(r, temperature_to_humidity)
    print(humi_ranges)
    for r in humi_ranges:
        loca_ranges += map_range(r, humidity_to_location)
    print(loca_ranges)

    locs = []
    for loc in loca_ranges:
        locs.append(loc.get("start"))
        
    res2 = min(locs)

    print("Result Challenge 2: " + str(res2))
