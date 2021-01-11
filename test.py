input = [[{'shiny orange': 5}, {'mirrored crimson': 2}, {'drab blue': 5}, {'dark aqua': 1}, {'mirrored purple': 3}],
[{'pale aqua': 2}, {'faded salmon': 5}, {'bright lavender': 1}, {'wavy silver': 2}, {'dull lime': 3}, {'wavy violet': 4}, {'plaid gray': 5}, {'faded orange': 5}, {'drab maroon': 3}, {'dim gray': 1}, {'striped beige': 3}, {'dotted lime': 1}, {'dim beige': 3}],
[{'posh purple': 4}, {'dull salmon': 1}, {'muted lavender': 4}, {'drab orange': 3}, {'muted violet': 3}, {'shiny cyan': 2}, {'dark yellow': 3}, {'light olive': 4}, {'vibrant lavender': 2}, {'striped red': 4}, {'drab olive': 5}, {'shiny aqua': 1}, {'faded plum': 5}, {'dark silver': 5}, {'posh black': 3}, {'dotted olive': 4}, {'dull gray': 5}, {'dim tomato': 3}, {'faded olive': 4}, {'muted gray': 5}, {'dull white': 4}, {'clear silver': 5}, {'dim salmon': 1}, {'posh green': 4}, {'faded orange': 2}, {'wavy gold': 5}, {'striped aqua': 5}, {'plaid silver': 2}, {'striped lime': 1}, {'dotted lavender': 5}],
[{'shiny salmon': 5}, {'mirrored yellow': 5}, {'dotted salmon': 3}, {'shiny cyan': 4}, {'vibrant orange': 3}, {'light lime': 5}, {'vibrant blue': 2}, {'pale blue': 4}, {'pale indigo': 5}, {'mirrored white': 4}, {'posh lavender': 5}, {'vibrant purple': 4}, {'dark cyan': 5}, {'mirrored lavender': 3}, {'faded magenta': 3}, {'dotted purple': 1}, {'muted gray': 4}, {'dark brown': 2}, {'wavy gray': 4}, {'muted salmon': 2}, {'shiny magenta': 1}, {'bright silver': 3}, {'bright silver': 3}, {'plaid white': 3}, {'shiny purple': 3}, {'mirrored purple': 4}, {'muted plum': 5}, {'posh beige': 5}, {'faded silver': 4}, {'muted orange': 3}, {'dotted aqua': 4}, {'shiny lime': 5}, {'mirrored lime': 5}, {'mirrored lime': 5}],
[{'light gold': 2}, {'dim chartreuse': 5}, {'dim chartreuse': 5}, {'mirrored yellow': 5}, {'muted coral': 3}, {'muted violet': 4}, {'shiny beige': 2}, {'posh coral': 5}, {'bright gold': 3}, {'dull green': 5}, {'dotted violet': 5}, {'faded blue': 3}, {'bright lavender': 1}, {'dull lime': 2}, {'dotted black': 3}, {'faded olive': 1}, {'wavy beige': 2}, {'shiny gray': 5}, {'vibrant brown': 5}, {'vibrant brown': 5}, {'muted salmon': 5}, {'bright turquoise': 5}, {'dull tomato': 5}, {'dotted gray': 4}, {'clear green': 2}, {'drab red': 3}, {'muted red': 3}]]

set_of_colors = set()
# print(input)
for group in input:
    for item in group:
        if item.keys() in set_of_colors:
            print("Overlap")
    #     set_of_colors.add(item)
print(list(set_of_colors))