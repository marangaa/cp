class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""  # No common prefix if the array is empty
    
        common_prefix = []  # Initialize an empty array for common prefix characters

        for i, char in enumerate(strs[0]):
            for string in strs[1:]:
                # Check if we've reached the end of the string or if the characters don't match
                if i >= len(string) or char != string[i]:
                    return ''.join(common_prefix)  # Return the common prefix as a string
            
            common_prefix.append(char)  # If all characters match, add to the common prefix array
        
        return ''.join(common_prefix)  # Return the common prefix as a string
        