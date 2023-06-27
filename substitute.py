import nazca as nd


mapping = {
    "part1.gds": {"part1": "part1"},
    # "part2.gds": {"part2": "part2"},
    # "part3.gds":{"part3":"part3"},
    # "part4.gds":{"part4":"part4"},
    # "part5.gds":{"part5":"part5"},
}

nd.replaceCells(
    gdsin="total.gds",
    gdsout="total_replace.gds",
    ScellMapping=mapping,
)
