def infixToPostfix(infixexpr):
    # menyimpan nilai tingkatan operator di dictionari python
    tingkatan_operator = {}
    tingkatan_operator["^"] = 4
    tingkatan_operator["*"] = 3
    tingkatan_operator["/"] = 3
    tingkatan_operator["+"] = 2
    tingkatan_operator["-"] = 2
    tingkatan_operator["("] = 1
    

    # inisialisasi stack kosong
    operator_stack = []

    #inisialisasi stack kosong untuk menyimpan hasil posfix
    postfix_list = []

    #looping token pada infix inputan yang telah ubah menjadi list token
    for token in infixexpr:

        #Jika token alfabet atau angka maka token akan dimasukkan ke postfixlist
        if token in "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz" or token in "0123456789":
            postfix_list.append(token)

        #Jika token = ( maka akan dimasukkan ke operator_stack
        elif token == '(':
            operator_stack.append(token)

        #Jika token = ) maka operator_stack yang ada di dlam operator stack akan di dikeluarkan semua sampe ketemu ( dan akan dimasukkan ke postfixlist
        elif token == ')':
            topToken = operator_stack.pop()
            while topToken != '(':
                postfix_list.append(topToken)
                topToken = operator_stack.pop()

        #jika operator_stack tdk kosong dan tingkatan operator yang paling terakhir didlm operator stack derajatnya >= tingkatan operator yang dicek
        # maka akan dimasukkan ke dalam postfix dan juga akan dikeluarkan dari operator stack sampe operator stack kosong
        # setelah operator_stack kosong maka token operator saat ini akan dimasukkan ke postfix_list
        else:
            while (len(operator_stack)!=0 ) and (tingkatan_operator[operator_stack[-1]] >= tingkatan_operator[token]):
                  postfixList.append(operator_stack.pop())
            operator_stack.append(token)
    # untuk isi operator_stack tdk kosong maka akan dimasukkan ke dalam postfix dan juga akan dikeluarkan dari operator stack sampe operator stack kosong
    while (len(operator_stack)!=0 ):
        postfix_list.append(operator_stack.pop())

    # menggabungkan postfix_list menjadi string
    return "".join(postfix_list)

#mengipnut notasi infix
infix= (raw_input('Masukkan notasi infix : '))

#mengubah notasi infix menjadi list dan membuang spasi 
infix=list(infix.replace(" ", ""))

# megubah infix menjadi postfix
postfix = infixToPostfix(infix)
print(postfix)
