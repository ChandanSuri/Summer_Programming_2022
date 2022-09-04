class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """

        uniqueEmails = set()
        for email in emails:
            trimmedEmail = list()
            isAfterPlusSign = False
            for idx, ch in enumerate(email):
                if ch == "@":
                    trimmedEmail.append(email[idx:])
                    break
                elif ch == "." or isAfterPlusSign:
                    continue
                elif ch == "+":
                    isAfterPlusSign = True
                    continue

                trimmedEmail.append(ch)
            uniqueEmails.add("".join(trimmedEmail))

        return len(uniqueEmails)
