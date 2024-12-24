alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','_']

def caesar( encode_decode = input("enter encode or decode ").lower(), original_text = input("Enter text ").lower(), shift_amount = int(input("Enter shift amount ")) ):
    output_text = ""
    for z in original_text:
        if encode_decode == "decode":
            shift_amount = shift_amount*(-1)
        else:
            shift_amount = shift_amount
        positionz = alphabet.index(z)
        newpositionz = alphabet.index(z) + shift_amount%28
        output_text += alphabet[newpositionz]

    print(output_text)

caesar()
