
class Solution:
    def uniqueMorseRepresentations(self, words):
        unique = set()
        translation = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        for word in words:
            morse_translated = ""
            for char in word:
                translated = translation[ord(char)-97]
                morse_translated += translated
            unique.add(morse_translated)
        print(len(unique))

if __name__ == "__main__":
    words = ["gin", "zen", "gig", "msg"]

    s = Solution()
    s.uniqueMorseRepresentations(words)
