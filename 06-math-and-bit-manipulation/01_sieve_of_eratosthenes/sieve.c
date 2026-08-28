/**
 * Problem: Sieve of Eratosthenes (Prime Generation)
 * 
 * Time Complexity: O(N log log N)
 * Space Complexity: O(N)
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

void sieveOfEratosthenes(int n) {
    bool *prime = (bool *)malloc((n + 1) * sizeof(bool));
    for (int i = 0; i <= n; i++) prime[i] = true;

    for (int p = 2; p * p <= n; p++) {
        if (prime[p]) {
            for (int i = p * p; i <= n; i += p) {
                prime[i] = false;
            }
        }
    }

    printf("Primes up to %d: ", n);
    for (int p = 2; p <= n; p++) {
        if (prime[p]) printf("%d ", p);
    }
    printf("\n");
    free(prime);
}

int main(void) {
    printf("[C] Sieve of Eratosthenes Test\n");
    sieveOfEratosthenes(30);
    return 0;
}
