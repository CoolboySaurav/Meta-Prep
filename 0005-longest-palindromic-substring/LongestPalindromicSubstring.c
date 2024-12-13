bool check(char* s, int i, int j);

char* longestPalindrome(char* s) {
    int length = strlen(s);
    char* result = strdup("");

    for (int len = length; len > 0; len--) {
        for (int start = 0; start <= strlen(s) - len; start++) {
            if (check(s, start, start + len)) {
                free(result);
                result = strndup(s + start, len);
                return result;
            }
        }
    }

    return result;
}

bool check(char* s, int i, int j) {
    int left = i;
    int right = j - 1;

    while (left < right) {
        if (s[left] != s[right]) {
            return false;
        }

        left++;
        right--;
    }

    return true;
}
