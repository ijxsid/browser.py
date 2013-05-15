# Subsets in a Set 
Set = ["Italy","USA","England","Argentina","Costa Rica", "India", "Bulgaria"]
def subsets_of_set(elements_list, selected_so_far):
    if elements_list == []:
        print selected_so_far
    else:
        current_element = elements_list[0]
        rest_of_list = elements_list[1:]
        subsets_of_set(rest_of_list, selected_so_far + [current_element])
        subsets_of_set(rest_of_list, selected_so_far)

     
subsets_of_set(Set, [])
# for 5 elements:
# 5* 1-element lists:-> [1],[2],[3],[4],[5]
# 10 *2-2element lists :-> [1,2],[2,3]
# 10