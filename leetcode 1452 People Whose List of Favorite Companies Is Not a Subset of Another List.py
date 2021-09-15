class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:

        words_index = collections.defaultdict(set)

        for i, favorite in enumerate(favoriteCompanies):
            for word in favorite:
                words_index[word].add(i)

        ans = []

        for i, favorite in enumerate(favoriteCompanies):
            candidate = set(words_index[favorite[0]])
            for word in favorite[1:]:
                candidate &= words_index[word]

            if len(candidate) == 1:
                ans.append(i)

        return ans
