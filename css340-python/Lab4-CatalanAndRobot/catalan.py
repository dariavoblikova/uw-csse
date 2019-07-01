import sys

def catalanNumber(num):
    catalan = 0
    if num < 0:
        catalan = None
    elif num == 0:
        catalan = 1
    else:
        for i in range(num):
            catalan = catalan + catalanNumber(i) * catalanNumber(num - i - 1)
    return catalan

if __name__ == "__main__":
    print(catalanNumber(int(sys.argv[1])))