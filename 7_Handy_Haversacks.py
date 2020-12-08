from Handy_Haversacks_input import input

bags = dict()
for bag in input.split('\n'):
    bag_color, definition = bag.split(" bags contain ")
    sub_bags = []
    for sub_bag in definition.split(', '):
        number, sub_bag = sub_bag.split(' ', 1)
        if number == "no":
            break
        sub_bag = ' '.join(sub_bag.split(' ', 3)[:2])
        sub_bags.append((int(number), sub_bag))
    bags[bag_color] = sub_bags

visited = dict()

def contains_shiny_gold(bag_name):
    if bag_name not in visited:
        visited[bag_name] = False
        for number, sub_bag in bags[bag_name]:
            if sub_bag == "shiny gold":
                found = True
            else:
                found = contains_shiny_gold(sub_bag)
            if found:
                visited[bag_name] = found
                break
    return visited[bag_name]

counts = dict()
def count_bags(bag_name):
    if bag_name not in counts:
        counts[bag_name] = 0
        for number, sub_bag in bags[bag_name]:
            counts[bag_name] += number + number * count_bags(sub_bag)
    return counts[bag_name]

for bag in bags:
    contains_shiny_gold(bag)

print(sum(visited.values()), visited)
print(count_bags("shiny gold"))
