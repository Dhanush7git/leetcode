class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        for ch in s:
            if ch == '*' and len(st) != 0:
                st.pop()
            else:
                st.append(ch)
        return "".join(st)
        