class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        place = 0
        array = []
        for ch2 in num2[::-1]: 
            # get the number
            n1 = int(ch2)
            # print(n1)
            temp = [0] * place 
            carry = 0
            for ch1 in num1[::-1]:
                n2 = int(ch1)
                res = n1 * n2 + carry
                carry = res // 10 
                res = res % 10
                temp.append(res)
            if carry:
                temp.append(carry)
            array.append(temp)
            place += 1
        final = []

        # print(array)
        carry = 0
        for i in range(len(array[-1])):
            res = 0
            for j in range(len(array)):
                # print(f'array {array[j]} considering {i}')
                # if i not in range of array[i]
                if i >= len(array[j]):
                    # print('skipping')
                    continue
                res += array[j][i]
            # only append if number is less than 10,
            res += carry
            carry = res // 10
            res = res % 10
            final.append(res)
        if carry:
            final.append(carry)
        string = ''
        for i in range(len(final) -1, -1, -1):
            string = string + str(final[i])
        return string

