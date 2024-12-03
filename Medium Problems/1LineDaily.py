class Solution:#this program inserts spaces into the string s at every index in the list spaces.
  """We use pointers i and j both referring to spaces, but i having an extra 0 at the beginning and j having an extra None at the end 
  so that any spaces on the zero position will be added and so we don't forget to add the rest of the string. Using i and j we
  fill an array with the substrings between the indexes of spaces and join it with spaces (' ')."""
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        return ' '.join([s[i:j] for i,j in zip([0]+spaces,spaces+[None])])
