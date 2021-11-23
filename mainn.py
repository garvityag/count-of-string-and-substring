
def countSubstring(S, N):

    ans = 0;

    i = 0;


    while (i < N):


        cnt0 = 0;
        cnt1 = 0;


        if (S[i] == '0'):


            while (i < N and S[i] == '0'):
                cnt0 += 1;
                i += 1;


            j = i;


            while (j < N and S[j] == '1'):
                cnt1 += 1;
                j += 1;


        else:

            while (i < N and S[i] == '1'):
                cnt1 += 1;
                i += 1;

            j = i;

            while (j < N and S[j] == '0'):
                cnt0 += 1;
                j += 1;

        ans += min(cnt0, cnt1);

    return ans;

if __name__ == "__main__":
    S = "0001110010"
    N = len(S)


    print(countSubstring(S, N))
    print(S)


