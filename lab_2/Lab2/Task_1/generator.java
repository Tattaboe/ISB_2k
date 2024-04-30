import java.util.Random;

/**
 * This class provides a method to generate a random sequence of bits.
 */
public class Generator {

    /**
     * Generates a random sequence of bits.
     *
     * @param random The Random object used for generating random numbers.
     * @param length The length of the random bit sequence to generate.
     * @return A string representing the random bit sequence.
     */
    private static String generateRandomBits(Random random, int length) {
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < length; i++) {
            int bit = random.nextInt(2);
            result.append(bit);
        }
        return result.toString();
    }

    /**
     * The main method to generate and print a random sequence of bits.
     *
     * @param args The command-line arguments (not used in this method).
     */
    public static void main(String[] args) {
        Random random = new Random();

        String randomBits = generateRandomBits(random, 128);

        System.out.println("Random sequence: " + randomBits);
    }
}