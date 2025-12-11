from sympy import factorint


Ranges = [1-14,46452718-46482242,16-35,92506028-92574540,1515128146-1515174322,56453-79759,74-94,798-971,49-66,601-752,3428-4981,511505-565011,421819-510058,877942-901121,39978-50500,9494916094-9494978970,7432846301-7432888696,204-252,908772-990423,21425-25165,1030-1285,7685-9644,419-568,474396757-474518094,5252506279-5252546898,4399342-4505058,311262290-311393585,1895-2772,110695-150992,567521-773338,277531-375437,284-364,217936-270837,3365257-3426031,29828-36350]


# probably could have done a more elegant solution than adding quotes myself, but hey if it works
ranges = [
    "1-14","46452718-46482242","16-35","92506028-92574540",
    "1515128146-1515174322","56453-79759","74-94","798-971",
    "49-66","601-752","3428-4981","511505-565011","421819-510058",
    "877942-901121","39978-50500","9494916094-9494978970",
    "7432846301-7432888696","204-252","908772-990423","21425-25165",
    "1030-1285","7685-9644","419-568","474396757-474518094",
    "5252506279-5252546898","4399342-4505058","311262290-311393585",
    "1895-2772","110695-150992","567521-773338","277531-375437",
    "284-364","217936-270837","3365257-3426031","29828-36350"
]

testRanges = ["1-14", "16-35"] # smaller subset for testing

range_dict = {}

for r in ranges:
    start, end = map(int, r.split('-'))
    range_dict[r] = range(start, end+1)

sum = 0

for entry, values in range_dict.items():
    print(entry)
    for value in values:
        # print(value)
        stringVal = str(value)
        stringLen = len(stringVal)
        primeFactors = set(factorint(stringLen).keys())
        # print(primeFactors)
        for factor in primeFactors:
            # print(factor)
            if stringLen % factor != 0:
                break
            chunkSize = int(stringLen / factor)
            chunks = { stringVal[i:i+chunkSize] for i in range(0, stringLen, chunkSize) }

            if len(chunks) == 1:
                print(f"Value: {stringVal}, Factor: {factor}, Chunk size: {chunkSize}, Chunks: {chunks}")
                print(f"Unique chunks: {len(chunks)}")  
                sum+= value
                print(sum)
                break  # forgot this the first time, so I double counted!

print(sum)

# Part 1, keeping unchanged in a comment for posterity while I work on Part 2
# for entry, values in range_dict.items():
#     print(entry)
#     for value in values:
#         stringVal = str(value)
#         if len(stringVal)%2 == 0:
#             halfwayPoint = int(len(stringVal)/2)
#             if stringVal[0:halfwayPoint] == stringVal[halfwayPoint:len(stringVal)]:
#                 print(value)
#                 sum+=value



