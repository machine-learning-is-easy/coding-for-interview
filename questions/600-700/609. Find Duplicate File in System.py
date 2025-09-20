

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_map = defaultdict(list)

        for entry in paths:
            parts = entry.split(" ")
            root = parts[0]
            for file in parts[1:]:
                name, content = file.split("(")
                content = content[:-1]  # remove the closing ')'
                full_path = f"{root}/{name}"
                content_map[content].append(full_path)

        # Only keep groups with duplicates (length > 1)
        return [group for group in content_map.values() if len(group) > 1]