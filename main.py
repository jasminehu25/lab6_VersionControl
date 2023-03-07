##Jasmine Hu

def decode(password):   # Decode function modified by Xin Zhao
    res = ""
    for num in password:
        new_num = str((int(num) - 3) % 10)
        res += new_num

    return res


def encode(password):

    res = "" ##final result

    for i in range(len(password)):
        curr_num = int(password[i]) ##stores value at i

        curr_num += 3 ##add 3

        str_num = str(curr_num) ##store num as string

        res = res + str_num ##add to result string

    return res


if __name__ == '__main__':

    newpass = ""

    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        print("Please enter an option:", end = "")
        option = input()

        password = ""

        if option == "1":
            print("\nPlease enter you password to encode:", end = "")
            password = input()
            newpass = encode(password)

            print("\nYour password has been encoded and stored!", newpass)

        if option == "2":

            ori_pass = decode(newpass)

            print("The encoded password is", newpass, ", and the original password is", ori_pass)

        if option == "3":
            break
