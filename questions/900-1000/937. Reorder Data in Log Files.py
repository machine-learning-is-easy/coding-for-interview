

class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        def process_str(str):
            return ' '.join(str.split()[1:] + [str.split()[0]])
        letter_logs = []
        digit_logs = []
        _ = [digit_logs.append(item) if item.split()[1].isdigit() else
             letter_logs.append(item) for item in logs]
        letter_logs.sort(key=lambda x: process_str(x))
        return letter_logs + digit_logs
