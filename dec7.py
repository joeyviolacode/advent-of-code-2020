from dec7_input import bags_dicts as bags


def part1():
    answer = set()
    def search(color):
        print("******* " + color + " *******")
        for b in bags:
            if color in bags[b]:
                answer.add(b)
                print(b)
                search(b)
    search('shiny gold')
    return len(answer)

print(part1())

# def part2():
#     def search(bag):
#         count = 1
#         for s in bags[bag]:
#             multiplier = bags[bag][s]
#             count += multiplier * search(s)
#         return count
#     return search('shiny gold' ) - 1 






# def find_gold_outers(list_of_bags):
#     outside_bags = []
#     for item in list_of_bags:
#         if "shiny gold" in item["inners"].keys():
#             # add dict {item["outer"]: item["inners"]["shiny gold"] to add count of shiny gold}
#             outside_bags.append({item["outer"]: item["inners"]["shiny gold"]})
#     next_bags = []
#     for item in list_of_bags:   
#         for thing in outside_bags:
#             for color in thing.keys():
#                 if color in item["inners"].keys():
#                     next_bags.append({item["outer"]: item["inners"][color]})
#     next_next_bags = []
#     for item in list_of_bags:   
#         for thing in next_bags:
#             for color in thing.keys():
#                 if color in item["inners"].keys():
#                     next_next_bags.append({item["outer"]: item["inners"][color]})
#     fourth_bags = []
#     for item in list_of_bags:   
#         for thing in next_next_bags:
#             for color in thing.keys():
#                 if color in item["inners"].keys():
#                     fourth_bags.append({item["outer"]: item["inners"][color]})
#     fifth_bags = []
#     for item in list_of_bags:   
#         for thing in fourth_bags:
#             for color in thing.keys():
#                 if color in item["inners"].keys():
#                     fifth_bags.append({item["outer"]: item["inners"][color]})



    # return outside_bags, next_bags, next_next_bags, fourth_bags, fifth_bags
        # for thing in outside_bags:
    #     for item in list_of_bags:
    #         if thing[0] in item:
    #             thing.append([{item["outer"]: item["inners"][thing["outer"]]}])
    # return outside_bags
    # for item in list_of_bags[]:
    #     if outside_bags in item["inners"].keys():
    #         outside_bags.append

# print(bags)
# first, second, third, fourth, fifth = find_gold_outers(bags)
# print(first)
# print(second)
# print(third)
# print(fourth)
# print(fifth)


