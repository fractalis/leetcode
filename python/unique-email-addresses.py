class Solution:
    def numUniqueEmails(self, emails: 'List[str]') -> 'int':
        uniq_emails = set()

        for email in emails:
            esplit = email.split("@")
            first = esplit[0]
            if first.find("+"):
                first = first[:first.find("+")]
            first = first.replace(".","")
            uniq_emails.add(first+"@"+esplit[1])
        return len(uniq_emails)

if __name__ == "__main__":
    input = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]

    s = Solution()

    print(s.numUniqueEmails(input))
