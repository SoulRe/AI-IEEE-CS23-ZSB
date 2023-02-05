def main():
    dict1 = { "A":[20,30,100,49],
              "B":[00,199,201,29],
              "C":[40,90,69,18] }
    keys = []
    for i in dict1.keys():
        keys.append(i)
    # print(keys)
    ranges = []
    
    x = 0
    for i in dict1.values():
        i.sort()
        key_range = i[len(i) - 1] - i[0]
        ranges.append([key_range, keys[x]])
        # print(ranges)
        x += 1
    ranges.sort(reverse = True)
    print("Output: ")
    print(ranges[0][1])
        
main()