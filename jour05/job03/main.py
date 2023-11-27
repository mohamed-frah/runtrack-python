def draw_triangle(height):

    height = int(input("Veuillez rentrez la hauteur du triangle : "))
    
    
    for i in range(height - 1):

        left_space = ' ' * (height - i - 1)
        inner_space = ' ' * (2 * i)

       
        if i == 0:
         
            print(left_space + '/' + '\\' + left_space)
        else:
          
            print(left_space + '/' + inner_space + '\\' + left_space)

   
    print('/' + '_' * (2 * height - 2) + '\\')

draw_triangle(0)