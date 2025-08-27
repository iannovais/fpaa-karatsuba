from karatsuba import karatsuba

def main():
    a = 11111111111111111
    b = 22222222222222222
    print("Karatsuba:", karatsuba(a, b))  
    print("Padrão:", a * b) 
    
if __name__ == "__main__":
    main()