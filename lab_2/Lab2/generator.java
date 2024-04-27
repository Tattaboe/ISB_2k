import java.util.Random;

public class Generator {

    private static String generateRandomBits(Random random, int length) {
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < length; i++) {
            int bit = random.nextInt(2);
            result.append(bit);
        }
        return result.toString();
    }

    public static void main(String[] args) {
        Random random = new Random();

        String randomBits = generateRandomBits(random, 128);

        System.out.println("Random sequence: " + randomBits);
    }
}