def compare(a, b):
    def longest_common_substring(A, B):
        m = len(A)
        n = len(B)
        
        # Membuat tabel untuk menyimpan panjang substring umum terpanjang.
        # Inisialisasi semua nilai tabel ke 0.
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Menyimpan panjang substring umum terpanjang
        longest = 0
        
        # Menyimpan indeks akhir dari substring terpanjang dalam A
        end_index = 0
        
        # Membangun tabel dp
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > longest:
                        longest = dp[i][j]
                        end_index = i
                else:
                    dp[i][j] = 0
        
        # Mengembalikan substring umum terpanjang
        return A[end_index - longest: end_index]

    return longest_common_substring(a, b)

if __name__ == '__main__':
    print(compare("AKA", "AKASHI"))  # AKA
    print(compare("KANGOORO", "KANG"))  # KANG
    print(compare("KI", "KIJANG"))  # KI
    print(compare("KUPU-KUPU", "KUPU"))  # KUPU
    print(compare("ILALANG", "ILA"))  # ILA
