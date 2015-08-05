/*
 * Always remember to add the type to the variable when instantiating an object along with the new keyword
 * I didn't add the first character initially, which is an issue because the loop starts at 1
 * I assumed the numbers were additive instead of multiplicative
 * I was appending the lastChar instead of the current character when they weren't equal
 */
class StringCompressor {

    public static void main(String[] args) {
        StringCompressor compressor = new StringCompressor();
        String compressed = compressor.compress("aabcccccaaa");
        System.out.println(compressed);
    }

    public String compress(String original) {
        if (original.length() < 2) {
            return original;
        }

        char lastChar = original.charAt(0);
        int repeatCount = 0;
        StringBuilder compressedString = new StringBuilder();
        compressedString.append(lastChar);
        for (int i = 1; i < original.length(); i++) {
            char nextChar = original.charAt(i);
            if (nextChar == lastChar) {
                repeatCount++;
            } else {
                if (repeatCount > 0) {
                    compressedString.append(repeatCount + 1);
                }
                compressedString.append(nextChar);
                repeatCount = 0;
            }
            lastChar = nextChar;
        }
        return compressedString.toString();
    }
}