******* shiny gold *******
shiny orange
******* shiny orange *******
pale aqua
******* pale aqua *******
dim salmon
******* dim salmon *******
posh lavender
******* posh lavender *******
mirrored lavender
******* mirrored lavender *******
muted violet
******* muted violet *******
light lime
******* light lime *******
light gold
******* light gold *******
mirrored red
******* mirrored red *******
bright gold
******* bright gold *******
dull lime
******* dull lime *******
striped red
******* striped red *******
bright silver
******* bright silver *******
plaid white
******* plaid white *******
posh coral
******* posh coral *******
drab olive
******* drab olive *******
dotted salmon
******* dotted salmon *******
wavy beige
******* wavy beige *******
striped cyan
******* striped cyan *******
wavy lavender
******* wavy lavender *******
dotted purple
******* dotted purple *******
faded silver
******* faded silver *******
dotted black
******* dotted black *******
faded orange
******* faded orange *******
wavy gold
******* wavy gold *******
mirrored purple
******* mirrored purple *******
bright lavender
******* bright lavender *******
posh purple
******* posh purple *******
shiny purple
******* shiny purple *******
faded olive
******* faded olive *******
vibrant lavender
******* vibrant lavender *******
vibrant orange
******* vibrant orange *******
dotted olive
******* dotted olive *******
bright silver
******* bright silver *******
dull gray
******* dull gray *******
muted gray
******* muted gray *******
plaid gray
******* plaid gray *******
dull salmon
******* dull salmon *******
light olive
******* light olive *******
shiny salmon
******* shiny salmon *******
dull green
******* dull green *******
pale blue
******* pale blue *******
vibrant purple
******* vibrant purple *******
dark cyan
******* dark cyan *******
faded blue
******* faded blue *******
plaid magenta
******* plaid magenta *******
muted gray
******* muted gray *******
striped aqua
******* striped aqua *******
dotted lavender
******* dotted lavender *******
mirrored white
******* mirrored white *******
drab red
******* drab red *******
dotted aqua
******* dotted aqua *******
mirrored lime
******* mirrored lime *******
dim chartreuse
******* dim chartreuse *******
mirrored chartreuse
******* mirrored chartreuse *******
vibrant brown
******* vibrant brown *******
clear turquoise
******* clear turquoise *******
pale violet
******* pale violet *******
drab maroon
******* drab maroon *******
shiny cyan
******* shiny cyan *******
mirrored yellow
******* mirrored yellow *******
dull white
******* dull white *******
shiny magenta
******* shiny magenta *******
muted salmon
******* muted salmon *******
muted plum
******* muted plum *******
shiny gray
******* shiny gray *******
mirrored beige
******* mirrored beige *******
plaid tomato
******* plaid tomato *******
mirrored lime
******* mirrored lime *******
dim chartreuse
******* dim chartreuse *******
mirrored chartreuse
******* mirrored chartreuse *******
vibrant brown
******* vibrant brown *******
clear turquoise
******* clear turquoise *******
pale violet
******* pale violet *******
plaid silver
******* plaid silver *******
pale indigo
******* pale indigo *******
shiny beige
******* shiny beige *******
bright turquoise
******* bright turquoise *******
dull tomato
******* dull tomato *******
clear green
******* clear green *******
muted red
******* muted red *******
muted aqua
******* muted aqua *******
vibrant purple
******* vibrant purple *******
dark cyan
******* dark cyan *******
faded blue
******* faded blue *******
plaid magenta
******* plaid magenta *******
posh beige
******* posh beige *******
dotted violet
******* dotted violet *******
striped lime
******* striped lime *******
faded magenta
******* faded magenta *******
dotted gray
******* dotted gray *******
dark brown
******* dark brown *******
muted coral
******* muted coral *******
dim gray
******* dim gray *******
posh green
******* posh green *******
vibrant blue
******* vibrant blue *******
muted salmon
******* muted salmon *******
muted orange
******* muted orange *******
dotted lime
******* dotted lime *******
faded plum
******* faded plum *******
shiny cyan
******* shiny cyan *******
mirrored yellow
******* mirrored yellow *******
mirrored crimson
******* mirrored crimson *******
faded salmon
******* faded salmon *******
muted lavender
******* muted lavender *******
muted violet
******* muted violet *******
light lime
******* light lime *******
light gold
******* light gold *******
mirrored red
******* mirrored red *******
bright gold
******* bright gold *******
dull lime
******* dull lime *******
striped red
******* striped red *******
bright silver
******* bright silver *******
plaid white
******* plaid white *******
posh coral
******* posh coral *******
drab olive
******* drab olive *******
dotted salmon
******* dotted salmon *******
wavy beige
******* wavy beige *******
striped cyan
******* striped cyan *******
wavy lavender
******* wavy lavender *******
dotted purple
******* dotted purple *******
faded silver
******* faded silver *******
dull lime
******* dull lime *******
striped red
******* striped red *******
bright silver
******* bright silver *******
plaid white
******* plaid white *******
posh coral
******* posh coral *******
drab olive
******* drab olive *******
dotted salmon
******* dotted salmon *******
wavy beige
******* wavy beige *******
striped cyan
******* striped cyan *******
wavy lavender
******* wavy lavender *******
wavy violet
******* wavy violet *******
drab orange
******* drab orange *******
wavy gray
******* wavy gray *******
dark yellow
******* dark yellow *******
faded olive
******* faded olive *******
faded orange
******* faded orange *******
striped beige
******* striped beige *******
posh black
******* posh black *******
shiny lime
******* shiny lime *******
dim tomato
******* dim tomato *******
dim beige
******* dim beige *******
dark silver
******* dark silver *******
clear silver
******* clear silver *******
drab blue
******* drab blue *******
wavy silver
******* wavy silver *******
shiny aqua
******* shiny aqua *******
dark aqua
******* dark aqua *******
mirrored purple
******* mirrored purple *******
bright lavender
******* bright lavender *******
posh purple
******* posh purple *******
shiny purple
******* shiny purple *******
faded olive
******* faded olive *******
vibrant lavender
******* vibrant lavender *******
vibrant orange
******* vibrant orange *******
dotted olive
******* dotted olive *******
bright silver
******* bright silver *******
dull gray
******* dull gray *******
muted gray
******* muted gray *******