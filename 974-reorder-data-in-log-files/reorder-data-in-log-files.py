
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letterlogs = list()
        digilogs = list()
        for log in logs:
            split = log.split(" ", maxsplit=1)
            if re.match("[0-9]", split[1]):
                digilogs.append((split[0], split[1]))
            else:
                letterlogs.append((split[0], split[1]))

        letterlogs.sort(key=lambda x: (x[1], x[0]))

        return [
            " ".join(list(log)) for log in letterlogs + digilogs
        ]