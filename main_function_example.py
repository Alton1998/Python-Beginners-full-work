# Main function

# how do you run your code automatically

print(f'Name:{__name__}')
print(f'File:{__file__}')

def test():
    print('This is a test function')

def main():
    print('This is the maint function')
    test()

if __name__ == "__main__":
    main()