from karatsuba import karatsuba

def main():
    a = 11111111111111111
    b = 22222222222222222
    n = max(len(str(a)), len(str(b)))
    print("Karatsuba:", karatsuba(a, b, n))  
    print("Padrão:", a * b) 
    
if __name__ == "__main__":
    main()