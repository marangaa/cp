class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common_strings = set(list1) & set(list2)  
        index_sums = {s: list1.index(s) + list2.index(s) for s in common_strings}  # Calculate index sums
        min_index_sum = min(index_sums.values()) 
        result = [s for s, index_sum in index_sums.items() if index_sum == min_index_sum]  # Get common strings with minimum index sum
        return result

        
        