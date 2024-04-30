#include <iostream>
#include <random>

/**
 * Generates a random binary string of length 128 using a shuffle order engine.
 *
 * @return The randomly generated binary string.
 */
std::string generate_random_shuffle() {
    std::random_device rd;
    std::shuffle_order_engine<std::mt19937, 2> gen(rd());

    std::string result;
    for (int i = 0; i < 128; ++i) {
        result += std::to_string(gen() % 2);
    }

    return result;
}

/**
 * Entry point of the program. Generates a random binary string and prints it to the console.
 *
 * @return 0 upon successful execution.
 */
int main() {
    std::string randomBits = generate_random_shuffle();
    std::cout << randomBits << std::endl;

    return 0;
}